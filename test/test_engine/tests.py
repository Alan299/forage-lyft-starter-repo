import unittest
from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine

class TestEngine(unittest.TestCase):
    def test_capulet(self):
        current_mileage = 40000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(engine.needs_service())

        current_mileage = 30000-1
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughby(self):
        current_mileage = 60100
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertTrue(engine.needs_service())

        current_mileage = 60000-1
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

if __name__ == "__main__":
    unittest.main()
