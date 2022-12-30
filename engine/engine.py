from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        service_interval = 1000  # define the number of miles between services for Capulet engines
        miles_since_last_service = self.current_mileage - self.last_service_mileage
        return miles_since_last_service >= service_interval

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        service_interval = 5000  # define the number of miles between services for Willoughby engines
        miles_since_last_service = self.current_mileage - self.last_service_mileage
        return miles_since_last_service >= service_interval

class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on