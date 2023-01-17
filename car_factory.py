import datetime
from car import *
from engine.engine import *
from battery.battery import *
from tire.tire import *

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage,tires_used):

        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        tires = CarriganTire(tires_used) 
        return Car(engine, battery,tires) 

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage,tires_used):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        tires = CarriganTire(tires_used) 
        return Car(engine, battery,tires)

    def create_palindrome(self, current_date, last_service_date, warning_light_on,tires_used):
        battery = NubbinBattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_on)
        tires = CarriganTire(tires_used) 
        return Car(engine, battery,tires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage,tires_used):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        tires = OctoprimeTire(tires_used) 
        return Car(engine, battery,tires)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage,tires_used):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        tires = OctoprimeTire(tires_used) 
        return Car(engine, battery,tires)