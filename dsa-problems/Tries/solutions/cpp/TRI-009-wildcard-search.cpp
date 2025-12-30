#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;

    bool dfs(TrieNode* node, const string& pattern, int index) {
        if (index == pattern.length()) {
            return node->isEnd;
        }

        char c = pattern[index];

        if (c == '?') {
            // Match any single character
            for (auto& [ch, child] : node->children) {
                if (dfs(child, pattern, index + 1)) {
                    return true;
                }
            }
            return false;
        } else if (c == '*') {
            // Match zero or more characters
            // Try matching 0 characters
            if (dfs(node, pattern, index + 1)) {
                return true;
            }
            // Try matching 1+ characters
            for (auto& [ch, child] : node->children) {
                if (dfs(child, pattern, index)) {
                    return true;
                }
            }
            return false;
        } else {
            // Regular character
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            return dfs(node->children[c], pattern, index + 1);
        }
    }

public:
    Solution() {
        root = new TrieNode();
    }

    void insertWord(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(const string& pattern) {
        return dfs(root, pattern, 0);
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();

    Solution solution;
    for (int i = 0; i < n; i++) {
        string word;
        getline(cin, word);
        solution.insertWord(word);
    }

    string pattern;
    getline(cin, pattern);

    bool result = solution.search(pattern);
    cout << (result ? "true" : "false") << endl;

    return 0;
}
