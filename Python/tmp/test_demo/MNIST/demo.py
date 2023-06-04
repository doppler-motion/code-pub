import numpy as np
import matplotlib.pyplot as plt
import logging.handlers
# from loguru import logger

from collections import OrderedDict

from load_mnist import load_mnist

# logging设置
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s:%(lineno)s : %(levelname)s %(message)s"
)

# fh = logging.FileHandler(filename="demo.log", mode="a", encoding=None, delay=False)
# fh = logging.StreamHandler(stream=None)
# formatter = logging.Formatter("%(asctime)s %(filename)s:%(lineno)s : %(levelname)s %(message)s")
# fh.setFormatter(formatter)
# fh.setLevel(logging.INFO)
# logging.getLogger().addHandler(fh)

logger = logging.getLogger(__name__)


# 与门的实现
def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp >= 0:
        return 1
    else:
        return 0


# 与非门的实现
def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 或门的实现
def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp >= 0:
        return 1
    else:
        return 0


# 异或门的实现
def xor_gate(x1, x2):
    y1 = or_gate(x1, x2)
    y2 = nand_gate(x1, x2)
    y = and_gate(y1, y2)
    return y


def numerical_diff(f, x):
    """
    数值微分
    :param f:
    :param x:
    :return:
    """
    h = 1e-4
    return (f(x + h) - f(x - h)) / 2 * h


def fun_1(x):
    return 0.01 * x ** 2 + 0.1 * x


def fun_2(x):
    return x[0] ** 2 + x[1] ** 2


def identify_function(x):
    return x


def step_function(x):
    """
    阶跃函数
    :param x:
    :return:
    """
    return np.array(x > 0, dtype=np.int_)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(x, 0)


def softmax_bak(x):
    c = np.max(x)
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a)

    y = exp_a / sum_exp_a

    return y


def softmax(x):
    # logger.info(f"x shape: {x.shape}, x ndim: {x.ndim}, x size: {x.size}")
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        # logger.info(f"y shape: {y.shape}, x ndim: {y.ndim}, x size: {y.size}")
        return y.T
    c = np.max(x)
    exp_a = np.exp(x - c)  # 溢出对策
    sum_exp_a = np.sum(exp_a)

    y = exp_a / sum_exp_a

    return y


def mean_squared_error(y, t):
    """
    均方误差
    :param y:
    :param t:
    :return:
    """
    return 0.5 * np.sum((y - t) ** 2)


def cross_entropy_errors(y, t):
    """
    交叉熵误差
    :param y:
    :param t:
    :return:
    """
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


def cross_entropy_error(y, t):
    # logger.info(f"y shape : {y.shape}, size: {y.size}, ndim: {y.ndim}")
    # logger.info(f"t shape : {t.shape}, size: {t.size}, ndim: {t.ndim}")
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)
    # logger.info(f"t shape : {t.shape}, size: {t.size}, ndim: {t.ndim}")

    batch_size = y.shape[0]
    # logger.info(f"batch_size : {batch_size}")

    y1 = y[np.arange(batch_size), t]
    # logger.info(f"y1 shape : {y1.shape}, size: {y1.size}, ndim: {y1.ndim}")

    val = -np.sum(np.log(y1 + 1e-7)) / batch_size

    return val


def numerical_gradient_bak(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val

    return grad


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=["multi_index"], op_flags=["readwrite"])
    while not it.finished:
        idx = it.multi_index

        tmp_val = x[idx]

        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        x[idx] = float(tmp_val) - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val
        it.iternext()

    return grad


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    """
    数值梯度
    :param f:
    :param init_x:
    :param lr:
    :param step_num:
    :return:
    """
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x


def init_network():
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    y1 = sigmoid(a1)
    a2 = np.dot(y1, W2) + b2
    y2 = sigmoid(a2)
    a3 = np.dot(y2, W3) + b3
    y = identify_function(a3)

    return y


# 乘法层的实现
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, dout):
        dx = dout * self.y  # 翻转x和y
        dy = dout * self.x

        return dx, dy


# 加法层的实现
class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        # logger.info(f"x shape : {x.shape}, size: {x.size}, ndim: {x.ndim}")
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        # logger.info(f"out shape : {out.shape}, size: {out.size}, ndim: {out.ndim}")

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        # out = 1 / (1 + np.exp(-x))
        out = softmax(x)
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1 - self.out) * self.out

        return dx


class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.original_x_shape = None
        # 权重和偏置参数的导数
        self.dW = None
        self.dx = None

    def forward(self, x):
        # 对应的张量
        # self.x = x
        # logger.info(f"x shape : {x.shape}, size: {x.size}, ndim: {x.ndim}")
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        # logger.info(f"x shape : {x.shape}, size: {x.size}, ndim: {x.ndim}")
        self.x = x

        # logger.info(f"self.W shape : {self.W.shape}, size: {self.W.size}, ndim: {self.W.ndim}")
        out = np.dot(self.x, self.W) + self.b
        # logger.info(f"out shape : {out.shape}, size: {out.size}, ndim: {out.ndim}")

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        dx = dx.reshape(*self.original_x_shape)  # 还原输入数据的形状（对应张量）
        return dx


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None  # 损失
        self.y = None  # softmax的输出
        self.t = None  # 监督数据（one-hot vector）

    def forward(self, x, t):
        # logger.info(f"x shape: {x.shape}, size: {x.size}, ndim: {x.ndim}")
        # logger.info(f"t shape: {t.shape}, size: {t.size}, ndim: {t.ndim}")
        self.t = t
        self.y = softmax(x)
        # logger.info(f"self.y shape: {self.y.shape}, size: {self.y.size}, ndim: {self.y.ndim}")
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        # batch_size = self.t.shape[0]
        # dx = (self.y - self.t) / batch_size

        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        return dx


class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]


class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for k, v in params.items():
                self.v[k] = np.zeros_like(v)

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.lr*grads[key]
            params[key] += self.v[key]


class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)  # 用高斯分布进行初始化

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        # # logger.info("z: ", z)
        # logger.info("type of z: ", type(z))
        y = softmax(z)
        # logger.info("y: ", y)
        # logger.info("type of y: ", type(y))
        loss = cross_entropy_error(y, t)

        return loss


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params["b2"] = np.zeros(output_size)

    def predict(self, x):
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]

        z1 = np.dot(x, W1) + b1
        y1 = sigmoid(z1)
        z2 = np.dot(y1, W2) + b2
        y2 = softmax(z2)

        return y2

    # x: 预测数据， t: 监督数据
    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

    # 准确度运算
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / np.float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads["W1"] = numerical_gradient(loss_W, self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W, self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W, self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W, self.params["b2"])

        return grads


class TwoLayersNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params["b2"] = np.zeros(output_size)

        # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["W1"], self.params["b1"])
        self.layers["Relu1"] = Relu()
        self.layers["Affine2"] = Affine(self.params["W2"], self.params["b2"])

        self.lastlayer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
            # logger.info(f"layer: {layer}, x: {x.shape}")

        return x

    # x: 预测数据， t: 监督数据
    def loss(self, x, t):
        # logger.info(f"x shape: {x.shape}, size: {x.size}, ndim: {x.ndim}")
        # logger.info(f"t shape: {t.shape}, size: {t.size}, ndim: {t.ndim}")
        y = self.predict(x)

        return self.lastlayer.forward(y, t)

    # 准确度运算
    def accuracy(self, x, t):
        y = self.predict(x)
        # logger.info(f"accuracy, y : {y.shape}, ndim : {y.ndim}")
        y = np.argmax(y, axis=1)
        # logger.info(f"accuracy, y : {y.shape}, ndim : {y.ndim}")
        if t.ndim != 1:
            t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads["W1"] = numerical_gradient(loss_W, self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W, self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W, self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W, self.params["b2"])

        return grads

    def gradient(self, x, t):
        # logger.info(f"x shape: {x.shape}, size: {x.size}, ndim: {x.ndim}")
        # logger.info(f"t shape: {t.shape}, size: {t.size}, ndim: {t.ndim}")
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.lastlayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        # logger.info("")
        for layer in layers:
            dout = layer.backward(dout)
            # logger.info(f"layer: {layer}, dout: {dout}")

        # 设定
        grads = {}
        grads["W1"] = self.layers["Affine1"].dW
        grads["b1"] = self.layers["Affine1"].db
        grads["W2"] = self.layers["Affine2"].dW
        grads["b2"] = self.layers["Affine2"].db

        return grads


def demo1():
    x = np.arange(0, 20, 0.1)
    y = fun_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.plot(x, y)
    plt.show()


def demo2():
    """
    单层网络的使用
    :return:
    """
    # 初始化网络
    net = simpleNet()
    # 输出权重值
    logger.info("weight value: ", net.W)
    x = np.array([0.6, 0.9])
    # 预测
    p = net.predict(x)
    logger.info("predict value: ", p)
    logger.info("index of max num: ", np.argmax(p))

    t = np.array([0, 0, 1])
    loss = net.loss(x, t)
    logger.info("loss: ", loss)

    f = lambda w: net.loss(x, t)

    dW = numerical_gradient(f, net.W)
    logger.info("dW: ", dW)


def demo3():
    """
    两层网络的使用
    :return:
    """
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    logger.info(net.params["b1"])

    # 伪数据
    x = np.random.rand(100, 784)
    logger.info("x: ", x)
    y = net.predict(x)
    logger.info("y: ", y)

    # 伪正确标签
    t = np.random.rand(100, 10)
    grads = net.numerical_gradient(x, t)
    logger.info("grads['W1']: ", grads["W1"])


def demo4():
    """
    基本函数的使用
    :return:
    """
    grad1 = numerical_diff(fun_1, 10)
    logger.info("grad1: ", grad1)

    grad2 = numerical_diff(fun_1, 5)
    logger.info("grad2: ", grad2)

    grad3 = gradient_descent(fun_2, np.array([-3.0, 4.0]), lr=0.1, step_num=100)
    logger.info("grad3: ", grad3)

    arr1 = np.array([1, 2, 3])
    arr1_y = softmax(arr1)
    logger.info("arr1_y: ", arr1_y)

    t2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    y2 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    cross_entropy_error1 = cross_entropy_error(np.array(y2), np.array(t2))
    logger.info("cross_entropy_error: ", cross_entropy_error1)


def demo5():
    """
    画阶跃函数的图形
    :return:
    """
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)

    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()


def demo6():
    """
    np.nditer使用
    :return:
    """
    # 单维迭代
    x = np.arange(6).reshape(2, 3)
    logger.info("x: ", x)
    it = np.nditer(x, flags=["f_index"])
    logger.info("it: ", it)
    while not it.finished:
        logger.info("single iter %d<%s>" % (it[0], it.index))
        it.iternext()

    # 多维迭代
    x1 = np.arange(6).reshape(2, 3)
    it1 = np.nditer(x1, flags=["multi_index"], op_flags=["readwrite"])
    while not it1.finished:
        logger.info("multi iter %d<%s>" % (it1[0], it1.multi_index))
        it1.iternext()


def demo7():
    network = init_network()
    x = np.array([0.1, 0.3])
    y = forward(network, x)
    logger.info(y)


def demo8():
    """
    二层神经网络训练mnist
    :return:
    """
    # 先加载数据
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

    train_loss_list = []

    # 超参数
    iters_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1

    # 初始化网络
    network = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

    for i in range(iters_num):
        # 获取mini_batch
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        # 计算梯度
        grad = network.numerical_gradient(x_batch, t_batch)

        # 更新参数
        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate * grad[key]

        # 记录学习过程
        loss = network.loss(x_batch, t_batch)
        logger.info(f"{i} epoch loss: {loss}")
        train_loss_list.append(loss)


def demo9():
    """
    二层神经网络训练mnist,优化
    :return:
    """
    # 先加载数据
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

    # 超参数
    iters_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1

    # 训练损失值记录
    train_loss_list = []
    train_acc_list = []
    test_acc_list = []
    # 平均每个epoch重复的次数
    iter_per_epoch = max(train_size / batch_size, 1)

    # 初始化网络
    network = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

    for i in range(iters_num):
        # 获取mini_batch
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        # 计算梯度
        grad = network.numerical_gradient(x_batch, t_batch)

        # 更新参数
        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate * grad[key]

        # 记录学习过程
        loss = network.loss(x_batch, t_batch)
        logger.info(f"{i} epoch loss: {loss}")
        train_loss_list.append(loss)

        # 计算每个epoch的识别精度
        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            logger.info(f"train acc: {train_acc}, test acc: {test_acc}")

    # 绘制图形
    markers = {"train": "o", "test": "s"}
    x = np.arange(len(train_acc_list))
    plt.plot(x, train_acc_list, label="train acc")
    plt.plot(x, test_acc_list, label="test acc", linestyle="--")
    plt.xlabel("epochs")
    plt.ylabel("accuracy")
    plt.ylim(-0.1, 1.1)
    plt.legend(loc="lower right")
    plt.show()


def demo10():
    """
    数值微分和反向传播法，求梯度的对比
    :return:
    """
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

    network = TwoLayersNet(input_size=784, hidden_size=50, output_size=10)

    x_batch = x_train[:3]
    t_batch = t_train[:3]

    grad_numerical = network.numerical_gradient(x_batch, t_batch)
    grad_backup = network.gradient(x_batch, t_batch)

    # 求各个权重的绝对误差的平均值
    for key in grad_numerical.keys():
        diff = np.average(np.abs(grad_backup[key] - grad_numerical[key]))
        logger.info(key + ":" + str(diff))


def demo11():
    """
    误差反向传播学习
    :return:
    """
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
    # logger.info(f"x_train shape: {x_train.shape}, size: {x_train.size}")
    # logger.info(f"t_train shape: {t_train.shape}, size: {t_train.size}")
    # logger.info(f"x_test shape: {x_test.shape}, size: {x_test.size}")
    # logger.info(f"t_test shape: {t_test.shape}, size: {t_test.size}")

    network = TwoLayersNet(input_size=784, hidden_size=100, output_size=10)
    # logger.info(f"network params keys: {network.params.keys()}")
    # logger.info(f"network layers keys: {network.layers.keys()}")

    iter_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1
    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iter_each_epoch = max(train_size / batch_size, 1)
    # logger.info(f"iter_each_epoch: {iter_each_epoch}")

    for i in range(iter_num):
        batch_mask = np.random.choice(train_size, batch_size)
        # logger.info(f"batch_mask : {batch_mask}")
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        # 通过误差反向传播法求梯度
        grad = network.gradient(x_batch, t_batch)

        # 更新
        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate * grad[key]

        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)

        if i % iter_each_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            logger.info(f"train_acc: {train_acc}, test_acc: {test_acc}")


def demo12():
    pass


if __name__ == "__main__":
    demo10()
