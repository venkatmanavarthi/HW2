import unittest
from problem2 import Obstacle


class TestProblem2(unittest.TestCase):

    def setUp(self) -> None:
        self.obs = Obstacle(4, 4, 0.25)

    def test_is_inside(self):
        self.assertEqual(self.obs.is_inside(2, 2), False)
        self.assertEqual(self.obs.is_inside(4, 4), True)

    def test_is_valid(self):
        pass
    
if __name__ == "__main__":
    unittest.main()
