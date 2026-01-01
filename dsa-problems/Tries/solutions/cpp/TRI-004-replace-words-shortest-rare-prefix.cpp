#include <iostream>
#include <unordered_map>
#include <sstream>
#include <string>
#include <climits>
#include <limits>

using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    string word;
    int rarity;

    TrieNode() : word(""), rarity(INT_MAX) {}
};

class Solution {
public:
    string replaceWords(unordered_map<string, int>& dictionary, const string& sentence) {
        root = new TrieNode();
        for (const auto& entry : dictionary) {
            insert(entry.first, entry.second);
        }

        istringstream iss(sentence);
        string token;
        string result;
        bool first = true;
        while (iss >> token) {
            if (!first) {
                result.push_back(' ');
            }
            first = false;
            result += findReplacement(token);
        }
        return result;
    }

private:
    TrieNode* root = nullptr;

    void insert(const string& word, int rarity) {
        TrieNode* curr = root;
        for (char c : word) {
            auto it = curr->children.find(c);
            if (it == curr->children.end()) {
                TrieNode* next = new TrieNode();
                curr->children[c] = next;
                curr = next;
            } else {
                curr = it->second;
            }
        }

        if (rarity < curr->rarity ||
            (rarity == curr->rarity && (curr->word.empty() || word.size() < curr->word.size()))) {
            curr->word = word;
            curr->rarity = rarity;
        }
    }

    string findReplacement(const string& word) {
        TrieNode* curr = root;
        string best;
        int bestRarity = INT_MAX;

        for (char c : word) {
            auto it = curr->children.find(c);
            if (it == curr->children.end()) {
                break;
            }
            curr = it->second;
            if (!curr->word.empty()) {
                if (curr->rarity < bestRarity ||
                    (curr->rarity == bestRarity && curr->word.size() < best.size())) {
                    best = curr->word;
                    bestRarity = curr->rarity;
                }
            }
        }

        return best.empty() ? word : best;
    }
};

int main() {
    int n;
    if (!(cin >> n)) {
        return 0;
    }

    unordered_map<string, int> dictionary;
    for (int i = 0; i < n; i++) {
        string root;
        int rarity;
        cin >> root >> rarity;
        dictionary[root] = rarity;
    }
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string sentence;
    getline(cin, sentence);

    Solution solution;
    string result = solution.replaceWords(dictionary, sentence);

    cout << result << '\n';
    return 0;
}
