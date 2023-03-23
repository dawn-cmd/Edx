#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;

    // input n
    cout << "Please enter a positive integer: ";
    cin >> n;

    // output even
    for (int i = 1; i <= n; ++i) {
        cout << i * 2 << endl;
    }
    return 0;
}