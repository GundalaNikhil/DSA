#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int count = 0;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->count++;
        }
        node->isEnd = true;
    }

    int findMinLength(const string& word) {
        TrieNode* node = root;
        for (int i = 0; i < word.length(); i++) {
            node = node->children[word[i]];
            if (node->count == 1) {
                return i + 1;
            }
        }
        return word.length();
    }

public:
    Solution() {
        root = new TrieNode();
    }

    vector<int> findMinimumPrefixLengths(vector<string>& words) {
        // Build trie with counts
        for (const string& word : words) {
            insert(word);
        }

        // Find minimum prefix length for each word
        vector<int> result;
        for (const string& word : words) {
            result.push_back(findMinLength(word));
        }

        return result;
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
    vector<int> result = solution.findMinimumPrefixLengths(words);

    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]" << endl;

    return 0;
}
