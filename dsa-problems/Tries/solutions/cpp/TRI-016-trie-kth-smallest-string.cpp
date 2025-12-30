#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    map<char, TrieNode*> children;  // map maintains alphabetical order
    bool isEnd = false;
    int count = 0;
};

class Solution {
private:
    TrieNode* root;
    string result;
    int remaining;

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

    bool dfs(TrieNode* node, string& path) {
        if (node->isEnd) {
            remaining--;
            if (remaining == 0) {
                result = path;
                return true;
            }
        }

        for (auto& [c, child] : node->children) {
            if (child->count >= remaining) {
                path.push_back(c);
                if (dfs(child, path)) {
                    return true;
                }
                path.pop_back();
            } else {
                remaining -= child->count;
            }
        }

        return false;
    }

public:
    Solution() { root = new TrieNode(); }

    string kthSmallest(vector<string>& words, int k) {
        for (const string& word : words) {
            insert(word);
        }

        remaining = k;
        string path = "";
        dfs(root, path);

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
    string result = solution.kthSmallest(words, k);

    cout << result << endl;

    return 0;
}
