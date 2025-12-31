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

    bool dfs(TrieNode* node, const string& query, int index, int edits) {
        if (edits > 1) {
            return false;
        }

        if (index == query.length()) {
            if (node->isEnd && edits == 1) {
                return true;
            }
            if (edits == 0) {
                for (auto& [ch, child] : node->children) {
                    if (child->isEnd) {
                        return true;
                    }
                }
            }
            return false;
        }

        char c = query[index];

        // Match without edit
        if (node->children.find(c) != node->children.end()) {
            if (dfs(node->children[c], query, index + 1, edits)) {
                return true;
            }
        }

        if (edits < 1) {
            // Substitution
            for (auto& [ch, child] : node->children) {
                if (ch != c) {
                    if (dfs(child, query, index + 1, edits + 1)) {
                        return true;
                    }
                }
            }

            // Deletion from query
            if (dfs(node, query, index + 1, edits + 1)) {
                return true;
            }

            // Insertion into query
            for (auto& [ch, child] : node->children) {
                if (dfs(child, query, index, edits + 1)) {
                    return true;
                }
            }
        }

        return false;
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

    bool hasEditDistance1(const string& query) {
        return dfs(root, query, 0, 0);
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

    string query;
    getline(cin, query);

    bool result = solution.hasEditDistance1(query);
    cout << (result ? "true" : "false") << endl;

    return 0;
}
