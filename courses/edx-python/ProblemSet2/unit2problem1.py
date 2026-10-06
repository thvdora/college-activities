taxa_mensal = taxa_anual / 12.0

for mes in range(12):
    pagamentoMinimo = taxaPagamentoMensal * saldo
    naoPago = saldo - pagamentoMinimo
    saldo = naoPago + (taxa_mensal * naoPago)

print("Saldo restante:", round(saldo, 2))