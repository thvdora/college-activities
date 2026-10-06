// 3.1 if e else

#include <iostream> 
#include <string>
using namespace std;

int main() {
    int numero;
    cout << "Digite um número: ";
    cin >> numero;

    if (numero >= 0) {
        cout << "O número é positivo.";
    }
    else {
        cout << "O número é negativo.";
    }
}