#include<bits/stdc++.h>
using namespace std;
int main() {
    float height;
    float weight;

    // Input height and weight
    cout << "Please enter weight in kilograms: ";
    cin >> weight;
    cout << "Please enter height in meters: ";
    cin >> height;
    
    // Calculate BMI
    float bmi = weight / pow(height, 2);
    cout.flags(ios::fixed);
    cout.precision(2);
    cout << "BMI is: " << bmi << endl;
    return 0;
}