import torchvision
"""здесь пишем класс по считыванию данных, удобнее для каждого набора данных выделять отдельный файл и класс"""

class Dataset:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path


    def read_data(self):
        train_ds = torchvision.datasets.KMNIST(self.dataset_path, train=True,
                                               transform=torchvision.transforms.ToTensor(), target_transform=None,
                                               download=True)