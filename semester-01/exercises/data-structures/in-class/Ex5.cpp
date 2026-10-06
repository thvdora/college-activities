// Exercício 5: Verificação de matrícula ativa 

#include <iostream>
#include <string>
using namespace std;

int main() {
    string estudante;
        cout << "Qual o nome do estudante?";
        cin >> estudante;
    int matricula;
        cout << "Qual o número de matrícula?";
        cin >> matricula;
    bool estado;
        cout << "Matrícula está ativa? Digite 1 para Sim e 0 para Não:";
        cin >> estado;

    cout << "=== DADOS ACADÊMICOS ===" << endl;
    cout << "Nome: " << estudante << endl;
    cout << "Matrícula: " << matricula << endl;
    cout << "Ativa: ";
        if (estado)
            {
                cout << "Verdadeiro";
            } 
        else 
            {
                cout << "Falso";                
            }
}