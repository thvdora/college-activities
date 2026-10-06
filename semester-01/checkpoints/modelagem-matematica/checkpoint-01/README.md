# CP01 - Modelagem Matemática Computacional

## Estrutura original

O material foi organizado seguindo a mesma sequência do PDF.

### Aula 02 - Octave/Scilab e R

#### Parte A - Matriz 3x3
- Matriz original: `A = [1 2 3; 0 1 0; 3 2 1]`
- Cálculo da transposta
- Determinante calculado manualmente pela regra de Sarrus: `det(A) = -8`
- Como o determinante é diferente de zero, a matriz possui inversa.
- O código correspondente está em `aula-02/parte-a_matriz.m`.

#### Parte B - Função quadrática
Função estudada:

```text
y = x^2 - 4x + 2
```

Intervalo utilizado: `x = -2` até `x = 6`.

No cálculo manual apresentado no trabalho, para `x = -2`:

```text
y = (-2)^2 - 4(-2) + 2 = 14
```

O código e a geração do gráfico estão em `aula-02/parte-b_funcao-quadratica.m`.

#### Parte C - Vetor aleatório
- Geração de 100 números aleatórios com `randi(100, 1, 100)`
- Soma dos valores com `sum(x)`
- Média calculada dividindo a soma por 100
- O PDF também apresenta um resultado de terminal usando `rand(1, 100)`.

Código em `aula-02/parte-c_vetor-aleatorio.m`.

---

### Aula 03 - Funções de diferentes graus

#### Parte A - Função de 1º grau
Modelo de valorização de um imóvel:

```text
y = 70 + 5x
```

O código gera o gráfico para `x = 0` até `10`.

Código em `aula-03/parte-a_primeiro-grau.m`.

#### Parte B - Função de 2º grau
Função estudada:

```text
h(t) = -5t^2 + 20t + 2
```

Na resolução manual, a parábola tem concavidade voltada para baixo e o vértice foi calculado em `(2, 22)`.

Código em `aula-03/parte-b_segundo-grau.m`.

#### Parte C - Função de 3º grau
Forma geral apresentada:

```text
f(x) = ax^3 + bx^2 + cx + d
```

Função analisada:

```text
f(x) = -x^3 + 15x^2 + 5
```

Coeficientes:
- `a = -1`
- `b = 15`
- `c = 0`
- `d = 5`

Código em `aula-03/parte-c_terceiro-grau.m`.

> Os arquivos de código foram separados para facilitar a consulta no GitHub, mas a ordem e a divisão em aulas/partes seguem o documento original.
