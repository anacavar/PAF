#include <Particle.h>
#include <iostream>
#include <math.h>

Particle::Particle(double v0, double theta, double x0, double y0, double step){
    t = 0;
    x = x0;
    y = 0;
    dt = step;
    theta = theta * 2*3.14/360;
    vx = v0*cos(theta);
    vy = v0*sin(theta);
}

Particle::~Particle(){}

void Particle::evolve(){
    while (y>=0){
        t = t+dt;
        x = x+vx*dt;
        y = y+vy*dt;
        vy = vy+g*dt;
    }
}

double Particle::range(){
    evolve();
    return x;
}

double Particle::time(){
    evolve();
    return t;
}