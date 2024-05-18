import os.path
import time

import numpy as np
import pickle
import matplotlib.pyplot as plt
from collections import OrderedDict

save_file = os.path.dirname(__file__) + "/mnist.pkl"


class Network:
    def __init__(self, input_size, hidden_size, out_size):
        I, H, O = input_size, hidden_size, out_size

        self.params = {}
        self.params["W1"] = np.random.randn(I, H).astype("f")
        self.params["b1"] = np.random.randn(H).astype("f")
        self.params["W2"] = np.random.randn(H, O).astype("f")
        self.params["b2"] = np.random.randn(O).astype("f")

        self.out = None

    def predict(self, x):
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]
        a = np.dot(x, W1) + b1
        out = np.dot(a, W2) + b2
        return out

    def forward(self, x):
        y = self.predict(x)
        return y

    def loss(self, x, t):
        y = self.forward(x)
        error = y - t
        sample_nums = error.shape[0]
        loss = error * error
        loss = np.sum(loss) / sample_nums
        return loss

    def gradient(self, dout, t):
        pass


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def step_function(x):
    # if x > 0:
    #     return x
    # if x <= 0:
    #     return 0
    y = x > 0
    return np.array(y, dtype=np.int)


def ReLu(x):
    return np.maximum(0, x)


def softmax(x):
    if x.ndim == 1:
        max_x = np.max(x)
        exp_x = np.exp(x - max_x)
        sum_x = np.sum(exp_x)
        y = exp_x / sum_x
        return y
    elif x.ndim == 2:
        max_x = np.max(x, axis=1, keepdims=True)
        exp_x = np.exp(x - max_x)
        sum_x = np.sum(exp_x, axis=1, keepdims=True)
        return exp_x / sum_x


# a = np.array([0.3, 2.9, 4.0])
# print(np.max(a))
# print(np.exp(a - np.max(a)))
# print(np.sum(np.exp(a - np.max(a))))
# print(np.exp(a - np.max(a)) / np.sum(np.exp(a - np.max(a))))
# print(a.ndim)
# s_out = softmax(a)
# print(f"s_out: {s_out}")

# x = np.arange(-5, 5, 0.1)
# y1 = step_function(x)
# y2 = sigmoid(x)
# y3 = ReLu(x)
# y4 = np.exp(-x)

# fig = plt.figure(figsize=(5, 5))
# plt.xlim(-5.1, 5.1)
# plt.ylim(-0.1, 1.1)
# plt.plot(x, y1)
# plt.plot(x, y2, linestyle="--")
# plt.plot(x, y3, linestyle="-")
# plt.plot(x, y4)
#
# plt.show()

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a.shape)
# print(a.ndim)
# print(a.size)
#
# X = np.array(np.arange(1, 3))
# print(X)
# W = np.array(np.arange(6).reshape(2, 3))
# print(W)
#
# out = np.dot(X, W)
# print(out)

# X1 = np.array(np.arange(1, 4).reshape(1, 3))
# print(X1)
# W1 = np.array(np.arange(6).reshape(3, 2))
# print(W1)
# B1 = np.array([7, 8])
# print(B1)
#
# out1 = np.dot(X1, W1) + B1
# print(out1)
#
# z = sigmoid(out1)
# print(z)

def init_network():
    network = {}
    network["W1"] = np.array(np.random.randn(2, 3))
    network["b1"] = np.array(np.random.randn(3))
    network["W2"] = np.array(np.random.randn(3, 4))
    network["b2"] = np.array(np.random.randn(4))
    network["W3"] = np.array(np.random.randn(4, 2))
    network["b3"] = np.array(np.random.randn(2))

    return network


def forward():
    network = init_network()
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    x = np.array(np.random.randn(1, 2))
    a1 = np.dot(x, W1) + b1
    a1 = sigmoid(a1)
    a2 = np.dot(a1, W2) + b2
    a2 = sigmoid(a2)
    a3 = np.dot(a2, W3) + b3
    y = sigmoid(a3)
    return y


# y_out = forward()
# print(y_out)

# a = np.array(np.arange(0.1, 1.0, 0.3))
# print(a)
# exp_a = np.exp(a)
# print(exp_a)
# sum_exp_a = np.sum(exp_a)
# print(sum_exp_a)
# exp_a_y = exp_a / sum_exp_a
# print(exp_a_y)
#
# a1 = np.array(np.random.randn(3, 4))
# print(a1.size)
# print(a1.shape)
# print(a1)
# max_a1 = np.max(a1, axis=1, keepdims=True)
# print(max_a1)
# a1 = a1 - max_a1
# print(a1)
# exp_a1 = np.exp(a1)
# print(exp_a1)
# sum_a1 = np.sum(exp_a1, axis=1, keepdims=True)
# print(sum_a1)
# y_out_a1 = exp_a1/sum_a1
# print(y_out_a1)

y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])  # 预测结果
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])  # 正确解标签 one-hot表示


def mean_square_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


mean_error = mean_square_error(y, t)


# print(mean_error)


def cross_entropy_error_1d(y, t):
    return -np.sum(t * np.log(y + 1e-7))


cross_error = cross_entropy_error_1d(y, t)
print(cross_error)


def cross_entropy_error_2D(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def cross_entropy_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    if y.size == t.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


y = np.random.randn(5, 11)


# print(y)
# t = np.array([2, 7, 0, 9, 4]).repeat(5, axis=0)

# out1 = cross_entropy_error_2D(y, t)
# print(out1)

def func1(x):
    return 0.01 * x ** 2 + 0.1 * x


def func2(x):
    return x[0] ** 2 + x[1] ** 2


def numerical_gradient_simple(f, x):
    delta = 1e-4
    return (f(x + delta) - f(x - delta)) / (2 * delta)


def numerical_gradient_1d(f, x):
    delta = 1e-4
    grads = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + delta
        d1 = f(x)

        x[idx] = tmp_val - delta
        d2 = f(x)

        grads[idx] = (d1 - d2) / (2 * delta)
        x[idx] = tmp_val

    return grads


a = np.array(np.arange(10))
b = func1(a)

# plt.figure(figsize=(5, 5))
# plt.ylim(-1, 10)
# plt.xlim(-1, 10)
# plt.plot(a, b)
# plt.show()

# print(numerical_gradient(func1, 6))
print(numerical_gradient_1d(func2, np.array([0.7, 0.9])))
print(numerical_gradient_1d(func2, np.array([3.0, 4.0])))


def gradient_descent(f, init_x, lr=0.1, step_num=100):
    x = init_x

    for i in range(step_num):
        grads = numerical_gradient_1d(f, x)
        x -= lr * grads

    return x


# print(gradient_descent(func2, np.array([3.0, 4.0])))


def numerical_gradient(f, x):
    delta = 1e-4
    grads = np.zeros_like(x)

    it = np.nditer(x, flags=["multi_index"], op_flags=["readwrite"])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + delta
        d1 = f(x)

        x[idx] = tmp_val - delta
        d2 = f(x)

        grads[idx] = (d1 - d2) / (2 * delta)
        x[idx] = tmp_val
        it.iternext()
    return grads


class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(3, 4)

    def predict(self, x):
        out = np.dot(x, self.W)
        return out

    def loss(self, x, t):
        out = self.predict(x)
        y = softmax(out)
        loss = cross_entropy_error_2D(y=y, t=t)
        return loss


# simple_net = SimpleNet()
# print(simple_net.W)
# x = np.array([0.3, 0.6, 0.9])
# p = simple_net.predict(x)
# print(p)
# t = np.array([0, 1, 0, 0])
# print(simple_net.loss(x, t))


def f(W):
    return simple_net.loss(x, t)


# dW = numerical_gradient(f, simple_net.W)
# print(dW)


class TwoLayerNetLower:
    def __init__(self, input_size, hidden_size, output_size, init_size=0.01):
        I, H, O = input_size, hidden_size, output_size

        self.params = {}
        self.params["W1"] = init_size * np.random.randn(I, H)
        self.params["b1"] = np.zeros(H)
        self.params["W2"] = init_size * np.random.randn(H, O)
        self.params["b2"] = np.zeros(O)

    def predict(self, x):
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]

        a = np.dot(x, W1) + b1
        a = sigmoid(a)
        y = np.dot(a, W2) + b2
        y = softmax(y)
        return y

    def loss(self, x, t):
        y = self.predict(x)

        loss = cross_entropy_error(y, t)

        return loss

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads["W1"] = numerical_gradient(loss_W, self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W, self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W, self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W, self.params["b2"])

        return grads


two_layer_net_low = TwoLayerNetLower(input_size=784, hidden_size=100, output_size=10)


# two_y = two_layer_net.predict(x)
# loss_y = two_layer_net.loss(x, t)
# grad_y = two_layer_net.numerical_gradient(x, t)
# print(two_y.shape)
# print(loss_y)
# print(grad_y)

def _change_one_hot(x):
    T = np.zeros((x.size, 10))
    for idx, row in enumerate(T):
        row[x[idx]] = 1

    return T


def load_data(normalize=True, one_hot_label=False, flatten=True):
    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ("train_img", "test_img"):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0

    if one_hot_label:
        dataset["train_label"] = _change_one_hot(dataset["train_label"])
        dataset["test_label"] = _change_one_hot(dataset["test_label"])

    if not flatten:
        for key in ("train_img", "test_img"):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)

    return (dataset["train_img"], dataset["train_label"]), (dataset["test_img"], dataset["test_label"])


# (x_train, t_train), (x_test, t_test) = load_data(normalize=True, one_hot_label=True)
# print(x_train.shape)
# print(t_train.shape)
#
# batch_size = 100
# train_size = x_train.shape[0]
# iters = 10
# learning_rate = 0.001
#
# for i in range(iters):
#     batch_mask = np.random.choice(train_size, batch_size)
#     x_batch = x_train[batch_mask]
#     t_batch = t_train[batch_mask]
#     print(x_batch.shape)
#     print(t_batch.shape)
#     # 计算梯度
#     grad = two_layer_net_low.numerical_gradient(x_batch, t_batch)
#
#     # 更新参数
#     for key in ("W1", "b1", "W2", "b2"):
#         two_layer_net.params[key] -= learning_rate * grad[key]
#     print(grad)
#     print(len(grad))
#     break


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y

        out = x * y
        return out

    def backward(self, dout=1):
        dx = self.y * dout
        dy = self.x * dout

        return dx, dy


class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout=1):
        dx = 1 * dout
        dy = 1 * dout

        return dx, dy


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx


class Affine:
    def __init__(self, W, b):
        self.params = [W, b]

        self.x = None
        self.original_x_shape = None
        # 权重和偏置参数的导数
        self.dW = None
        self.db = None

    def forward(self, x):
        # 对应张量
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x

        W, b = self.params
        y = np.dot(x, W) + b
        return y

    def backward(self, dout):
        W, b = self.params
        dW = np.dot(self.x.T, dout)
        dx = np.dot(dout, W.T)
        db = np.sum(dout, axis=0)
        self.dW = dW
        self.db = db

        dx = dx.reshape(*self.original_x_shape)  # 还原输入数据的形状（对应张量）
        return dx


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None  # 损失值
        self.y = None  # softmax的值
        self.t = None  # 监督标签

    def forward(self, x, t):
        self.t = t
        out = softmax(x)
        self.y = out
        loss = cross_entropy_error(out, t)
        self.loss = loss
        return loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:  # 监督标签是one-hot-label的形式
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        return dx


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, initialize=0.01):
        I, H, O = input_size, hidden_size, output_size

        self.params = {}
        self.params["W1"] = initialize * np.random.randn(I, H)
        self.params["b1"] = np.zeros(H)
        self.params["W2"] = initialize * np.random.randn(H, O)
        self.params["b2"] = np.zeros(O)

        # 生成层
        self.layers = OrderedDict()
        self.layers["aff1"] = Affine(self.params["W1"], self.params["b1"])
        self.layers["relu1"] = Relu()
        self.layers["aff2"] = Affine(self.params["W2"], self.params["b2"])
        self.lastlayer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x

    def loss(self, x, t):
        y = self.predict(x)
        loss = self.lastlayer.forward(y, t)

        return loss

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1:
            t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def gradient(self, x, t):
        # 计算损失
        self.loss(x, t)
        # 反向传播
        dout = 1
        dout = self.lastlayer.backward(dout)

        layers = list(self.layers.values())
        for layer in layers[::-1]:
            dout = layer.backward(dout)

        # 梯度保存
        grads = {}
        grads["W1"] = self.layers["aff1"].dW
        grads["b1"] = self.layers["aff1"].db
        grads["W2"] = self.layers["aff2"].dW
        grads["b2"] = self.layers["aff2"].db
        return grads

    def numerical_gradient(self, x, t):
        loss_w = lambda W: self.loss(x, t)

        grads = {}
        grads["W1"] = numerical_gradient(loss_w, self.params["W1"])
        grads["b1"] = numerical_gradient(loss_w, self.params["b1"])
        grads["W2"] = numerical_gradient(loss_w, self.params["W2"])
        grads["b2"] = numerical_gradient(loss_w, self.params["b2"])

        return grads


x = np.random.randn(100, 784)
t = np.random.randn(100, 10)

# (x_train, t_train), (x_test, t_test) = load_data(normalize=True, one_hot_label=True)
#
# two_layer_net = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# y = two_layer_net.predict(x)
# print(y.shape)
# loss = two_layer_net.loss(x, t)
# print(loss)
# start = int(4.time.4.time())
# grad = two_layer_net.numerical_gradient(x, t)
# print(grad)
# end = int(4.time.4.time())
# print(end - start)
# start = int(4.time.4.time())
# grad1 = two_layer_net.gradient(x, t)
# print(grad1)
# end = int(4.time.4.time())
# print(end - start)

# 梯度的验证
# x_batch = x_train[:3]
# t_batch = t_train[:3]
#
# grad_numerical = two_layer_net.numerical_gradient(x_batch, t_batch)
# grad_backprop = two_layer_net.gradient(x_batch, t_batch)
#
# for key in grad_numerical.keys():
#     diff = np.average(np.abs(grad_backprop[key]) - grad_numerical[key])
#     print(f"{key}: {str(diff)}")

# 进行神经网络的学习
# 超参数
# learning_rate = 0.1
# iters_num = 10000
# train_size = x_train.shape[0]
# batch_size = 100
# train_loss_list = []
# train_acc_list = []
# test_acc_list = []
#
# iter_each_epoch = max(train_size / batch_size, 1)
#
# for i in range(iters_num):
#     batch_mask = np.random.choice(train_size, batch_size)
#     x_batch = x_train[batch_mask]
#     t_batch = t_train[batch_mask]
#
#     # 计算梯度
#     grads = two_layer_net.gradient(x_batch, t_batch)
#
#     # 更新参数
#     for key in ("W1", "b1", "W2", "b2"):
#         two_layer_net.params[key] -= learning_rate * grads[key]
#
#     loss = two_layer_net.loss(x_batch, t_batch)
#     train_loss_list.append(loss)
#
#     if i % iter_each_epoch == 0:
#         train_acc = two_layer_net.accuracy(x_train, t_train)
#         test_acc = two_layer_net.accuracy(x_test, t_test)
#         train_acc_list.append(train_acc)
#         test_acc_list.append(test_acc)
#         print(train_acc, test_acc)


# 隐藏层的激活值的分布
# x_act = np.random.randn(1000, 100)  # 输入值
# node_num = 100  # 各隐藏层的节点数
# hidden_layer_size = 5  # 隐藏层有5层
# activations = {}  # 激活值的结果保存在这里
#
# for i in range(hidden_layer_size):
#     if i != 0:
#         x_act = activations[i-1]
#
#     # 改变权重的初始值，进行试验
#     # w = np.random.randn(node_num, node_num) * 1
#     # w = np.random.randn(node_num, node_num) * 0.01
#     w = np.random.randn(node_num, node_num) / np.sqrt(node_num)
#
#     z = np.dot(x_act, w)
#
#     # 切换不同的函数进行试验
#     # a = sigmoid(z)
#     a = ReLu(z)
#     activations[i] = a
#
# for i, a in activations.items():
#     plt.subplot(1, len(activations), i + 1)
#     plt.title(str(i+1) + "-layer")
#     plt.hist(a.flatten(), 30, range=(0, 1))
# plt.show()


x_4D = np.random.randn(10, 1, 28, 28)
print(x_4D.shape)


def im2col(input_data, filter_w, filter_h, stride=1, pad=0):
    """
    将图像转换为二维矩阵形式
    :param input_data: 由（数据量，通道，高，长）的4维数组构成输入数据
    :param filter_w: 滤波器的高
    :param filter_h:  滤波器的宽
    :param stride: 步长
    :param pad: 填充
    :return: col：2维数组
    """
    N, C, H, W = input_data.shape
    out_h = (H + 2 * pad - filter_h) // stride + 1
    out_w = (W + 2 * pad - filter_w) // stride + 1

    img = np.pad(input_data, [(0, 0), (0, 0), (pad, pad), (pad, pad)], "constant")
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

    for y in range(filter_h):
        y_max = y + stride * out_h
        for x in range(filter_w):
            x_max = x + stride * out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N * out_h * out_w, -1)
    return col


def col2img(col, input_data, filter_h, filter_w, stride=1, pad=0):
    """
    将矩阵转换为图像
    :param col: 2维数组
    :param input_data: 输入数据的形状(例如：(10, 1, 28, 28))
    :param filter_h: 滤波器大小
    :param filter_w: 滤波器大小
    :param stride: 步长
    :param pad: 填充
    :return:
    """
    N, C, H, W = input_data
    out_h = (H + 2 * pad - filter_h) // stride + 1
    out_w = (W + 2 * pad - filter_w) // stride + 1
    col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

    img = np.zeros((N, C, H + 2 * pad + stride - 1, W + 2 * pad + stride - 1))
    for y in range(filter_h):
        y_max = y + stride * out_h
        for x in range(filter_w):
            x_max = x + stride * out_w
            img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

    return img[:, :, pad:H + pad, pad:W + pad]


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

        # 中间数据（backward时使用）
        self.x = None
        self.col = None
        self.col_W = None

        # 权重和偏置参数的梯度
        self.dW = None
        self.db = None

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = 1 + int((H + 2 * self.pad - FH) / self.stride)
        out_w = 1 + int((W + 2 * self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
        col_W = self.W.reshape(FN, -1).T

        out = np.dot(col, col_W) + self.b
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        self.x = x
        self.col = col
        self.col_W = col_W

        return out

    def backward(self, dout):
        FN, C, FH, FW = self.W.shape
        dout = dout.transpose(0, 2, 3, 1).reshape(-1, FN)

        self.db = np.sum(dout, axis=0)
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_W.T)
        dx = col2img(dcol, self.x.shape, FH, FW, self.stride, self.pad)

        return dx


class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad

        self.x = None
        self.arg_max = None

    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)

        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h * self.pool_w)

        arg_max = np.argmax(col, axis=1)
        out = np.max(col, axis=1)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        self.x = x
        self.arg_max = arg_max

        return out

    def backward(self, dout):
        dout = dout.transpose(0, 2, 3, 1)

        pool_size = self.pool_h * self.pool_w
        dmax = np.zeros((dout.size, pool_size))
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
        dmax = dmax.reshape(dout.shape + (pool_size,))

        dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
        dx = col2img(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)

        return dx


class SimpleConvNet:
    """简单的ConvNet

    conv - relu - pool - affine - relu - affine - softmax

    Parameters
    ----------
    input_size : 输入大小（MNIST的情况下为784）
    hidden_size_list : 隐藏层的神经元数量的列表（e.g. [100, 100, 100]）
    output_size : 输出大小（MNIST的情况下为10）
    activation : 'relu' or 'sigmoid'
    weight_init_std : 指定权重的标准差（e.g. 0.01）
        指定'relu'或'he'的情况下设定“He的初始值”
        指定'sigmoid'或'xavier'的情况下设定“Xavier的初始值”
    """

    def __init__(self, input_dim=(1, 28, 28),
                 conv_param={"filter_num": 30, "filter_size": 5, "pad": 0, "stride": 1},
                 hidden_size=100, output_size=10, weight_init_std=0.01):
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_size']
        filter_pad = conv_param['pad']
        filter_stride = conv_param['stride']
        input_size = input_dim[1]
        conv_output_size = (input_size - filter_size + 2 * filter_pad) / filter_stride + 1
        pool_output_size = int(filter_num * (conv_output_size / 2) * (conv_output_size / 2))

        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(filter_num, input_dim[0],
                                                              filter_size, filter_size)
        self.params["b1"] = np.zeros(filter_num)
        self.params["W2"] = weight_init_std * np.random.randn(pool_output_size, hidden_size)
        self.params["b2"] = np.zeros(hidden_size)
        self.params["W3"] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params["b3"] = np.zeros(output_size)

        # 生成层
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                           conv_param['stride'], conv_param['pad'])
        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
        self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

        self.last_layer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        """求损失函数
        参数x是输入数据、t是教师标签
        """
        y = self.predict(x)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1: t = np.argmax(t, axis=1)

        acc = 0.0

        for i in range(int(x.shape[0] / batch_size)):
            tx = x[i * batch_size:(i + 1) * batch_size]
            tt = t[i * batch_size:(i + 1) * batch_size]
            y = self.predict(tx)
            y = np.argmax(y, axis=1)
            acc += np.sum(y == tt)

        return acc / x.shape[0]

    def numerical_gradient(self, x, t):
        """求梯度（数值微分）

        Parameters
        ----------
        x : 输入数据
        t : 教师标签

        Returns
        -------
        具有各层的梯度的字典变量
            grads['W1']、grads['W2']、...是各层的权重
            grads['b1']、grads['b2']、...是各层的偏置
        """
        loss_w = lambda w: self.loss(x, t)

        grads = {}
        for idx in (1, 2, 3):
            grads['W' + str(idx)] = numerical_gradient(loss_w, self.params['W' + str(idx)])
            grads['b' + str(idx)] = numerical_gradient(loss_w, self.params['b' + str(idx)])

        return grads

    def gradient(self, x, t):
        """求梯度（误差反向传播法）

        Parameters
        ----------
        x : 输入数据
        t : 教师标签

        Returns
        -------
        具有各层的梯度的字典变量
            grads['W1']、grads['W2']、...是各层的权重
            grads['b1']、grads['b2']、...是各层的偏置
        """
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W2'], grads['b2'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W3'], grads['b3'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

        return grads

    def save_params(self, file_name="params.pkl"):
        params = {}
        for key, val in self.params.items():
            params[key] = val
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)

    def load_params(self, file_name="params.pkl"):
        with open(file_name, 'rb') as f:
            params = pickle.load(f)
        for key, val in params.items():
            self.params[key] = val

        for i, key in enumerate(['Conv1', 'Affine1', 'Affine2']):
            self.layers[key].W = self.params['W' + str(i + 1)]
            self.layers[key].b = self.params['b' + str(i + 1)]


class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]


class Adam:
    """Adam (http://arxiv.org/abs/1412.6980v8)"""

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, value in params.items():
                self.m[key] = np.zeros_like(value)
                self.v[key] = np.zeros_like(value)

        self.iter += 1
        lr_t = self.lr * np.sqrt(1.0 - self.beta2 ** self.iter) / (1.0 - self.beta1 ** self.iter)

        for key in params.keys():
            # self.m[key] = self.beta1*self.m[key] + (1-self.beta1)*grads[key]
            # self.v[key] = self.beta2*self.v[key] + (1-self.beta2)*(grads[key]**2)
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key] ** 2 - self.v[key])

            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)

            # unbias_m += (1 - self.beta1) * (grads[key] - self.m[key]) # correct bias
            # unbisa_b += (1 - self.beta2) * (grads[key]*grads[key] - self.v[key]) # correct bias
            # params[key] += self.lr * unbias_m / (np.sqrt(unbisa_b) + 1e-7)

x_4d = np.random.randn(1, 3, 7, 7)

col1 = im2col(x_4D, 5, 5, stride=1, pad=0)
print(col1.shape)

col2 = im2col(x_4d, 5, 5)
print(col2.shape)


class Trainer:
    """进行神经网络训练的类"""

    def __init__(self, network, x_train, t_train, x_test, t_test,
                 epochs=20, mini_batch_size=100,
                 optimizer="SGD", optimizer_param={"lr": 0.01},
                 evaluate_sample_num_per_epoch=None, verbose=True):
        self.network = network
        self.x_train = x_train
        self.t_train = t_train
        self.x_test = x_test
        self.t_test = t_test
        self.epochs = epochs
        self.verbose = verbose
        self.batch_size = mini_batch_size
        self.evaluate_sample_num_per_epoch = evaluate_sample_num_per_epoch

        # optimizer dict
        optimizer_class_dict = {"sgd": SGD, "adam": Adam}
        self.optimizer = optimizer_class_dict[optimizer.lower()](**optimizer_param)

        self.train_size = self.x_train.shape[0]
        self.iter_per_epoch = max(self.train_size / mini_batch_size, 1)
        self.max_iter = int(epochs * self.iter_per_epoch)
        self.current_iter = 0
        self.current_epoch = 0

        self.train_loss_list = []
        self.train_acc_list = []
        self.test_acc_list = []

    def train_step(self):
        batch_mask = np.random.choice(self.train_size, self.batch_size)
        x_batch = self.x_train[batch_mask]
        t_batch = self.t_train[batch_mask]

        grads = self.network.gradient(x_batch, t_batch)
        self.optimizer.update(self.network.params, grads)

        loss = self.network.loss(x_batch, t_batch)
        self.train_loss_list.append(loss)

        if self.verbose:
            print(f"train loss: {loss}")

        if self.current_iter % self.iter_per_epoch == 0:
            self.current_epoch += 1

            x_train_sample, t_train_sample = self.x_train, self.t_train
            x_test_simple, t_test_simple = self.x_test, self.t_test

            if not self.evaluate_sample_num_per_epoch is None:
                t = self.evaluate_sample_num_per_epoch
                x_train_sample, t_train_sample = x_train_sample[:t], t_train_sample[:t]
                x_test_simple, t_test_simple = x_test_simple[:t], t_test_simple[:t]

            train_acc = self.network.accuracy(x_train_sample, t_train_sample)
            test_acc = self.network.accuracy(x_test_simple, t_test_simple)
            self.train_acc_list.append(train_acc)
            self.test_acc_list.append(test_acc)

            if self.verbose:
                print(f"===epoch: {self.current_epoch}, train acc: {str(train_acc)}, test acc : {str(test_acc)}")

        self.current_iter += 1

    def train(self):
        for i in range(self.max_iter):
            self.train_step()

        test_acc = self.network.accuracy(self.x_test, self.t_test)

        if self.verbose:
            print("=============== Final Test Accuracy ===============")
            print(f"test acc : {str(test_acc)}")


(x_train, t_train), (x_test, t_test) = load_data(flatten=False)

max_epochs = 20

network = SimpleConvNet(input_dim=(1, 28, 28), conv_param={"filter_num": 30, "filter_size": 5, "pad": 0, "stride": 1},
                        hidden_size=100, output_size=110, weight_init_std=0.01)

trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=max_epochs, mini_batch_size=100,
                  optimizer="Adam", optimizer_param={"lr": 0.001},
                  evaluate_sample_num_per_epoch=1000)

trainer.train()
