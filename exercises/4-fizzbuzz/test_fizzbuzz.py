from src import fizzbuzz

def test_fizzbuzz():
     assert fizzbuzz(1) == '1'
     assert fizzbuzz(2) == '2'
     assert fizzbuzz(3) == 'Fizz'
     assert fizzbuzz(4) == '4'
     assert fizzbuzz(5) == 'Buzz'