#include<bits/stdc++.h>
using namespace std;
int main() {
    float height;
    float weight;
    cout << "Please enter weight in kilograms: ";
    cin >> weight;
    cout << "Please enter height in meters: ";
    cin >> height;
    // input heght and weight

    float bmi = weight / pow(height, 2);
    string state;
    if (bmi < 18.5) {
        state = "Underweight";
    }
    else if (bmi < 24.9) {
        state = "Normal";
    }
    else if (bmi < 29.9) {
        state = "Overweight";
    }
    else {
        state = "Obese";
    }
    // calculate bmi

    printf("BMI is: %.2f, Status is %s\n", bmi, state.c_str());
    // print ans
    return 0;
}