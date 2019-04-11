class Calculator:
    def add(self, numbers):
        if numbers == '':
            return 0
        elif numbers.find(',') != -1:
            digits = numbers.split(",")
            accumulator = 0
            for digit in digits:
                accumulator += int(digit)
            return accumulator
        else:
            return int(numbers)
