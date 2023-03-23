#include <bits/stdc++.h>
#define MAX 1000
using namespace std;

class Stack {
    public:
        int top;
        int a[MAX]; // Maximum size of Stack
        Stack() { 
            top = -1; 
        }
        bool push(int x) {
            if (top == MAX - 1) {
                return 0;
            }
            a[++top] = x;
            return 1;
        }
        int pop() {
            return  top == -1 ? 0 : a[top--];
        };
        int peek() {
            return top == -1 ? 0 : a[top];
        };
        bool isEmpty() {
            return top == -1;
        };
};