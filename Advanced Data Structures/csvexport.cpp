#include<bits/stdc++.h>
using namespace std;
void csv_export(string data[][10], int records,int columns, string filename) {
    ofstream outfile;
    outfile.open(filename);
    for (int i = 0; i < records; ++i) {
        for (int j = 0; j < columns; ++j) {
            outfile << data[i][j] << (j == columns - 1 ? '\n' : ',');
        }
    }
    outfile.close();
}