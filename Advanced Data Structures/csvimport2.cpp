#include <bits/stdc++.h>
using namespace std;

class NODE {
    public:
        string firstname;
        string lastname;
        string email;
        NODE* next;
};

void csv_import2(NODE** data, string filename) {
    ifstream infile;
    infile.open(filename);
    string now;
    NODE* head = nullptr;
    NODE* tail = nullptr;
    while (getline(infile, now)) {
        NODE* temp = new NODE;
        temp->firstname = "";
        temp->lastname = "";
        temp->email = "";
        temp->next = nullptr;
        int id = 0;
        for (; now[id] != ',' && id < now.length(); ++id) {
            temp->firstname += now[id];
        }
        ++id;
        for (; now[id] != ',' && id < now.length(); ++id) {
            temp->lastname += now[id];
        }
        ++id; 
        for (; id < now.length(); ++id) {
            temp->email += now[id];
        }
        if (tail == nullptr) {
            tail = temp;
            head = temp;
        }
        else {
            tail->next = temp;
            tail = temp;
        }
    }
    *data = head;
}