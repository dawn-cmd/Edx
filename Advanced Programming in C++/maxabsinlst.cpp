#include<bits/stdc++.h>
using namespace std;
int maxabsinlst(int lst[], int size) {
    int maxn = INT_MIN;
    for (int i = 0; i < size; ++i) {
        if (abs(lst[i]) > maxn) {
            maxn = abs(lst[i]);
        }
    }
    return maxn;
}