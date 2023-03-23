#include<bits/stdc++.h>
using namespace std;
int main() {

    // Input the number of coins
    int quarters;
    int dimes;
    int nickels;
    int pennies;
    cout << "Please enter the number of coins:" << endl;
    cout << "# of quarters:";
    cin >> quarters;
    cout << "# of dimes:";
    cin >> dimes;
    cout << "# of nickels:";
    cin >> nickels;
    cout << "# of pennies:";
    cin >> pennies;

    // Calculate the value
    int dollars = int(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01);
    int cents = quarters * 25 + dimes * 10 + nickels * 5 + pennies; 
    cents %= 100;

    // Output the ans
    cout << "The total is "<< dollars << " dollars and "<< cents <<" cents" << endl;
    return 0;
}