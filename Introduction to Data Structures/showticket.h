#include<bits/stdc++.h>
using namespace std;
class ShowTicket {
    private:
        string field;
        string seat;
        bool sold;

    public:
        ShowTicket(string infield, string inseat) {
            seat = inseat;
            field = infield;
            sold = false;
        }
        bool is_sold() {
            return sold;
        }
        void sell_seat() {
            sold = true;
        }
        string print_ticket() {
            return field + " " + seat + " " + (sold == 1 ? "sold" : "avaliable");
        }
};