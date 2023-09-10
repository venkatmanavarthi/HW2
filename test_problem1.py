import unittest
import problem1


class TestProblem1(unittest.TestCase):

    def test_calculate_distance(self):
        self.assertEqual(problem1.calculate_distance(2, 1, 3, 2), 1.41)
        self.assertEqual(problem1.calculate_distance(1, 1, 6, 1), 5)
        self.assertEqual(problem1.calculate_distance(1, 1, 2, 8), 7.07)


if __name__ == "__main__":
    unittest.main()
