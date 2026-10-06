// 4.0 bool

#include <iostream> 
#include <string>
using namespace std;

int main() {
    string produto;
    cout << "Nome do produto: ";
    cin >> produto;

    bool disponivel;
    cout << "O produto está disponível em estoque? 1 = Sim e 0 = Não.";
    cin >> disponivel;

    cout << "Status: ";
        if (disponivel) {
            cout << "Disponível";
        }
        else {
            cout << "Indisponível";
        }
}