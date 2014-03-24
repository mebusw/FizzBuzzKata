import unittest


class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def testCountOff(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))
        self.assertEqual('Fizz', FizzBuzz().countOff(3))


class FizzBuzz():
    def countOff(self, n):
        return n


if __name__ == "__main__":
    unittest.main()
