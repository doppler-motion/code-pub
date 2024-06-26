import urllib.request
import os.path
import pickle
import gzip
import os
import numpy as np

url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
    'train_img': 'train-images-idx3-ubyte.gz',
    'train_label': 'train-labels-idx1-ubyte.gz',
    'test_img': 't10k-images-idx3-ubyte.gz',
    'test_label': 't10k-labels-idx1-ubyte.gz'
}

train_num = 60000
test_num = 10000
img_dim = (1, 28, 28)
img_size = 784

dataset_dir = os.path.dirname(os.path.abspath(__file__))
print(dataset_dir)
save_file = dataset_dir + "/mnist.pkl"


def _download(filename):
    file_path = dataset_dir + "/" + filename

    if os.path.exists(file_path):
        return

    print(f"Downloading {filename} ...")
    urllib.request.urlretrieve(url_base + filename, file_path)
    print("Done.")


def download_mnist():
    for v in key_file.values():
        _download(v)


def _load_label(file_name):
    file_path = dataset_dir + "/" + file_name

    print("Converting " + file_name + "to numpy Array...")
    with gzip.open(file_path, "rb") as f:
        data = np.frombuffer(f.read(), np.uint8, offset=8)
    print("Done.")
    return data


def _load_img(file_name):
    file_path = dataset_dir + "/" + file_name

    print("Converting " + file_name + "to numpy Array...")
    with gzip.open(file_path, "rb") as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)

    data = data.reshape(-1, img_size)
    print("Done")
    return data


def _convert_to_numpy():
    dataset = {}
    dataset["train_img"] = _load_img(key_file["train_img"])
    dataset["train_label"] = _load_label(key_file["train_label"])
    dataset["test_img"] = _load_img(key_file["test_img"])
    dataset["test_label"] = _load_label(key_file["test_label"])

    return dataset


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1
    return T


def init_mnist():
    download_mnist()

    dataset = _convert_to_numpy()
    print("Creating 6.pickle file ...")

    with open(save_file, "wb") as f:
        pickle.dump(dataset, f, -1)
    print("Done.")


def load_mnist(normalize=True, flatten=True, one_hot_label=False):
    if not os.path.exists(save_file):
        init_mnist()

    with open(save_file, "rb") as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ("train_img", "test_img"):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0

    if not flatten:
        for key in ("train_img", "test_img"):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)

    if one_hot_label:
        dataset["train_label"] = _change_one_hot_label(dataset["train_label"])
        dataset["test_label"] = _change_one_hot_label(dataset["test_label"])

    return (dataset["train_img"], dataset["train_label"]), (dataset["test_img"], dataset["test_label"])


if __name__ == "__main__":
    init_mnist()
