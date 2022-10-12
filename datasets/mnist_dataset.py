import json
from datasets.Base.dataset import BaseDataSet
from enums.Datasets import DataSetType
import numpy as np
import idx2numpy
"""здесь пишем класс по считыванию данных, удобнее для каждого набора данных выделять отдельный файл и класс"""

class MNISTDataset(BaseDataSet):

    data_class = 10

    def __init__(self, dataset_type: DataSetType,
                dataset_path = 'C:\\Users\\Admin\\Desktop\\MLProject\\configs\\data\\',
                image_file_name = 'train-images-idx3-ubyte',
                label_file_name = 'train-labels-idx1-ubyte'):
        self.__dataset_path = dataset_path
        self.__dataset_type = dataset_type
        self.__image_file_name = image_file_name
        self.__label_file_name = label_file_name
        self.__labels = []
        self.__images = []
        self._read_data()

    def _read_data(self):
        self.__labels = idx2numpy.convert_from_file(self.__dataset_path + self.__label_file_name)
        self.__images = idx2numpy.convert_from_file(self.__dataset_path + self.__image_file_name)

    def __len__(self):
        return len(self.__images)

    def __getitem__(self, indx):
        return (self.__images[indx], self.__labels[indx]) if abs(indx) < len(self.__images) else 'Неверный индекс' 
    
    def show_stat(self):
        unique, counts = np.unique(self.__labels, return_counts=True)
        print(f'Датасет - {self.__dataset_type.name} \nКоличество элементов в датасете: {self.__len__()} \nКоличество классов: {self.data_class} \n{dict(zip(unique, counts))}')