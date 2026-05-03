import unittest

class TestSimulation(unittest.TestCase):

    def test_single_car(self):
        field = Field(10, 10)
        car = Car("A", 1, 2, "N", "FFRFFFFRRL")

        sim = Simulator(field, [car])
        result = sim.simulate()[0]

        self.assertEqual((result.x, result.y, result.direction), (5, 4, "S"))

    def test_collision(self):
        field = Field(10, 10)

        car_a = Car("A", 1, 2, "N", "FFRFFFFRRL")
        car_b = Car("B", 7, 8, "W", "FFLFFFFFFF")

        sim = Simulator(field, [car_a, car_b])
        results = sim.simulate()

        self.assertTrue(results[0].collision is not None)
        self.assertTrue(results[1].collision is not None)


if __name__ == "__main__":
    unittest.main()
