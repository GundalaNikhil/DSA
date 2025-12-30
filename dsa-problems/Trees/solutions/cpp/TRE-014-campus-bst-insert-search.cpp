#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    TreeNode* root = nullptr;

    TreeNode* insert(TreeNode* node, int val) {
        if (!node) return new TreeNode(val);
        if (val < node->val) {
            node->left = insert(node->left, val);
        } else {
            node->right = insert(node->right, val);
        }
        return node;
    }

    void inorder(TreeNode* node, vector<int>& res) {
        if (!node) return;
        inorder(node->left, res);
        res.push_back(node->val);
        inorder(node->right, res);
    }

    bool search(TreeNode* node, int x) {
        if (!node) return false;
        if (node->val == x) return true;
        if (x < node->val) return search(node->left, x);
        return search(node->right, x);
    }

public:
    vector<int> buildInorder(const vector<int>& values) {
        root = nullptr; // Reset for fresh build
        for (int v : values) {
            root = insert(root, v);
        }
        vector<int> res;
        inorder(root, res);
        return res;
    }

    bool searchValue(const vector<int>& values, int x) {
        if (!root && !values.empty()) buildInorder(values);
        return search(root, x);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    int x;
    cin >> x;

    Solution solution;
    vector<int> inorder = solution.buildInorder(values);
    for (int i = 0; i < (int)inorder.size(); i++) {
        if (i) cout << ' ';
        cout << inorder[i];
    }
    cout << "\n" << (solution.searchValue(values, x) ? "true" : "false") << "\n";
    return 0;
}
