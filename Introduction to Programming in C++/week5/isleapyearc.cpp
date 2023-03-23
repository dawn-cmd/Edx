#include<bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {
    int n = 0;

    // input n
    for (int i = 0; i < strlen(argv[1]); ++i) {
        n = n * 10 + argv[1][i] - '0';
    }

    // check leap year or not
    if (n % 4 == 0 && n % 100 != 0) {
        cout << n << " was a leap year" << endl;
    }
    else if (n % 400 == 0) {
        cout << n << " was a leap year" << endl;
    }
    else {
        cout << n << " was not a leap year" << endl;
    }
    return 0; 
}