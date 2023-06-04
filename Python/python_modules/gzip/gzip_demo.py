import gzip
import numpy as np


with gzip.open("t10k-images-idx3-ubyte.gz", "rb") as f:
    dataset = np.frombuffer(f.read(), np.uint8, offset=16)

print("type of dataset: ", type(dataset))
print("ndim of dataset: ", dataset.ndim)
print("size of dataset: ", dataset.size)
print("shape of dataset: ", dataset.shape)
print("reshape of dataset: ", dataset.reshape(-1, 784).shape)
