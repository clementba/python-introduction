def fizzbuzz(number: int) -> str:
    if(number % 3 == 0 & number % 5 == 0):
        return "FizzBuzz"
    if(number % 3):
        return "Fizz"
    if '3' in str(number):
        return "Fizz"

    if(number % 5 == 0):
        return "Buzz"
    if '5' in str(number):
        return "Buzz"
    return str(number)