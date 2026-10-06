#include <iostream> 
#include <string>
using namespace std;

int main() {
    double valorOriginal;
    double valorDoDesconto;
    double valorFinal;
    double desconto = 0.10;
    
    cout << "Valor de compra: R$ ";
    cin >> valorOriginal;

    if (valorOriginal > 200) {
        valorDoDesconto = valorOriginal * 0.10;
    }
    else {
        valorDoDesconto = 0;
        cout << "Valor não aplicável para descontos" << endl;
    }
    valorFinal = valorOriginal - valorDoDesconto;

    cout << "Desconto aplicado: R$ " << valorDoDesconto << endl;
    cout << "Valor final: R$ " << valorFinal << endl;
}