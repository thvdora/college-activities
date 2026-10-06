// código feito pelo professor - if/else "indireto"

#include <iostream>
using namespace std;

int main(){
    int idade;
    bool acesso = false;

    cout<<"             BALADINHA               " << "\n\n" ;
    cout<<"SÓ PERMITIRMOS MAIORES DE IDADE AQUI!!! " << "\n\n" ;

    cout << "Digite sua idade: ";
    cin >> idade;

    if (idade >= 18){
        acesso = true;
    }

    if (acesso == true){
        cout << "Destrancar";
    }else {
        cout << "Trancar";
    }

    return 0;
}