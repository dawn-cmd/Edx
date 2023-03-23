#include<bits/stdc++.h>
using namespace std;
string firstword(string s) {
    string ans = "";
    for (int i = 0; s[i] != ' ' && i < s.length(); ++i) {
        ans += s[i]; 
    }
    return ans;
}