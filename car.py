from abc import ABC, abstractmethod
from engine import *
from battery import *

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.__engine = engine
        self.__battery = battery
        self.__tires = tires 

    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service() or self.__tires.needs_service()


