from torch.utils.data import Dataset
from PIL import Image
import os


class MyDataSet(Dataset):
    """
    继承自Dataset类，需要重写__getitem__方法，也可以重写__len__方法
    """

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir).replace("\\", "/")
        self.img_list = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_list[idx]
        img_path = os.path.join(self.root_dir, self.label_dir, img_name).replace("\\", "/")
        img = Image.open(img_path)

        return img

    def __len__(self):
        return len(self.img_list)


root_dir = "/Users/ydchen/Documents/files/programming/jupyter-notebook/cat_classify/dataset"
label_dir = "cat_12_train"
my_dataset = MyDataSet(root_dir=root_dir, label_dir=label_dir)

img1 = my_dataset[0]
print(img1)


