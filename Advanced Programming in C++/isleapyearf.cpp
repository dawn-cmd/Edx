#include<bits/stdc++.h>
using namespace std;
bool isleapyear(int inyear) {
    if (inyear % 4 == 0 && inyear % 100 != 0) {
        return 1;
    }
    if (inyear % 400 == 0) {
        return 1;
    }
    return 0;
}