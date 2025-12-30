#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    Node* children[26];
    Node* fail;
    Node* output;
    vector<pair<int, long long>> patterns; // len, weight

    Node() {
        for (int i = 0; i < 26; i++) children[i] = nullptr;
        fail = nullptr;
        output = nullptr;
    }
};

class Solution {
public:
    long long maxCooldownScore(const string& text, const vector<string>& patterns,
                               const vector<long long>& weights, int g) {
        Node* root = new Node();
        
        // 1. Build Trie
        for (size_t i = 0; i < patterns.size(); i++) {
            Node* curr = root;
            for (char c : patterns[i]) {
                int idx = c - 'a';
                if (!curr->children[idx]) curr->children[idx] = new Node();
                curr = curr->children[idx];
            }
            curr->patterns.push_back({(int)patterns[i].length(), weights[i]});
        }
        
        // 2. Build Failure Links
        queue<Node*> q;
        for (int i = 0; i < 26; i++) {
            if (root->children[i]) {
                root->children[i]->fail = root;
                q.push(root->children[i]);
            } else {
                root->children[i] = root;
            }
        }
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            
            if (!curr->fail->patterns.empty()) curr->output = curr->fail;
            else curr->output = curr->fail->output;
            
            for (int i = 0; i < 26; i++) {
                if (curr->children[i]) {
                    curr->children[i]->fail = curr->fail->children[i];
                    q.push(curr->children[i]);
                } else {
                    curr->children[i] = curr->fail->children[i];
                }
            }
        }
        
        // 3. DP
        int n = text.length();
        vector<long long> dp(n + 1, 0);
        Node* curr = root;
        
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i];
            curr = curr->children[text[i] - 'a'];
            
            Node* temp = curr;
            while (temp != root) {
                for (auto& p : temp->patterns) {
                    int len = p.first;
                    long long w = p.second;
                    int prevIdx = i + 1 - len - g;
                    long long prevScore = (prevIdx < 0) ? 0 : dp[prevIdx];
                    dp[i + 1] = max(dp[i + 1], prevScore + w);
                }
                if (temp->output == nullptr) break;
                temp = temp->output;
            }
        }
        
        // Cleanup memory (optional for CP, good for practice)
        // ... recursive delete ...
        
        return dp[n];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<string> patterns(k);
        vector<long long> weights(k);
        for (int i = 0; i < k; i++) {
            cin >> patterns[i] >> weights[i];
        }
        int g;
        cin >> g;
        string text;
        cin >> text;

        Solution solution;
        cout << solution.maxCooldownScore(text, patterns, weights, g) << "\n";
    }
    return 0;
}
