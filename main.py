from asyncio.windows_events import NULL
from dataloader.dataloader import DataLoader
from datasets.mnist_dataset import MNISTDataset
from enums.Datasets import DataSetType
from utils.Config.config import Config
from utils.Transform import Normalize, View
from matplotlib import pyplot as plt


def run():

    conf = Config('configs\\config.xml')

    #Инициализация тренировочного датасета
    train_ds = MNISTDataset(dataset_type=DataSetType.Train, transforms= [Normalize(),View()],nrof_classes=conf.Data.nrof_classes)
    #Инициализация тестового датасета
    test_ds = MNISTDataset(dataset_type=DataSetType.Test, transforms=[], nrof_classes=conf.Data.nrof_classes,
                            image_file_name='t10k-images-idx3-ubyte',
                            label_file_name='t10k-labels-idx1-ubyte')
    #Подготавливаем данные для тренировочного и тестового датасета
    train_ds._read_data()
    test_ds._read_data()

    #Инифиализация даталоадера с тренировочным и тестовым датасетом
    train_dataloared = DataLoader(train_ds,conf.Train.batch_size,None,conf.Train.nrof_epoch)
    test_dataloader = DataLoader(test_ds,conf.Train.batch_size,None,conf.Train.nrof_epoch)

    #Берем один батч из тренировочной и тестовой выборки и показываем его
    next(train_dataloared.batch_generator())
    train_dataloared.show_batch()


if __name__ == '__main__':
    run()
