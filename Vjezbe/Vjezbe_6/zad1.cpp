// Napišite C++ program u koji sadrži funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije
// točke. Neka ta funkcija na ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu
// funkciju u svom programu

#include <iostream>

std::string funkcija(int x1, int y1, int x2, int y2){

    float a = (y2-y1)/(x2-x1);
    float b = y1-a*x1;

    std::string a_string = std::to_string(a);
    std::string b_string = std::to_string(b);

    if (b>=0) {
        return "y="+a_string+"x+"+b_string;
    }
    else {
        return "y="+a_string+"x-"+b_string;
    }
}

int main() {
    std::cout << funkcija(1, 2, 3, 4) << std::endl;
    return 0;
}