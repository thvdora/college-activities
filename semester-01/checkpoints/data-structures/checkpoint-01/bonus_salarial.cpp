#include <iostream> 
#include <string>
using namespace std;

int main() {
    string nome;
    double salarioAtual;
    float notaDeDesempenho;
    double bonusPercentual;
    double valorDoBonus;
    double salarioNovo;

    cout << "Nome do funcionário: ";
    getline(cin, nome);
    
    cout << "Salário atual: ";
    cin >> salarioAtual;

    cout << "Nota de desempenho: ";
    cin >> notaDeDesempenho;

    if (notaDeDesempenho >= 9 && notaDeDesempenho <= 10) {
        bonusPercentual = 0.15;
    }
    else if (notaDeDesempenho >= 7 && notaDeDesempenho <= 8.99) {
        bonusPercentual = 0.10;
    }
    else if (notaDeDesempenho >= 5 && notaDeDesempenho <= 6.99) {
        bonusPercentual = 0.05;
    }
    else {
        bonusPercentual = 0;
    }

    valorDoBonus = salarioAtual * bonusPercentual;
    salarioNovo = salarioAtual + valorDoBonus;
    
    cout << "\n--- Sistema de bônus salarial ---\n";
    cout << "Nome do funcionário: " << nome << endl;
    cout << "Salário atual: R$ " << salarioAtual << endl;
    cout << "Bônus percentual: " << bonusPercentual * 100 << "%" << endl;
    cout << "Valor do bônus: R$ " << valorDoBonus << endl;
    if (bonusPercentual == 0) {
        cout << "Não houve alterações no salário." << endl;
    }
    else {
        cout << "Novo salário: R$ " << salarioNovo << endl;
    }

    return 0;
}