import datetime
from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def needs_service(self):
        service_interval = 2  # define the number of years between services for Spindler batteries
        
        time_since_last_service = self.current_date - self.last_service_date
        #from days to years 
        years_since_last_service = time_since_last_service.days/365.25
        
        return years_since_last_service  >= service_interval

class NubbinBattery(Battery):
    def needs_service(self):
        service_interval = 4  # define the number of years between services for Nubbin batteries
        time_since_last_service = self.current_date - self.last_service_date
        #from days to years 
        years_since_last_service = time_since_last_service.days/365.25
    
        return years_since_last_service >= service_interval
