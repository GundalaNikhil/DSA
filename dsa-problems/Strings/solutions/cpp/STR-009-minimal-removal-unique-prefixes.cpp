struct TrieNode {
    unordered_map<char, TrieNode*> children;
    vector<string> strings;
};

class Solution {
public:
    int minimalRemovalUniquePrefixes(int L, vector<string>& strings) {
        TrieNode* root = new TrieNode();

        // Build trie
        for (const string& s : strings) {
            TrieNode* node = root;
            for (int i = 0; i < min((int)s.size(), L); i++) {
                char c = s[i];
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->strings.push_back(s);
        }

        // Find conflicts
        int totalDeletions = 0;
        findConflicts(root, 0, L, totalDeletions);
        return totalDeletions;
    }

private:
    void findConflicts(TrieNode* node, int depth, int L, int& totalDeletions) {
        if (depth == L) {
            if (node->strings.size() > 1) {
                // Sort by length descending
                sort(node->strings.begin(), node->strings.end(),
                     [](const string& a, const string& b) {
                         return a.size() > b.size();
                     });

                // Delete all except longest
                for (int i = 1; i < node->strings.size(); i++) {
                    const string& s = node->strings[i];
                    if ((int)s.size() >= L) {
                        totalDeletions += s.size() - (L - 1);
                    }
                }
            }
            return;
        }

        for (auto& [c, child] : node->children) {
            findConflicts(child, depth + 1, L, totalDeletions);
        }
    }
};
