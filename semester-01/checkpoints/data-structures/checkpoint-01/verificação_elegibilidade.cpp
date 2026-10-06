#include <iostream> 
#include <string>
using namespace std;

int main() {
    int idade;
    cout << "Qual a sua idade? ";
    cin >> idade;

    if (idade < 16) {
        cout << "Voto não permitido.";
    }
    else if (idade <= 17) {
        cout << "Voto facultativo.";
    }
    else if (idade <= 69) {
        cout << "Voto obrigatório.";
    }
    else {
        cout << "Voto facultativo.";
    }
}