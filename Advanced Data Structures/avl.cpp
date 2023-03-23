#include <bits/stdc++.h>
using namespace std;
class Node {
    public:
        int key;
        Node* left;
        Node* right;
        int height;
};
Node* new_node(int key) {
    Node* ans = new Node();
    ans->key = key;
    ans->left = NULL;
    ans->right = NULL;
    ans->height = 1;
    return ans;
}
Node* insertnb(Node* node, int key) {
    if (!node) {
        node = new_node(key);
        return node;
    } 
    if (key <= node->key) {
        node->left = insertnb(node->left, key);
        node->height = max(node->height, node->left->height + 1);
    }
    else {
        node->right = insertnb(node->right, key);
        node->height = max(node->height, node->right->height + 1);
    }
    return node;
}
Node* left_rotate(Node* x) {
    Node* xchild = x->right;
    x->right = xchild->left;
    xchild->left = x;
    x->height = max(x->left ? x->left->height : 0,
                    x->right ? x->right->height : 0) + 1;
    xchild->height = max(xchild->left ? xchild->left->height : 0,              
                         xchild->right ? xchild->right->height : 0) + 1;
    return xchild;
}
Node* right_rotate(Node* x) {
    Node* xchild = x->left;
    x->left = xchild->right;
    xchild->right = x;
    x->height = max(x->left ? x->left->height : 0,
                    x->right ? x->right->height : 0) + 1;
    xchild->height = max(xchild->left ? xchild->left->height : 0,              
                         xchild->right ? xchild->right->height : 0) + 1;
    return xchild; 
}
int get_balance(Node* x) {
    if (!x) {
        return 0;
    }
    int lh = x->left ? x->left->height : 0;
    int rh = x->right ? x->right->height : 0;
    return lh - rh;
}
Node* insert(Node* node, int key) {
    if (!node) {
        node = new_node(key);
        return node;
    } 
    if (key <= node->key) {
        node->left = insertnb(node->left, key);
        node->height = max(node->height, node->left->height + 1);
        if (abs(get_balance(node)) > 1) {
            if (key > node->left->key) {
                node->left = left_rotate(node->left);
            }
            node = right_rotate(node);
        }
    }
    else {
        node->right = insertnb(node->right, key);
        node->height = max(node->height, node->right->height + 1);
        if (abs(get_balance(node)) > 1) {
            if (key <= node->right->key) {
                node->right = right_rotate(node->right);
            }
            node = left_rotate(node);
        }
    }
    return node;
}