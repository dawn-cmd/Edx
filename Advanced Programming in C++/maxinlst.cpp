#include<bits/stdc++.h>
using namespace std;
int maxinlst(int lst[], int size) {
    int maxn = INT_MIN;
    for (int i = 0; i < size; ++i) {
        if (lst[i] > maxn) {
            maxn = lst[i];
        }
    }
    return maxn;
}