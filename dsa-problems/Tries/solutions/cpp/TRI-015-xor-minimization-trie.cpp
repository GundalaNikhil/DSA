#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
};

class Solution {
private:
    TrieNode* root;
    static const int MAX_BITS = 30;

    void insert(int num) {
        TrieNode* node = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node->children[bit] == nullptr) {
                node->children[bit] = new TrieNode();
            }
            node = node->children[bit];
        }
    }

    int query(int num) {
        TrieNode* node = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            if (node->children[bit] != nullptr) {
                node = node->children[bit];
            } else {
                result |= (1 << i);
                node = node->children[1 - bit];
            }
        }

        return result;
    }

public:
    Solution() { root = new TrieNode(); }

    int minimizeXOR(vector<int>& a, int X) {
        int n = a.size();
        vector<int> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] ^ a[i];
        }

        int minXor = INT_MAX;

        for (int j = 0; j <= n; j++) {
            if (root->children[0] != nullptr || root->children[1] != nullptr) {
                int target = prefix[j] ^ X;
                int closest = query(target);
                minXor = min(minXor, closest ^ target);
            }
            insert(prefix[j]);
        }

        return minXor;
    }
};

int main() {
    int n, X;
    cin >> n >> X;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    int result = solution.minimizeXOR(a, X);

    cout << result << endl;

    return 0;
}
