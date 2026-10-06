s = 'azcbobobegghakl'

longest = '' #com a string vazia a saída sempre será 0
current = ''

for i in s:
    # se a sequência atual está vazia ou a letra atual continua em ordem alfabética
    if not current or i >= current[-1]:
        current += i # adiciona a letra à sequência atual
    else:
        if len(current) > len(longest): # se a sequência quebrou, atualiza a maior substring
            longest = current
        current = i # reinicia a sequência atual com a letra que quebrou a sequência

# após o loop, pode ser que a última sequência seja a maior, então verifica novamente
if len(current) > len(longest):
    longest = current

print('A maior substring em ordem alfabética é: ', longest)
