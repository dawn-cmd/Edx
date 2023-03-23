#include <bits/stdc++.h>
#include "sportticket.h"
using namespace std;
class TicketSales {
    public:
        string print_ticket(ShowTicket *myticket) {
            return myticket->print_ticket();
        }

        string print_ticket(SportTicket *myticket) {
            return myticket->print_ticket();
        }
};