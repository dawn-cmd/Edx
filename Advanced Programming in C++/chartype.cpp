#include<bits/stdc++.h>
using namespace std;
int main() {
    char c;
    // define the parament

    cout << "Enter a character: ";
    cin >> c;
    // input c

    if (c >= '0' && c <= '9') {
        cout << c << " is a digit." << endl;
    }
    else if (c >= 'a' && c <= 'z') {
        cout << c << " is a lower case letter." << endl;
    }
    else if (c >= 'A' && c <= 'Z') {
        cout << c << " is an upper case letter." << endl;
    }
    else {
        cout << c << " is a non-alphanumeric character." << endl;
    }
    // output ans
    return 0;
}