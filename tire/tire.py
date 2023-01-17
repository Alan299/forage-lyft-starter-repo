from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self,percentage_used):
        self.percentage_used = percentage_used 

    @abstractmethod
    def needs_service(self):
        pass

class CarriganTire(Tire):

    def needs_service(self):
        return any( list(map(lambda x: x>= 0.9, self.percentage_used)))

class OctoprimeTire(Tire):

    def needs_service(self):
        return sum(self.percentage_used) >= 3

       
