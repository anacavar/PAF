#include <Particle.h>
#include <iostream>

int main(){

    Particle p1(10, 45, 0, 0);
    Particle p2(10, 90, 0, 0);
    Particle p3(0, 60, 0, 0);
    Particle p4(10, 60, 0, 0);

    std::cout << p1.range() << std::endl;
    std::cout << p1.range() << std::endl;
    
    std::cout << p2.range() << std::endl;
    std::cout << p2.time() << std::endl;

    std::cout << p3.range() << std::endl;
    std::cout << p3.time() << std::endl;
    
    std::cout << p4.range() << std::endl;
    std::cout << p4.time() << std::endl;

    return 0;
}