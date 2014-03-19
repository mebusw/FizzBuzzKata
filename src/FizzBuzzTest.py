import unittest

class FizzBuzzTest(unittest.TestCase):

    def testCountOff(self):
        self.assertEquals(1, FizzBuzz().countOff(1))
        self.assertEquals(2, FizzBuzz().countOff(2))
        self.assertEquals('Fizz', FizzBuzz().countOff(3))





class FizzBuzz():
	def countOff(self, n):
		return n


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
