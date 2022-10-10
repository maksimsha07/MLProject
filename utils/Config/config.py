from asyncio.windows_events import NULL
from msilib.schema import Class
import xml.etree.ElementTree as ET

from utils.Config.ModelConfig.Data import Data
from utils.Config.ModelConfig.Model import Model
from utils.Config.ModelConfig.Train import Train


class Config:
    """Класс конфиругации"""

    Data = NULL
    """Поле соответствует "data" в файле конфигураци"""

    Train = NULL
    """Поле соответствует "train" в файле конфигураци"""

    Model = NULL
    """Поле соответствует "model" в файле конфигураци"""

    def __init__(self, config_path):
        self.__from_xml(config_path)

    @classmethod
    def __from_xml(self,config_path):
        """Метод собираем блоки с данными из конфика и прокидывает в модели,
            уже в них происходить дальнейшая обработка
        """
        tree = ET.parse(config_path)
        root = tree.getroot()
        self.Data =  Data(root.findall('data')[0])
        self.Train = Train(root.findall('train')[0])
        self.Model = Model(root.findall('model')[0])
