from ast import List
from typing import List
import json
from typing import Callable
from datasets.Base.dataset import BaseDataSet
from enums.Datasets import DataSetType
import numpy as np
import idx2numpy
"""здесь пишем класс по считыванию данных, удобнее для каждого набора данных выделять отдельный файл и класс"""

class MNISTDataset(BaseDataSet):

    def __init__(self, dataset_type: DataSetType, transforms: List[Callable],
                nrof_classes: int,
                dataset_path = 'C:\\Users\\Admin\\Desktop\\MLProject\\configs\\data\\',
                image_file_name = 'train-images-idx3-ubyte',
                label_file_name = 'train-labels-idx1-ubyte'):
        self.__dataset_path = dataset_path
        self.__dataset_type = dataset_type
        self.__image_file_name = image_file_name
        self.__label_file_name = label_file_name
        self.__labels = []
        self.__images = []
        self.__transforms = transforms
        self.__nrof_classes = nrof_classes

    def _read_data(self):
        self.__labels = idx2numpy.convert_from_file(self.__dataset_path + self.__label_file_name)
        self.__images = idx2numpy.convert_from_file(self.__dataset_path + self.__image_file_name)

        self.show_statistics()

    def one_hot_labels(self, label):
        """
        для 10 классов метка 5-> [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        :param label: метка класса
        :return: one-hot encoding вектор
        """
        result = []
        if(abs(label) > self.__nrof_classes):
            raise ValueError('Такого класса не существует')

        for i in range(0,self.__nrof_classes):
            if(i == label):
                result.append(1)
            else:
                result.append(0)
        return result

    def __len__(self):
        return len(self.__images)

    def __getitem__(self, idx:int):
        images = self.__images[idx]
        labels = self.__labels[idx]
        for transform in self.__transforms:
            images = transform(images)
        return  images, labels
    
    def show_statistics(self):
        unique, counts = np.unique(self.__labels, return_counts=True)
        print(f'Датасет - {self.__dataset_type.name} \nКоличество элементов в датасете: {self.__len__()} \nКоличество классов: {self.__nrof_classes} \n{dict(zip(unique, counts))}\n')