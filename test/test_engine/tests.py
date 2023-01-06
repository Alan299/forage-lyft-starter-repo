from engine.engine import CapuletEngine
from engine.engine import WilloughbyEngine
from engine.engine import SternmanEngine



def test_capulet():

    current_mileage = 40000
    last_service_mileage = 0

    engine = CapuletEngine(last_service_mileage= last_service_mileage, current_mileage= current_mileage)
    
    assert engine.needs_service() == True, 'True test failed'

    current_mileage = 30000-1
    last_service_mileage = 0

    engine = CapuletEngine(last_service_mileage= last_service_mileage, current_mileage= current_mileage)


    assert engine.needs_service() == False, 'False test failed'

def test_willoughby():
    current_mileage = 60100
    last_service_mileage = 0

    engine = WilloughbyEngine(last_service_mileage= last_service_mileage, current_mileage= current_mileage)
    
    assert engine.needs_service() == True, 'True test failed'

    current_mileage = 60000
    last_service_mileage = 0

    engine = WilloughbyEngine(last_service_mileage= last_service_mileage, current_mileage= current_mileage)


    assert engine.needs_service() == False, 'False test failed'

def test_sternman():
    warning_light_is_on = True

    engine = SternmanEngine(warning_light_is_on)
    
    assert engine.needs_service() == True, 'True test failed'

    warning_light_is_on = False

    engine = SternmanEngine(warning_light_is_on)


    assert engine.needs_service() == False, 'False test failed'


if __name__ ==  "__main__":
    print("Capulet  Tests")
    test_capulet()

    print("Willoughby  Tests")
    test_capulet()

    print("Sternman Tests")
    test_capulet()

    print("All tests passed.")
    print("SUCCESS")


