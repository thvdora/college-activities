# CP02 - Modelagem Matematica Computacional

## Parte A - Descontinuidade removivel

Funcao: f(x) = (x^2 - 9) / (x - 3)

A fatoracao usada no trabalho e x^2 - 9 = (x - 3)(x + 3). Assim, o limite em x -> 3 e igual a 6.

Em x = 3, a funcao original nao esta definida, pois ocorre 0/0. Portanto, ha uma descontinuidade removivel (buraco) em x = 3, embora o limite exista e seja igual a 6.

## Parte B - Descontinuidade infinita

Funcao: g(x) = 1 / (50 - x)

O trabalho testa valores de x cada vez mais proximos de 50 pelo lado esquerdo e conclui que o limite tende a +infinito.

Interpretacao registrada no PDF: no modelo, o custo cresce sem limites conforme o numero de usuarios se aproxima de 50. Na pratica, o servidor possui limitacoes fisicas e financeiras e pode apresentar lentidao, recusar conexoes ou parar de funcionar antes de um custo real se tornar infinito.

## Parte C - Descontinuidade por salto

Funcao por partes:

h(x) = 100, para x < 10
h(x) = 150, para x >= 10

Limites laterais:
- lim x->10- h(x) = 100
- lim x->10+ h(x) = 150

Como os limites laterais sao diferentes, o limite em x = 10 nao existe. Portanto, a funcao e descontinua por salto nesse ponto.

### Tres condicoes de continuidade analisadas

1. A funcao esta definida no ponto: h(10) = 150.
2. O limite no ponto deveria existir, mas os limites laterais sao diferentes.
3. O limite deveria ser igual ao valor da funcao, porem o limite nao existe.

A estrutura deste README segue a ordem Parte A, Parte B e Parte C do documento original.
