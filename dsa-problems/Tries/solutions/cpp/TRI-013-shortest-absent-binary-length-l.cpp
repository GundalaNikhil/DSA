#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;

    void insert(const string& s) {
        TrieNode* node = root;
        for (char c : s) {
            int idx = c - '0';
            if (node->children[idx] == nullptr) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    string dfs(TrieNode* node, string path, int L) {
        if (path.length() == L) {
            return node->isEnd ? "" : path;
        }

        // Try '0' first
        if (node->children[0] == nullptr) {
            return path + string(L - path.length(), '0');
        }

        string result = dfs(node->children[0], path + '0', L);
        if (!result.empty()) return result;

        // Try '1'
        if (node->children[1] == nullptr) {
            return path + '1' + string(L - path.length() - 1, '0');
        }

        return dfs(node->children[1], path + '1', L);
    }

public:
    Solution() { root = new TrieNode(); }

    string findShortestAbsent(vector<string>& binaryStrings, int L) {
        if (binaryStrings.size() == pow(2, L)) {
            return "";
        }

        for (const string& s : binaryStrings) {
            insert(s);
        }

        return dfs(root, "", L);
    }
};

int main() {
    int L, n;
    cin >> L >> n;
    cin.ignore();

    vector<string> binaryStrings(n);
    for (int i = 0; i < n; i++) {
        getline(cin, binaryStrings[i]);
    }

    Solution solution;
    string result = solution.findShortestAbsent(binaryStrings, L);

    cout << result << endl;

    return 0;
}
