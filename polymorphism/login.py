from abc import ABC, abstractclassmethod

class Login(ABC):
    @abstractclassmethod
    def login(self):
        pass