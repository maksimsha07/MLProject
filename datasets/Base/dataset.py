from abc import ABC, abstractmethod

class BaseDataSet(ABC):
    """Базоый класс для датасетов"""

    @abstractmethod
    def _read_data(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass

    @abstractmethod
    def show_stat(self):
        pass