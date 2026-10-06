#Função McNuggets(n):
#    Se n <= 0:
#    Retorna False

#Para a de 0 até n dividido por 6:
#    Para b de 0 até n dividido por 9:
#        resto = n - (6 * a + 9 * b)

#        Se resto >= 0 E resto módulo 20 igual a 0:
#            Retorna True

def McNuggets(n):
    if n <= 0:
        return False

    for a in range(0, n // 6 + 1):
        for b in range(0, n // 9 + 1):
            rest = n - (6 * a + 9 * b)
            if rest >= 0 and rest % 20 == 0:
                return True
    return False
print(McNuggets(15))
print(McNuggets(16))
print(McNuggets(17))