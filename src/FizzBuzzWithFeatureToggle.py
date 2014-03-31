class FizzBuzz():
	
    featureToggleBodyMovement = False
    
    def countOff(self, n):
        if (n % 3 == 0): return FizzBuzz.featureToggleBodyMovement and 'FizzAndTouchHead' or 'Fizz'
        return n