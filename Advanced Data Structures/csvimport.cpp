#include<bits/stdc++.h>
using namespace std;
void csv_import(string data[][10], int columns, int *records, string filename) {
    ifstream infile;
    infile.open(filename);
    *records = 0;
    int id = 0;
    string tmp;
    data[0][0] = "";
    while (getline(infile, tmp)) {
        *records += 1;
        for (int i = 0, j = 0; i < columns; ++i, ++j) {
            data[*records - 1][i] = "";
            while (j < tmp.length() && tmp[j] != ',') {
                data[*records - 1][i] += tmp[j];
                j++;
            }
        }
    }
}