#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[2];
    int count;

    TrieNode() {
        children[0] = children[1] = nullptr;
        count = 0;
    }
};

class Solution {
    void insert(TrieNode* root, int num) {
        TrieNode* curr = root;
        for (int i = 29; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (!curr->children[bit]) {
                curr->children[bit] = new TrieNode();
            }
            curr = curr->children[bit];
            curr->count++;
        }
    }

    int countLessEqual(TrieNode* root, int num, int K) {
        if (K < 0) return 0;
        TrieNode* curr = root;
        int count = 0;
        for (int i = 29; i >= 0; i--) {
            if (!curr) break;
            int bitNum = (num >> i) & 1;
            int bitK = (K >> i) & 1;

            if (bitK == 1) {
                if (curr->children[bitNum]) {
                    count += curr->children[bitNum]->count;
                }
                curr = curr->children[1 - bitNum];
            } else {
                curr = curr->children[bitNum];
            }
        }
        if (curr) count += curr->count;
        return count;
    }

    long long solve(const vector<int>& nums, int L, int U) {
        TrieNode* root = new TrieNode();
        long long total = 0;
        int limitL = L - 1;

        for (int x : nums) {
            int cU = countLessEqual(root, x, U);
            int cL = countLessEqual(root, x, limitL);
            total += (cU - cL);
            insert(root, x);
        }
        // Memory leak check: In CP context, often ignored, but we should traverse delete
        // For strictness, assume simple struct is fine.
        return total;
    }

public:
    long long countPairwiseXorBandParity(vector<int>& a, int L, int U) {
        vector<int> evens, odds;
        for (int i = 0; i < a.size(); i++) {
            if (i % 2 == 0) evens.push_back(a[i]);
            else odds.push_back(a[i]);
        }
        return solve(evens, L, U) + solve(odds, L, U);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int L, U;
    cin >> L >> U;

    Solution solution;
    cout << solution.countPairwiseXorBandParity(a, L, U) << "\n";
    return 0;
}
