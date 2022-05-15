// Napišite C++ program koji za zadane koeficijente rješava sustav od dvije jednadžbe s dvije nepoznanice:
// a1x + b1y = c1
// a2x + b2y = c2.

#include <iostream>

void rijesi_sustav(float a1, float b1, float c1, float a2, float b2, float c2){
    if (a1*b2-b1*a2==0){
        std::cout << "Sustav nema rješenja" << std::endl;
    }
    else{
        float x = (c1-c2*b1/b2)/(a1-a2*b1/b2);
        float y = (c1-a1*x)/b1;
        std::cout << "Rjesenje sustava: x = "+std::to_string(x)+" y = "+std::to_string(y) << std::endl;
    }
}

int main(){

    float a1 = 1;
    float b1 = 2;
    float c1 = 3;
    float a2 = 4;
    float b2 = 5;
    float c2 = 6;

    rijesi_sustav(a1, b1, c1, a2, b2, c2);

    return 0;
}