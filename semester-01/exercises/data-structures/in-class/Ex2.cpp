//   Exercício 2: Cálculo da idade futura 

#include <iostream>
using namespace std;

int main() {
    int idadeAtual;
    int anos;
        cout << "Qual a sua idade atual?";
        cin >> idadeAtual;

        cout << "Quantos anos deseja avançar?";
        cin >> anos;

    int idadeFutura;
    idadeFutura = idadeAtual + anos;
        cout << "Daqui a " << anos << " anos " << "você terá " << idadeFutura << " anos.";
}