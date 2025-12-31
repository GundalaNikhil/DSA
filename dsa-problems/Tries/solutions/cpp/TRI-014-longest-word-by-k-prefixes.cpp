#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
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
        }
        node->isEnd = true;
    }

    int countPrefixes(const string& word) {
        TrieNode* node = root;
        int count = 0;

        for (int i = 0; i < word.length(); i++) {
            node = node->children[word[i]];
            if (i < word.length() - 1 && node->isEnd) {
                count++;
            }
        }

        return count;
    }

public:
    Solution() { root = new TrieNode(); }

    string longestWordWithKPrefixes(vector<string>& words, int k) {
        // Build trie
        for (const string& word : words) {
            insert(word);
        }

        string result = "";
        int maxLen = 0;

        // Check each word
        for (const string& word : words) {
            int prefixCount = countPrefixes(word);
            if (prefixCount >= k) {
                if (word.length() > maxLen ||
                    (word.length() == maxLen && word < result)) {
                    result = word;
                    maxLen = word.length();
                }
            }
        }

        return result;
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    cin.ignore();

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        getline(cin, words[i]);
    }

    Solution solution;
    string result = solution.longestWordWithKPrefixes(words, k);

    cout << result << endl;

    return 0;
}
