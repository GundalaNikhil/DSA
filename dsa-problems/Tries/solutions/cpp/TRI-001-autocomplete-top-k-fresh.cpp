#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord = false;
};

struct WordMetadata {
    int frequency;
    int lastUsed;
};

struct WordScore {
    string word;
    double score;

    bool operator<(const WordScore& other) const {
        if (abs(score - other.score) > 1e-9) {
            return score < other.score; // Max-heap by score
        }
        return word > other.word; // Min-heap by lexicographic
    }
};

class Solution {
private:
    TrieNode* root;
    unordered_map<string, WordMetadata> metadata;

    void collectWords(TrieNode* node, string prefix, vector<string>& result) {
        if (node->isEndOfWord) {
            result.push_back(prefix);
        }
        for (auto& [ch, child] : node->children) {
            collectWords(child, prefix + ch, result);
        }
    }

public:
    Solution() {
        root = new TrieNode();
    }

    void insertWord(string word, int frequency, int timestamp) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
        metadata[word] = {frequency, timestamp};
    }

    vector<string> autocomplete(string prefix, int currentTime, int D, int k) {
        // Navigate to prefix node
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }

        // Collect all words with this prefix
        vector<string> matches;
        collectWords(node, prefix, matches);

        // Compute decay scores
        priority_queue<WordScore> heap;
        for (const string& word : matches) {
            WordMetadata meta = metadata[word];
            double decay = exp(-(currentTime - meta.lastUsed) / (double)D);
            double score = meta.frequency * decay;
            heap.push({word, score});
        }

        // Extract top k
        vector<string> result;
        for (int i = 0; i < k && !heap.empty(); i++) {
            result.push_back(heap.top().word);
            heap.pop();
        }

        return result;
    }
};

int main() {
    int n;
    cin >> n;

    Solution solution;
    for (int i = 0; i < n; i++) {
        string word;
        int freq, time;
        cin >> word >> freq >> time;
        solution.insertWord(word, freq, time);
    }

    string prefix;
    int currentTime, D, k;
    cin >> prefix >> currentTime >> D >> k;

    vector<string> result = solution.autocomplete(prefix, currentTime, D, k);

    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << "\"" << result[i] << "\"";
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]" << endl;

    return 0;
}
