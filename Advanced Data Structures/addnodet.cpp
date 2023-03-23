#include <bits/stdc++.h>
using namespace std;
class NODE {
    public:
        string firstname;
        string lastname;
        string email;
        NODE* next;
};
void add_node_tail(NODE** data, string firstname,string lastname, string email) {
    if (*data == nullptr) {
        *data = new NODE;
        (*data)->firstname = firstname;
        (*data)->lastname = lastname;
        (*data)->email = email;
    }
    else {
        NODE* temp = new NODE;
        temp->firstname = firstname;
        temp->lastname = lastname;
        temp->email = email;
        temp->next = (*data)->next;
        (*data)->next = temp;
    }
    return;
}