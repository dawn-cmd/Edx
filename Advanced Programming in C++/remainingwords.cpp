#include<bits/stdc++.h>
using namespace std;
string remainingwords(string s) {
    int start = 0;
    while (s[start] != ' ') {
        start++;
    }
    while (s[start] == ' ') {
        start++;
    }
    return s.substr(start, s.length() - start);
}