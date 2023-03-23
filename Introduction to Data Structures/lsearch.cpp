#include<bits/stdc++.h>
using namespace std;
int linear_search(int search_value, int lst[], int elements) {
    int cnt = 0;
    for (int i = 0; i < elements; ++i) {
        ++cnt;
        if (lst[i] == search_value) {
            break;
        }
    }
    return cnt;
}