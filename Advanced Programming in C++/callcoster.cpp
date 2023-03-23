#include <bits/stdc++.h>
using namespace std;
int main() {
    map <string, int> h;
    h["Mon"] = 1;
    h["Tue"] = 2;
    h["Wed"] = 3;
    h["Thr"] = 4;
    h["Fri"] = 5;
    h["Sat"] = 6;
    h["Sun"] = 7;
    int time;
    int len;
    int day;
    double cost;
    // define and intialize paraments

    string tmp;
    cout << "Enter the day the call started at: ";
    cin >> tmp;
    day = h[tmp];
    cout << "Enter the time the call started at (hhmm): ";
    cin >> time;
    cout << "Enter the duration of the call (in minutes): ";
    cin >> len;
    // input the paraments

    if (day >= 1 && day <= 5) {
        cost = (time >= 800 && time <= 1800 ? 0.4 : 0.25) * len;
    }
    else {
        cost = len * 0.15;
    }
    // calculate the cost

    printf("This call will cost $%.2f\n", cost);
    // output the cost
    return 0;
}