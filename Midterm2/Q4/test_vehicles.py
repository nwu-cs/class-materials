import unittest

from vehicles import Vehicle,Car,Convertible,MotorCycle,PedalBike,Pickup,Bike,Bus


class TestVehicles(unittest.TestCase):

    def test_sorting_same_types(self):
        a = MotorCycle("motorcycle1",2,6,1,3)
        e = MotorCycle("motorcycle2",2,5,1,3)
        # a is greater than e by volume
        self.assertTrue(a > e)

    def test_sorting_different_types(self):
        a = MotorCycle("motorcycle1",2,6,1,3)
        b = Bus("bus1",4,20,12,10)
        c = Convertible("mini1",4,10,7,5)
        d = PedalBike("pedalbike1",2,5,1,3)
        e = MotorCycle("motorcycle2",2,5,1,3)
        f = Pickup("pickup1",4,12,10,6)

        # make a list of vehicles
        y = [a, b, c, d, e, f]
        # presorted list by volume
        z = [d, e, a, c, f, b]
        print(y)
        y.sort()
        print(y)
        self.assertTrue(y == z)

if __name__ == '__main__':
    unittest.main()
