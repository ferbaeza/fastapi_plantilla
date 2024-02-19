from abc import ABC, abstractmethod

class BaseController(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def list(self, filters):
        pass