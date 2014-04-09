class FizzBuzzText():

	def fizz_text(self):
		return 'Fizz'

class FizzBuzzBodyMovementText():

	def fizz_text(self):
		return 'FizzAndTouchHead'

class FizzBuzz():
	
    feature_toggle_body_movement = False
 
    def create_text(self):
    	return FizzBuzzBodyMovementText() if self.feature_toggle_body_movement else FizzBuzzText()

    def count_off(self, n):
        if self.is_fizz(n) and self.is_buzz(n): 
        	return self.fizzbuzz_text()
        if self.is_fizz(n): 
        	return self.create_text().fizz_text()
        if self.is_buzz(n):
        	return self.buzz_text()
        return n

    def is_fizz(self, n):
    	return n % 3 == 0

    def is_buzz(self, n):
    	return n % 5 == 0

    def buzz_text(self):
    	if self.feature_toggle_body_movement:
    		return 'BuzzAndTouchShoulder'
    	else:
    		return 'Buzz'

    def fizzbuzz_text(self):
    	if self.feature_toggle_body_movement:
    		return 'FizzBuzzAndTouchKnee'
    	else:
    		return 'FizzBuzz'

