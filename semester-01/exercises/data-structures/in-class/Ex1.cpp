// Exercício 1: Cadastro de um aluno 

#include <iostream>
using namespace std;

int main() {
string nome; 
    cout << "Digite seu nome:";
    cin >> nome;

int idade;
    cout << "Qual a sua idade?";
    cin >> idade;

double altura;
    cout << "Qual a sua altura?";
    cin >> altura;

    cout << "=== DADOS DO ALUNO ===" << endl;
    cout << "Nome: " << nome << endl;
    cout << "Idade: " << idade << endl;
    cout << "Altura: " << altura << endl; 
}