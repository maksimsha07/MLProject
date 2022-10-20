from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
class DataLoader:
    """Data Loader class"""

    def __init__(self,dataset,batch_size,sample_type,
    epoch_size=None,
    shuffle = True):
        self.__dataset = dataset
        self.__batch_size = batch_size
        self.__shuffle = shuffle
        self.__sample_type = sample_type
        self.__epoch_size = epoch_size


    def batch_generator(self):
        """
        Создание батчей на эпоху с учетом указанного размера эпохи и типа сэмплирования.
        """
        indexes = np.arange(len(self.__dataset))
        if(self.__shuffle):
            np.random.shuffle(indexes)
        for i in range(0, len(indexes), self.__batch_size):
            self.__batch_img = self.__dataset[indexes[i: i+self.__batch_size]]
            yield self.__batch_img

    def show_batch(self):
        """
        Необходимо визуализировать и сохранить изображения в батче (один батч - одно окно). Предварительно привести значение в промежуток
        [0, 255) и типу к uint8
        :return:
        """
        img, label =  self.__batch_img

        pic_box = plt.figure(figsize=(10,6))

        for i, picture in enumerate(img):
            pic_box.add_subplot(
                int(sqrt(len(img)))+1,
                int(sqrt(len(img))),
                i+1)
            plt.imshow(picture)
            plt.title(label[i])
            plt.axis('off')

        plt.subplots_adjust(wspace=0.2, hspace=0.5)
        plt.show()
