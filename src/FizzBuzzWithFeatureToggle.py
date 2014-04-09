class FizzBuzzText():

	def fizz_text(self):
		return 'Fizz'

	def buzz_text(self):
		return 'Buzz'

class FizzBuzzBodyMovementText():

	def fizz_text(self):
		return 'FizzAndTouchHead'

	def buzz_text(self):
		return 'BuzzAndTouchShoulder'

class FizzBuzz():
	
    feature_toggle_body_movement = False
 
    def create_text(self):
    	return FizzBuzzBodyMovementText() if self.feature_toggle_body_movement else FizzBuzzText()

    def count_off(self, n):
    	text = self.create_text()

        if self.is_fizz(n) and self.is_buzz(n): 
        	return self.fizzbuzz_text()
        if self.is_fizz(n): 
        	return text.fizz_text()
        if self.is_buzz(n):
        	return text.buzz_text()
        return n

    def is_fizz(self, n):
    	return n % 3 == 0

    def is_buzz(self, n):
    	return n % 5 == 0

    def fizzbuzz_text(self):
    	if self.feature_toggle_body_movement:
    		return 'FizzBuzzAndTouchKnee'
    	else:
    		return 'FizzBuzz'

