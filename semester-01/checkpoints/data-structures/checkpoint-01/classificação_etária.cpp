#include <iostream> 
#include <string>
using namespace std;

int main() {
    int idade;
    cout << "Digite sua idade: ";
    cin >> idade;

    if (idade <= 12) {
        cout << "Classificação etária: criança." << endl;
    }
    else if (idade <= 17) {
        cout << "Classificação etária: adolescente." << endl;
    }
    else {
        cout << "Classificação etária: adulto." << endl;
    }
}