# CP01 - Modelagem Matemática Computacional

## Aula 02 - Octave/Scilab e R

### Parte A - Matriz 3x3

Matriz original: `A = [1 2 3; 0 1 0; 3 2 1]`

Determinante calculado pela regra de Sarrus:

```text
det(A) = 1 - 9 = -8
```

Como o determinante é diferente de zero, a matriz possui inversa.

### Parte B - Função quadrática

```text
y = x^2 - 4x + 2
```

Intervalo: `x = -2` até `x = 6`.

Para `x = -2`:

```text
y = (-2)^2 - 4(-2) + 2 = 14
```

### Parte C - Vetor aleatório

```text
x = randi(100, 1, 100)
soma = sum(x)
media = soma / 100
```

## Aula 03 - Funções de diferentes graus

### Parte A - 1º grau

```text
y = 70 + 5x
```

### Parte B - 2º grau

```text
h(t) = -5t^2 + 20t + 2
```

### Parte C - Funções de graus superiores

```text
f(x) = ax^3 + bx^2 + cx + d
```

```text
f(x) = -x^3 + 15x^2 + 5
```

Coeficientes:
- `a = -1`
- `b = 15`
- `c = 0`
- `d = 5`
