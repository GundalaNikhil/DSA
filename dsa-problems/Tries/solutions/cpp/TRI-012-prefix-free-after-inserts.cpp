#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;
    
public:
    Solution() { root = new TrieNode(); }
    
    bool insert(const string& number) {
        TrieNode* node = root;
        for (char c : number) {
            if (node->isEnd) return false;
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        
        if (!node->children.empty()) return false;
        node->isEnd = true;
        return true;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    Solution solution;
    vector<bool> results;
    
    for (int i = 0; i < n; i++) {
        string number;
        getline(cin, number);
        results.push_back(solution.insert(number));
    }
    
    cout << "[";
    for (int i = 0; i < results.size(); i++) {
        cout << (results[i] ? "true" : "false");
        if (i < results.size() - 1) cout << ",";
    }
    cout << "]" << endl;
    
    return 0;
}
