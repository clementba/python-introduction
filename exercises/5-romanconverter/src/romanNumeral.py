def romanNumeral(number):
    valeurs_romaines = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    resultat = ''

    for valeur, symbole in valeurs_romaines:
        while number >= valeur:
            resultat += symbole
            number -= valeur
    return resultat


def entierNumeral(number):
    valeurs_romaines = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    precedent = 0
    for symbole_romain in reversed(number):
        valeur = valeurs_romaines[symbole_romain]
        if valeur < precedent:
            total -= valeur
        else:
            total += valeur
            precedent = valeur
    return total