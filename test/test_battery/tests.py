import unittest
from datetime import date
from battery.battery import SpindlerBattery, NubbinBattery

class TestBattery(unittest.TestCase):
    def test_spindler(self):
        current_date = date.fromisoformat("2022-01-06")
        last_service_date = date.fromisoformat("2020-01-01")
        battery = SpindlerBattery(last_service_date=last_service_date,
                                  current_date=current_date)

        self.assertTrue(battery.needs_service())

        current_date = date.fromisoformat("2021-12-31")
        last_service_date = date.fromisoformat("2020-01-01")
        battery = SpindlerBattery(last_service_date=last_service_date,
                                  current_date=current_date)

        self.assertFalse(battery.needs_service())

    def test_nubbin(self):
        current_date = date.fromisoformat("2022-01-06")
        last_service_date = date.fromisoformat("2018-01-01")
        battery = NubbinBattery(last_service_date=last_service_date,
                                current_date=current_date)

        self.assertTrue(battery.needs_service())

        current_date = date.fromisoformat("2022-01-01")
        last_service_date = date.fromisoformat("2019-01-01")
        battery = NubbinBattery(last_service_date=last_service_date,
                                current_date=current_date)

        self.assertFalse(battery.needs_service())

if __name__ == "__main__":
    unittest.main()
