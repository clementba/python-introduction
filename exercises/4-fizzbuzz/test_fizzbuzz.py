from src import fizzbuzz

def test_fizzbuzz():
     assert fizzbuzz(1) == '1'
     assert fizzbuzz(2) == '2'
     assert fizzbuzz(3) == 'Fizz'


def test_buzz():
     assert fizzbuzz(4) == '4'
     assert fizzbuzz(5) == 'Buzz'

def test_fizz_buz():
     assert fizzbuzz(15) == 'FizzBuzz'

def test_etape2():
     assert fizzbuzz(15) == 'FizzBuzz'

def test_compute():
     for number in range(1, 101):
          resultat = fizzbuzz(number)
          print(f"{number} => {resultat}")