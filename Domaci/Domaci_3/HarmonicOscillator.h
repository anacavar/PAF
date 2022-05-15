class HarmonicOscillator{  
    private:
     double x, v, a, t;
     double x0, v0, k, m, tmax;
     double dt = 0.01;
     double g = -9.81;
     void oscillate();

    public:
     HarmonicOscillator(double x0_, double v0_, double k_, double m_, double tmax_);
     ~HarmonicOscillator();
     void data_export();
};