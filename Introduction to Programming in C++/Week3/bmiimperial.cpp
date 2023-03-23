#include<bits/stdc++.h>
using namespace std;
int main() {
    float height;
    float weight;

    // Input height and weight
    cout << "Please enter weight in pounds: ";
    cin >> weight;
    cout << "Please enter height in inches: ";
    cin >> height;
    
    // Calculate BMI
    weight *= 0.453592;
    height *= 0.0254;
    float bmi = weight / pow(height, 2);
    cout.flags(ios::fixed);
    cout.precision(2);
    cout << "BMI is: " << bmi << endl;
    return 0;
}