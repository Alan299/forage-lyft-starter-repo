from datetime import date

from battery.battery import  SpindlerBattery
from battery.battery import NubbinBattery

def test_spindler():
    current_date =date.fromisoformat("2022-01-06") 
    last_service_date = date.fromisoformat("2020-01-01")
    battery = SpindlerBattery(last_service_date=last_service_date,
        current_date= current_date)

    assert battery.needs_service() == True, 'True test failed ' + test_spindler.__name__

    current_date =date.fromisoformat("2021-12-31") 
    last_service_date = date.fromisoformat("2020-01-01")
    battery = SpindlerBattery(last_service_date=last_service_date,
        current_date= current_date)

    assert battery.needs_service() == False, 'False test failed ' + test_spindler.__name__


def test_nubbin():
    current_date =date.fromisoformat("2022-01-06") 
    last_service_date = date.fromisoformat("2018-01-01")
    battery = NubbinBattery(last_service_date=last_service_date,
        current_date= current_date)

    assert battery.needs_service() == True, 'True test failed ' + test_nubbin.__name__

    current_date =date.fromisoformat("2022-01-01") 
    last_service_date = date.fromisoformat("2019-01-01")
    battery = NubbinBattery(last_service_date=last_service_date,
        current_date= current_date)

    assert battery.needs_service() == False, 'False test failed ' + test_nubbin.__name__

if __name__ ==  "__main__":
    print("Spindler Tests")
    test_spindler()

    print("Nubbin Tests")
    test_nubbin()

    print()
    print("All tests passed.")
    print("SUCCESS")

