class FizzBuzzText():

    def fizz_text(self):
        return 'Fizz'

    def buzz_text(self):
        return 'Buzz'

    def fizzbuzz_text(self):
        return 'FizzBuzz'

class FizzBuzzBodyMovementText():

    def fizz_text(self):
        return 'FizzAndTouchHead'

    def buzz_text(self):
        return 'BuzzAndTouchShoulder'

    def fizzbuzz_text(self):
        return 'FizzBuzzAndTouchKnee'

class FizzBuzz():
    
    feature_toggle_body_movement = False
 
    def create_text_generator(self):
        return FizzBuzzBodyMovementText() if self.feature_toggle_body_movement else FizzBuzzText()

    def count_off(self, n):
        text_generator = self.create_text_generator()

        if self.is_fizz(n) and self.is_buzz(n): 
            return text_generator.fizzbuzz_text()
        if self.is_fizz(n): 
            return text_generator.fizz_text()
        if self.is_buzz(n):
            return text_generator.buzz_text()
        return n

    def is_fizz(self, n):
        return n % 3 == 0

    def is_buzz(self, n):
        return n % 5 == 0
