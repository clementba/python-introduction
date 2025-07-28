#write code here
def score(sequence):
    # permet de convertir les lancer en valeur numérique
    lancers = []
    i = 0
    while i < len(sequence):
        char = sequence[i]
        if char == 'X':  # strike, ajout de 10 quilles
            lancers.append(10)
            i += 1
        elif char == '/':  # spare, ajout des quille jusqu'a 10
            lancers.append(10 - lancers[-1])
            i += 1
        elif char == '-':  # raté, aucune quille
            lancers.append(0)
            i += 1
        else: # nombre de quille tombé hors spare ou strike, on rajoute a la liste
            lancers.append(int(char))
            i += 1

    score = 0
    index = 0

    # les 10 frames
    for frame in range(10):
        if lancers[index] == 10:  # strike
            # score +10 + total des 2 lancer suivantes
            score += 10 + lancers[index + 1] + lancers[index + 2]
            index += 1
        elif lancers[index] + lancers[index + 1] == 10:  # spare
            score += 10 + lancers[index + 2]
            index += 2
        else: # lancer normal
            score += lancers[index] + lancers[index + 1]
            index += 2

    return score