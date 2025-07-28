from src import romanNumeral, entierNumeral

def test_romanNumeral():
    assert romanNumeral(1) == "I"
    assert romanNumeral(10) == "X"
    assert romanNumeral(7) == "VII"

    assert entierNumeral("I") == 1
    assert entierNumeral("X") == 10
    assert entierNumeral("VII") == 7