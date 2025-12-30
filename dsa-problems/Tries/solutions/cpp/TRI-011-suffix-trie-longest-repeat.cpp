#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int suffixCount = 0;  // Number of suffixes passing through this node
};

class Solution {
private:
    TrieNode* root;
    int maxLength;

    void insertSuffix(const string& suffix) {
        TrieNode* node = root;
        for (char c : suffix) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->suffixCount++;  // Increment count for each suffix passing through
        }
    }

    void dfs(TrieNode* node, int depth) {
        // A repeated substring exists if 2+ suffixes pass through this node
        if (node->suffixCount >= 2 && depth > 0) {
            maxLength = max(maxLength, depth);
        }

        for (auto& [ch, child] : node->children) {
            dfs(child, depth + 1);
        }
    }

public:
    Solution() {
        root = new TrieNode();
        maxLength = 0;
    }

    int longestRepeatedSubstring(const string& s) {
        for (int i = 0; i < s.length(); i++) {
            insertSuffix(s.substr(i));
        }

        dfs(root, 0);
        return maxLength;
    }
};

int main() {
    string s;
    getline(cin, s);

    Solution solution;
    int result = solution.longestRepeatedSubstring(s);
    cout << result << endl;

    return 0;
}
