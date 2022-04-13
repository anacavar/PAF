// Napišite C++ program u kojem korsnik definira polje cjelih brojeva. Ispišite sve članove polja koju se nalaze
// u intervalu [a, b]. Neka korisniku budu dostupne funkcije za okretanje redosljeda članova polja, zamjenu
// mjesta dva člana polja i sortiranje članova po veličini.

#include <iostream>

void clanovi_polja_unutar_intervala(int a, int b, int polje[], int N){
    for (int i = 0; i < N; i++) {
        if(polje[i]>=a && polje[i]<=b){
            std::cout << std::to_string(polje[i]) << std::endl; 
        }
    }
}

void okreni_redosljed(int polje[], int N){
    int polje2[N];
    for(int i = 0; i<N; i++){
        polje2[i] = polje[N-i-1];
    }
    for(int i = 0; i<N; i++){
        polje[i] = polje2[i];
    }
}

void zamjeni_clanove(int polje[], int N, int index1, int index2){

    int clan1;
    int clan2;

    for(int i = 0; i<N; i++) {
        if(i == index1) {
            clan1 = polje[i];
        } else if (i == index2){
            clan2 = polje[i];
        }
    }

    for(int i = 0; i<N; i++){
        if(i == index1) {
            polje[i] = clan2;
        } else if (i == index2){
            polje[i] = clan1;
        }
    }
}

int main(){
    int a = 1;
    int b = 10;
    int N = 6;
    int polje[N] = {5, 1, 23, 6, 0, 79};

    okreni_redosljed(polje, N);
    zamjeni_clanove(polje, N, 3, 5);
    clanovi_polja_unutar_intervala(a, b, polje, N);

    return 0;
}