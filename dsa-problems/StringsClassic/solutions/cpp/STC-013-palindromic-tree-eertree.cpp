#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

struct Node {
    int len;
    int link;
    map<char, int> next;
    
    Node(int l = 0, int lnk = 0) : len(l), link(lnk) {}
};

class Solution {
public:
    int countDistinctPalindromes(const string& s) {
        vector<Node> tree;
        tree.emplace_back(-1, 0); // Node 0: odd root
        tree.emplace_back(0, 0);  // Node 1: even root
        
        int last = 1;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            char c = s[i];
            int curr = last;
            
            while (true) {
                int len = tree[curr].len;
                if (i - 1 - len >= 0 && s[i - 1 - len] == c) {
                    break;
                }
                curr = tree[curr].link;
            }
            
            if (tree[curr].next.count(c)) {
                last = tree[curr].next[c];
                continue;
            }
            
            int newNodeIdx = tree.size();
            tree.emplace_back(tree[curr].len + 2, 0);
            tree[curr].next[c] = newNodeIdx;
            
            if (tree[newNodeIdx].len == 1) {
                tree[newNodeIdx].link = 1;
            } else {
                int temp = tree[curr].link;
                while (true) {
                    int len = tree[temp].len;
                    if (i - 1 - len >= 0 && s[i - 1 - len] == c) {
                        break;
                    }
                    temp = tree[temp].link;
                }
                tree[newNodeIdx].link = tree[temp].next[c];
            }
            
            last = newNodeIdx;
        }
        
        return tree.size() - 2;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.countDistinctPalindromes(s) << "\n";
    }
    return 0;
}
