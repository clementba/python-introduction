from src import romanNumeral

def test_romanNumeral():
    assert romanNumeral(1) == "I"
    assert romanNumeral(10) == "X"
    assert romanNumeral(7) == "VII"