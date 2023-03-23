#include<bits/stdc++.h>
using namespace std;
double* getDoubles(int numDoubles) {
    double *a = new double[numDoubles];
    for (int i = 0; i < numDoubles; ++i) {
        a[i] = (double)(i + 1) / 3;
    }
    return a;
}