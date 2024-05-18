import torch
from torch.utils.data import Dataset, DataLoader


class MyData(Dataset):
    def __init__(self):
        super(MyData, self).__init__()

        self.x = torch.randn(1000, 3)
        self.y = self.x.sum(axis=1)

        self.src, self.trg = [], []
        for i in range(1000):
            self.src.append(self.x[i])
            self.trg.append(self.y[i])

    def __getitem__(self, item):
        return self.src[item], self.trg[item]

    def __len__(self):
        return len(self.src)


train_dataset = MyData()
test_dataset = MyData()
dataloader_train = DataLoader(train_dataset, batch_size=5, shuffle=False)
dataloader_test = DataLoader(test_dataset, batch_size=5, shuffle=False)

for i_batch, batch_data in enumerate(dataloader_train):
    print(i_batch)
    print(batch_data[0])
    print(batch_data[1])
