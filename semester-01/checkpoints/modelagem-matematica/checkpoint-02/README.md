# CP02 - Modelagem Matemática Computacional

## Parte A

```text
f(x) = (x^2 - 9) / (x - 3)
```

```text
x^2 - 9 = (x - 3)(x + 3)
lim x->3 (x + 3) = 6
```

A função apresenta uma descontinuidade removível (buraco) em `x = 3`, pois não está definida nesse ponto, embora o limite exista e seja igual a 6.

## Parte B

```text
g(x) = 1 / (50 - x)
```

```text
lim x->50- g(x) = +∞
```

Na prática, o servidor possui limitações físicas e financeiras. Antes que o custo se torne infinito, ele pode ficar sobrecarregado, apresentar lentidão, recusar novas conexões ou até parar de funcionar.

Portanto, o resultado `+∞` indica que o custo aumenta sem limites no modelo à medida que o número de usuários se aproxima de 50, mas não significa que o custo real chegará ao infinito.

## Parte C

```text
h(x) = 100, x < 10
h(x) = 150, x >= 10
```

```text
lim x->10- h(x) = 100
lim x->10+ h(x) = 150
```

O limite em `x = 10` não existe pois os limites laterais não são os mesmos. Portanto, a função é descontínua por salto nesse ponto.

### Três condições de continuidade

1. A função deve estar definida no ponto: `h(10) = 150`.
2. O limite no ponto deve existir: `lim x->10- h(x) = 100` e `lim x->10+ h(x) = 150`.
3. O limite deve ser igual ao valor da função, porém o limite não existe.
