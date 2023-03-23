#include<bits/stdc++.h>
using namespace std;
int binary_search(int search_value, int lst[], int elements) {
    int st = 0;
    int ed = elements - 1;
    int cnt = 0;
    while (st <= ed) {
        int mid = st + ed >> 1;
        cnt++;
        if (search_value > lst[mid]) {
            st = mid + 1;
        }
        else if (search_value < lst[mid]) {
            ed = mid - 1;
        }
        else {
            break;
        }
    }
    return cnt;
}