x = float(input('Digite um numero: ')) #trabalha com float para suportar resultados não inteiros

# 2️⃣ Definir intervalo
low = 0.0
high = x

# 3️⃣ Definir tolerância
T = 0.01

# 4️⃣ Calcular primeiro chute (meio do intervalo
mid = (low + high) / 2

guesses = 0

# 6️⃣ Loop principal de bisection
while abs(mid**2 -x) >= T: #Enquanto o erro for maior ou igual que a tolerância
    guesses += 1
    if mid**2 < x: #Se o intervalo ao quadrado for menor que x, a raiz está pra direita
        low = mid
    else:
        high = mid #Se não, está para esquerda
    mid = (low + high) / 2

print("A raiz aproximada de", x, "é", mid)
print("Número de tentativas:", guesses)
