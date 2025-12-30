#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    long long val;
    TreeNode *left, *right;
    TreeNode(long long x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    TreeNode* insert(TreeNode* node, long long val) {
        if (!node) return new TreeNode(val);
        if (val < node->val) {
            node->left = insert(node->left, val);
        } else {
            node->right = insert(node->right, val);
        }
        return node;
    }

    int count;
    long long result;

    void inorder(TreeNode* node, long long L, long long R, int k) {
        if (!node || result != -1) return;

        if (node->val > L) {
            inorder(node->left, L, R, k);
        }

        if (result != -1) return;

        if (node->val >= L && node->val <= R) {
            count++;
            if (count == k) {
                result = node->val;
                return;
            }
        }

        if (node->val < R) {
            inorder(node->right, L, R, k);
        }
    }

public:
    long long kthInRange(const vector<long long>& values, long long L, long long R, int k) {
        TreeNode* root = nullptr;
        for (long long v : values) {
            root = insert(root, v);
        }

        count = 0;
        result = -1;
        inorder(root, L, R, k);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    long long L, R;
    cin >> L >> R;
    int k;
    cin >> k;

    Solution solution;
    cout << solution.kthInRange(values, L, R, k) << "\n";
    return 0;
}
