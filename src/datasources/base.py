
from abc import ABC, abstractmethod



class DataSource(ABC):


    @abstractmethod
    def find_documents(self):
        pass

    @abstractmethod
    def source_name(self):
        pass



