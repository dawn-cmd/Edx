#include <bits/stdc++.h>
using namespace std;
class BST {
    public:
        int data;
        int size = 1;
        BST *left = NULL;
        BST *right = NULL;

        BST() {
            data = 0; 
        }

        BST(int key) {
            data = key;
        }

        void insert(int num) {
            if (num <= data) {
                if (!left) {
                    left = new BST(num);
                }
                else {
                    left->insert(num);
                }
            }
            else {
                if (!right) {
                    right = new BST(num);
                }
                else {
                    right->insert(num);
                }
            }
            size += 1;
        }

        int nth_node(int n) {
            int base = left ? left->size : 0;
            if (n <= base) {
                return left->nth_node(n);
            }
            if (n == base + 1) {
                return data;
            } 
            if (n > base + 1) {
                return right->nth_node(n - base - 1);
            }
        }
};