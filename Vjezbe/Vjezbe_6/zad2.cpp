// Napišite C++ program u koji sadrži funkciju koja kao ulazne parametre prima (x, y) koordinate ishodišta
// kružnice, njezin radijus i koordinate neke točke. Funkcija vraća informaciju o tome da li se točka nalazi
// unutar kružnice.

#include <iostream>

bool funkcija(float x, float y, float x0, float y0, float r){

    if((x-x0)*(x-x0)+(y-y0)*(y-y0)<=r*r){
        return true;
    }
    else{
        return false;
    }

}

int main(){
    
    if(funkcija(1, 1, 2, 2, 0.5)){
        std::cout << "Tocka se nalazi unutar kruznice." << std::endl;
    }
    else{
        std::cout << "Tocka se ne nalazi unutar kruznice." << std::endl;
    }

    return 0;
}