#include <bits/stdc++.h>
#include "showticket.h"
using namespace std;
class SportTicket: public ShowTicket {
    private:
        bool beer;

    public:
        SportTicket(string ifield, string iseat): ShowTicket(ifield, iseat) {
            beer = 0;
        }

        bool beer_sold() {
            return beer;
        }

        void sell_beer() {
            beer = 1;
        }

        string print_ticket() {
            return ShowTicket::print_ticket() + ' ' + (beer ? "beer" : "nobeer");
        }
};
