// Exercício 4: Características de um veículo 

#include <iostream>
using namespace std;

int main() {
    string marca;
        cout << "Qual a marca do veículo?";
        cin >> marca;
    int ano;
        cout << "Qual o ano de fabricação?";
        cin >> ano;
    char categoria;
        cout << "Qual a categoria de habilitação?";
        cin >> categoria;

    cout << "=== VEÍCULO ===" << endl;
    cout << "Marca: " << marca << endl;
    cout << "Ano: " << ano << endl;
    cout << "Categoria: " << categoria << endl;
}