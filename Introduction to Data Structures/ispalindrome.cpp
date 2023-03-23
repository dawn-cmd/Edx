#include<bits/stdc++.h>
using namespace std;
bool is_palindrome(int test) {
    int a = test % 10;
    int p = 1;
    while (test / p > 0) {
        p *= 10;
    }
    if (p <= 10) {
        return 1;
    }
    else {
        p /= 10;
    }
    int b = test / p;
    if (a == b) {
        return is_palindrome(test % p / 10);
    } 
    else {
        return 0;
    }
}