#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;

    // input n
    cout << "Please enter a positive integer greater than 1: ";
    cin >> n;

    // output fb
    int a = 1;
    int b = 1;
    cout << 1 << endl;
    for (int i = 1; i <= n - 1; ++i) {
        cout << b << endl;
        b = a + b;
        a = b - a;
    }
    return 0;
}