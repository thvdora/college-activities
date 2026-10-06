def isIn(char, aStr):
    if aStr == '':        #se a string procurada for vazia já para de procurar
        return False

    middle_index = len(aStr) // 2        #pega o INDICE do meio
    middle_char = aStr[middle_index]     #pega o CHAR do meio
    if middle_char == char:
        return True
    elif char < middle_char:
        return isIn(char, aStr[:middle_index])
    else:
        return isIn(char, aStr[middle_index + 1:])
