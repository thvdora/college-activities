// 1.0 Variáveis + cin + cout

#include <iostream> 
#include <string>
using namespace std;

int main() {
string filme;
cout << "Digite o nome do filme: ";
getline(cin, filme); // Para receber nomes compostos e o programa não pular assim que percorrer um espaço em branco, use getline.

int lancamento;
cout << "Qual o ano de lançamento do filme?";
cin >> lancamento;

float nota;
cout << "Que nota você daria para ele?";
cin >> nota;

cout << "=== FILME ===" << endl;
cout << "Nome: " << filme << endl;
cout << "Ano: " << lancamento << endl;
cout << "Nota: " << nota << endl;
}