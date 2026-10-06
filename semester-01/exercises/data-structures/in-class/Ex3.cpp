// Exercício 3: informações de um produto 

#include <iostream>
using namespace std;

int main() {
    string produto;
        cout << "Nome do produto: ";
        cin >> produto;
    double valorUn;
        cout << "Qual o preço unitário do produto? ";
        cin >> valorUn;
    int quantidade;
        cout << "Qual a quantidade em estoque? ";
        cin >> quantidade;

    cout << "=== PRODUTO CADASTRADO ===" << endl;
    cout << "Produto: " << produto << endl;
    cout << "Preço: R$ " << valorUn << endl;
    cout << "Estoque: " << quantidade << endl;
}