from src import romanNumeral, entierNumeral

def test_romanNumeral_unite():
    assert romanNumeral(1) == "I"
    assert romanNumeral(2) == "II"
    assert romanNumeral(3) == "III"
    assert romanNumeral(4) == "IV"
    assert romanNumeral(5) == "V"
    assert romanNumeral(6) == "VI"
    assert romanNumeral(7) == "VII"
    assert romanNumeral(8) == "VIII"
    assert romanNumeral(9) == "IX"
    assert romanNumeral(10) == "X"

def test_romanNumeral_dizaine():
    assert romanNumeral(20) == "XX"
    assert romanNumeral(10) == "X"
    assert romanNumeral(30) == "XXX"
    assert romanNumeral(34) == "XXXIV"
    assert romanNumeral(48) == "XLVIII"

def test_romanNumeral_centaine():
    assert romanNumeral(100) == "C"
    assert romanNumeral(200) == "CC"
    assert romanNumeral(300) == "CCC"
    assert romanNumeral(400) == "CD"
    assert romanNumeral(500) == "D"
    assert romanNumeral(600) == "DC"
    assert romanNumeral(700) == "DCC"
    assert romanNumeral(800) == "DCCC"
    assert romanNumeral(900) == "CM"
    assert romanNumeral(1000) == "M"

    assert romanNumeral(155) == "CLV"
    assert romanNumeral(478) == "CDLXXVIII"
    assert romanNumeral(752) == "DCCLII"


def test_entierNumeral_unite():
    assert entierNumeral("I") == 1
    assert entierNumeral("I") == 1
    assert entierNumeral("II") == 2
    assert entierNumeral("III") == 3
    assert entierNumeral("IV") == 4
    assert entierNumeral("V") == 5
    assert entierNumeral("VI") == 6
    assert entierNumeral("VII") == 7
    assert entierNumeral("VIII") == 8
    assert entierNumeral("IX") == 9
    assert entierNumeral("X") == 10

def test_entierNumeral_dizaine():
    assert entierNumeral("XX") == 20
    assert entierNumeral("X") == 10
    assert entierNumeral("XXX") == 30
    assert entierNumeral("XXXIV") == 34
    assert entierNumeral("XLVIII") == 48


def test_entierNumeral_centaine():
    assert entierNumeral("C") == 100
    assert entierNumeral("CC") == 200
    assert entierNumeral("CCC") == 300
    assert entierNumeral("CD") == 400
    assert entierNumeral("D") == 500
    assert entierNumeral("DC") == 600
    assert entierNumeral("DCC") == 700
    assert entierNumeral("DCCC") == 800
    assert entierNumeral("CM") == 900
    assert entierNumeral("M") == 1000

    assert entierNumeral("CLV") == 155
    assert entierNumeral("CDLXXVIII") == 478
    assert entierNumeral("DCCLII") == 752
