#include <HarmonicOscillator.h>
#include <iostream>
#include <fstream>

using namespace std;

HarmonicOscillator::HarmonicOscillator(double x0_, double v0_, double k_, double m_, double tmax_){
    x0 = x0_;
    v0 = v0_;
    k = k_;
    m = m_;
    tmax = tmax_;
    a = -k*x0/m;
    v = v0;
    x = x0;
    t = 0;
}

HarmonicOscillator::~HarmonicOscillator(){}

void HarmonicOscillator::oscillate(){
    a=-(k/m)*x;
    v=v+a*dt;
    x=x+v*dt;
    t=t+dt;
}

void HarmonicOscillator::data_export(){

    ofstream filewrite_x("/repos/PAF/Domaci/Domaci_3/HO_x.txt", ofstream::out);
    ofstream filewrite_v("/repos/PAF/Domaci/Domaci_3/HO_v.txt", ofstream::out);
    ofstream filewrite_a("/repos/PAF/Domaci/Domaci_3/HO_a.txt", ofstream::out);
    ofstream filewrite_t("/repos/PAF/Domaci/Domaci_3/HO_t.txt", ofstream::out);

    while(t < tmax){
        filewrite_x << x <<"\n";
        filewrite_v << v <<"\n";
        filewrite_a << a <<"\n";
        filewrite_t << t << "\n";
        oscillate();
    }

    filewrite_x.close();
    filewrite_v.close();
    filewrite_a.close();
    filewrite_t.close();
}