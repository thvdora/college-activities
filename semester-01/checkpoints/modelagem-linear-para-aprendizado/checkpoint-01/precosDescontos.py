precos = [15.50, 20.00, 3.25, 50.00, 10.75]

def calcular_total_com_desconto(precos, desconto): 
    total = 0

    for preco in precos:
        preco_com_desconto = preco - (preco * desconto)
        total += preco_com_desconto

    return total

total_final = calcular_total_com_desconto(precos, 0.20)

print(f"Total com 20% de desconto: R$ {total_final:.2f}")
