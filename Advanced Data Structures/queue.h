#include <bits/stdc++.h>
using namespace std;
#define MAX 1000

class Queue {
    public:
        int rear_value;
        int a[MAX]; // Maximum size of Queue
        Queue() { rear_value = -1; }
        bool enqueue(int x) {
            if (rear_value == MAX - 1) {
                return 0;
            }
            a[++rear_value] = x;
            return 1;
        };
        int dequeue() {
            if (rear_value == -1) {
                return 0;
            }
            int ans = a[0];
            for (int i = 0; i < rear_value; ++i) {
                a[i] = a[i + 1]; 
            }
            --rear_value;
            return ans;
        };
        int front() {
            return rear_value == -1 ? 0 : a[0];
        };
        int rear() {
            return rear_value == -1 ? 0: a[rear_value];
        };
};