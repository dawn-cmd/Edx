#include<bits/stdc++.h>
using namespace std;
int main() {
    int dollars;
    int cents;

    // Input dollars and cents
    cout << "# of dollars:";
    cin >> dollars;
    cout << "# of cents:";
    cin >> cents;
    cents += dollars * 100;

    // Calculate the number of coins
    int quarters = cents / 25;
    cents %= 25;
    int dimes = cents / 10;
    cents %= 10;
    int nickels = cents / 5;
    cents %= 5;
    int pennies = cents;

    // Output the ans
    cout << "The coins are " << quarters << " quarters, " << dimes << " dimes, " << nickels << " nickels and " << pennies << " pennies" << endl;
    return 0;
}