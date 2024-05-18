import tensorflow as tf
import os
import timeit

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 用GPU 0号卡

gpu_device_name = tf.test.gpu_device_name()
print(gpu_device_name)

with tf.device('/gpu:0'):
    with tf.compat.v1.Session() as sess:
        # Here 6 GBs of GPU RAM are allocated.
        #     4.time.sleep(10)
        a = tf.constant([1, 2, 3, 4], dtype=tf.float32)
        a = tf.expand_dims(a, -1)
        a_sum = tf.reduce_sum(a, 1)
        print(sess.run(a_sum))

tensorflow_version = tf.__version__
gpu_available = tf.config.list_physical_devices("GPU")

print('tensorflow version:', tensorflow_version, '\tGPU available:', gpu_available)

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([1.0, 2.0], name='b')
result = tf.add(a, b, name='add')
print(result)

with tf.device('/cpu:0'):
    cpu_a = tf.random.normal([10000, 1000])
    cpu_b = tf.random.normal([1000, 2000])
    print(cpu_a.device, cpu_b.device)

with tf.device('/gpu:0'):
    gpu_a = tf.random.normal([10000, 1000])
    gpu_b = tf.random.normal([1000, 2000])
    print(gpu_a.device, gpu_b.device)


def cpu_run():
    with tf.device('/cpu:0'):
        c = tf.matmul(cpu_a, cpu_b)
    return c


def gpu_run():
    with tf.device('/gpu:0'):
        c = tf.matmul(gpu_a, gpu_b)
    return c


# warm up
cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('warmup:', cpu_time, gpu_time)

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('run 4.time:', cpu_time, gpu_time)
