#include <iostream>
#include <vector>
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
    int nodeCount;

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
                nodeCount++;
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

public:
    Solution() {
        root = new TrieNode();
        nodeCount = 1; // Start with root
    }

    int countTrieNodes(vector<string>& words) {
        for (const string& word : words) {
            insert(word);
        }
        return nodeCount;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        getline(cin, words[i]);
    }

    Solution solution;
    int result = solution.countTrieNodes(words);

    cout << result << endl;

    return 0;
}
