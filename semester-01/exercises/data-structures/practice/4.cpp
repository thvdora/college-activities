// 3.0 if e else

#include <iostream> 
#include <string>
using namespace std;

int main() {
    int idade;
    cout << "Qual a sua idade? ";
    cin >> idade;
    bool acesso;

    if (idade >= 18) {
        cout << "Pode dirigir.";
    }
    else {
        cout << "Não pode dirigir.";
    }
}