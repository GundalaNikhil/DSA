#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
};

class Solution {
public:
    int countDistinctSubstrings(const string& s) {
        if (s.empty()) {
            return 0;
        }
        TrieNode* root = new TrieNode();
        int nodeCount = 0;
        int n = static_cast<int>(s.size());

        for (int i = 0; i < n; i++) {
            TrieNode* curr = root;
            for (int j = i; j < n; j++) {
                char c = s[j];
                auto it = curr->children.find(c);
                if (it == curr->children.end()) {
                    TrieNode* next = new TrieNode();
                    curr->children[c] = next;
                    curr = next;
                    nodeCount++;
                } else {
                    curr = it->second;
                }
            }
        }

        return nodeCount;
    }
};

int main() {
    string s;
    getline(cin, s);

    Solution solution;
    int result = solution.countDistinctSubstrings(s);

    cout << result << '\n';
    return 0;
}
