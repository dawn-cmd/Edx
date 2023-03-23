#include<bits/stdc++.h>
using namespace std;
int main() {
    int ga;
    int gb;

    //input grades
    cout << "Please enter 2 grades, separated by a space: ";
    cin >> ga >> gb;

    // evaluate
    if (ga < 60 && gb < 60) {
        cout << "Student Failed:(" << endl;
    }
    else if (ga >= 95 && gb >= 95) {
        cout << "Student Graduated with Honors:)" << endl;
    }
    else {
        cout << "Student Graduated!" << endl;
    }
    return 0;
}