import ft

class FizzBuzz():
    def countOff(self, n):
        if not ft.featureToggle:
            if (n == 3):
                return 'Fizz'
        return n