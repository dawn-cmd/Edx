#include <bits/stdc++.h>
using namespace std;
class ShowTickets {
    private:
        map <string, bool> check;
    
    public:
        bool is_sold(string row, string seat) {
            string id = row + " " + seat;
            if (check.find(id) == check.end()) {
                check[id] = false;
                return false;
            }
            else if (check.find(id) -> second == 0) {
                return false;
            }
            else {
                return true;
            }
        }

        void sell_seat(string row, string seat) {
            string id = row + " " + seat;
            check[id] = 1;
        }

        string print_ticket(string row, string seat) {
            string id = row + " " + seat;
            if (check.find(id) == check.end()) {
                check[id] = false;
                return id + " avaliable";
            }
            else if (check.find(id) -> second == 0) {
                return id + " avaliable";
            }
            else {
                return id + " sold";
            }
        }
};