#include<bits/stdc++.h>
using namespace std;
int main() {
    float item1;
    float item2;
    char c;
    float tax;
    // define paraments
     
    cout << "Enter price of the first item: ";
    cin >> item1;
    cout << "Enter price of the second item: ";
    cin >> item2;
    cout << "Does customer have a club card? (Y/N): ";
    cin >> c;
    cout << "Enter tax rate, e.g. 5.5 for 5.5% tax: ";
    cin >> tax;
    // input paraments

    float base = item1 + item2;
    float discount = item1 < item2 ? item1 / 2 + item2 : item2 / 2 + item1;
    if (c == 'Y' || c == 'y') {
        discount *= 0.9;
    }
    float total = discount + discount * tax / 100;
    // caculate cost

    printf("Base price = %.2f\n", base);
    printf("Price after discounts = %.2f\n", discount);
    printf("Total price = %.2f\n", total);
    // print ans

    return 0;
}