class FizzBuzz():
	
    feature_toggle_body_movement = False
    
    def count_off(self, n):
        if self.is_fizz(n) and self.is_buzz(n): 
        	if self.feature_toggle_body_movement:
        		return 'FizzBuzzAndTouchKnee'
        	else:
        		return 'FizzBuzz'
        if self.is_fizz(n): 
        	return self.fizz_text()
        if self.is_buzz(n):
        	return self.buzz_text()
        return n

    def is_fizz(self, n):
    	return n % 3 == 0

    def is_buzz(self, n):
    	return n % 5 == 0

    def fizz_text(self):
    	if self.feature_toggle_body_movement:
    		return 'FizzAndTouchHead'
    	else:
    		return 'Fizz'

    def buzz_text(self):
    	if self.feature_toggle_body_movement:
    		return 'BuzzAndTouchShoulder'
    	else:
    		return 'Buzz'