# -*- coding: utf-8 -*-
"""Data Loader"""
"""Здесь находятся все классы и функции загрузки и предварительной обработки данных. При желании можно разделить"""
import torch, torchvision


class DataLoader:
    """Data Loader class"""

    @staticmethod
    def load_data(dataset):
        """Loads dataset from path"""

        dataloader = DataLoader(dataset, batch_size=data_config.batch_size, shuffle=True)
        return dataloader
