class FizzBuzz():
	
    featureToggleBodyMovement = False
    
    def countOff(self, n):
        if (self.isFizz(n) and self.isBuzz(n)): 
        	return 'FizzBuzz'
        if (self.isFizz(n)): 
        	return self.featureToggleBodyMovement and 'FizzAndTouchHead' or 'Fizz'
        if (self.isBuzz(n)):
        	return self.featureToggleBodyMovement and 'BuzzAndTouchShoulder' or 'Buzz'
        return n

    def isFizz(self, n):
    	return n % 3 == 0

    def isBuzz(self, n):
    	return n % 5 == 0