#include<bits/stdc++.h>
using namespace std;
int main() {
    string s;
    int mid;
    // define the paraments

    cout << "Enter an odd length string: ";
    getline(cin, s);
    // input the string

    mid = s.length() / 2;
    // calculate the mid

    printf("Middle character: %s\n", s.substr(mid, 1).c_str());
    printf("First half: %s\n", s.substr(0, mid).c_str());
    printf("Second half: %s\n", s.substr(mid + 1, mid).c_str());
    // output the ans
    return 0;
}