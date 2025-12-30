#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    unordered_set<int> wordIds;
};

class Solution {
private:
    TrieNode* root;
    string longestPrefix;

    void insertWord(const string& word, int wordId) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->wordIds.insert(wordId);
        }
    }

    void dfs(TrieNode* node, string prefix, int totalWords) {
        // If all words are represented at this node, update longest prefix
        if (node->wordIds.size() == totalWords) {
            if (prefix.length() > longestPrefix.length()) {
                longestPrefix = prefix;
            }
        }

        // Continue DFS
        for (auto& [ch, child] : node->children) {
            dfs(child, prefix + ch, totalWords);
        }
    }

public:
    Solution() {
        root = new TrieNode();
        longestPrefix = "";
    }

    string longestCommonPrefixAfterOneDeletion(vector<string>& words) {
        int n = words.size();

        // Insert all variants into trie
        for (int wordId = 0; wordId < n; wordId++) {
            const string& word = words[wordId];

            // Insert original word
            insertWord(word, wordId);

            // Insert all single-deletion variants
            for (int i = 0; i < word.length(); i++) {
                string variant = word.substr(0, i) + word.substr(i + 1);
                insertWord(variant, wordId);
            }
        }

        // DFS to find longest prefix with all word IDs
        dfs(root, "", n);

        return longestPrefix;
    }
};

int main() {
    int n;
    cin >> n;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }

    Solution solution;
    string result = solution.longestCommonPrefixAfterOneDeletion(words);

    cout << result << endl;

    return 0;
}
