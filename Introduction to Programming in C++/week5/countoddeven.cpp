#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    int cnt_odd = 0;
    int cnt_even = 0;

    // input numbers
    cout << "Please enter 4 positive integers, separated by a space:" << endl;
    for (int i = 0; i < 4; ++i) {
        cin >> n;
        if (n % 2 == 0) {
            cnt_even += 1;
        }
        else {
            cnt_odd += 1;
        }
    }

    // print ans
    if (cnt_even == cnt_odd) {
        cout << "same number of evens and odds" << endl;
    }
    else if (cnt_odd > cnt_even) {
        cout << "more odds" << endl;
    }
    else {
        cout << "more evens" << endl;
    }
    return 0;
}