# -*- coding: utf-8 -*-
""" main.py """

from utils.Config.config import Config
#from model.ExampleModel import ExampleModel


def run():
    """Builds model, loads data, trains and evaluates"""

    conf = Config('configs\\config.xml')

    print(conf.Data.path, conf.Data.image_size, conf.Data.load_with_info)
    print(conf.Train.batch_size, conf.Train.nrof_epoch, conf.Train.optimizer,conf.Train.metrics)
    print(conf.Model.input, conf.Model.up_stack, conf.Model.acivation_function, conf.Model.output)
    #model = ExampleModel(CFG)
    #model.load_data()
    #model.build()
    #model.train()
    #model.evaluate()


if __name__ == '__main__':
    run()
