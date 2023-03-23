#include<bits/stdc++.h>
using namespace std;
float avgoflst(int lst[], int size) {
    float ans = 0;
    for (int i = 0; i < size; ++i) {
        ans += lst[i];
    }
    return ans / size;
}