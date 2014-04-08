class FizzBuzz():
	
    feature_toggle_body_movement = False
    
    def count_off(self, n):
        if (self.is_fizz(n) and self.is_buzz(n)): 
        	return 'FizzBuzz'
        if (self.is_fizz(n)): 
        	return self.feature_toggle_body_movement and 'FizzAndTouchHead' or 'Fizz'
        if (self.is_buzz(n)):
        	return self.feature_toggle_body_movement and 'BuzzAndTouchShoulder' or 'Buzz'
        return n

    def is_fizz(self, n):
    	return n % 3 == 0

    def is_buzz(self, n):
    	return n % 5 == 0

