#include <iostream> 
#include <string>
using namespace std;

int main() {
    string aluno;
    cout << "Nome do aluno: ";
    getline(cin, aluno);

    float nota;
    cout << "Nota: ";
    cin >> nota;

    if (nota >= 6) {
        cout << "Aprovado!";
    }
    else {
        cout << "Reprovado.";
    }
    return 0;
}