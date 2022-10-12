# -*- coding: utf-8 -*-
""" main.py """

from datasets.mnist_dataset import MNISTDataset
from enums.Datasets import DataSetType
from utils.Config.config import Config
#from model.ExampleModel import ExampleModel


def run():
    """Builds model, loads data, trains and evaluates"""

    conf = Config('configs\\config.xml')

    dataset = MNISTDataset(dataset_type=DataSetType.Train)

    print(dataset.show_stat())
    #model = ExampleModel(CFG)
    #model.load_data()
    #model.build()
    #model.train()
    #model.evaluate()


if __name__ == '__main__':
    run()
