// 1.1 Cadastro de jogador

#include <iostream>
#include <string>
using namespace std;

int main() {
string jogador;
cout << "Digite seu nome: ";
getline(cin, jogador);

int idade;
cout << "Digite a sua idade: ";
cin >> idade;

char rank;
cout << "Rank: ";
cin >> rank;

cout << "====JOGADOR====" << endl;
cout << "Nome: " << jogador << endl;
cout << "Idade: " << idade << endl;
cout << "Seu rank: " << rank << endl;
}