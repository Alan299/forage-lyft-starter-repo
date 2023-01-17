import unittest
from tire.tire import CarriganTire,OctoprimeTire

class TestTire(unittest.TestCase):
    def test_carrigan(self):
        
        percentage_used = [0,0.9,0,0]
        tire = CarriganTire(percentage_used)
        self.assertTrue(tire.needs_service() )

        percentage_used = [0,0.89,0.8,0.899]
        tire = CarriganTire(percentage_used)
        self.assertFalse(tire.needs_service())
    

    def test_octoprime(self):
        
        percentage_used = [1,1,0.5,0.5]
        tire = OctoprimeTire(percentage_used)
        self.assertTrue(tire.needs_service() )

        percentage_used = [1,1,0.5,0.49]
        tire = OctoprimeTire(percentage_used)
        self.assertFalse(tire.needs_service())
    
if __name__ == "__main__":
    unittest.main()