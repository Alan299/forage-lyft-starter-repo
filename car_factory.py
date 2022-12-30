import datetime
from car import *
from engine.engine import *
from battery.battery import *

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        battery = NubbinBattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_on)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)