#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> suffixArray(const string& s) {
        int n = s.length();
        vector<int> sa(n), rank(n), newRank(n);
        
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s[i];
        }
        
        for (int k = 1; k < n; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < n) ? rank[i + k] : -1;
                int rj = (j + k < n) ? rank[j + k] : -1;
                return ri < rj;
            };
            
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                if (cmp(sa[i - 1], sa[i])) {
                    newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                } else {
                    newRank[sa[i]] = newRank[sa[i - 1]];
                }
            }
            rank = newRank;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        return sa;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        vector<int> sa = solution.suffixArray(s);
        for (int i = 0; i < (int)sa.size(); i++) {
            if (i > 0) cout << " ";
            cout << sa[i];
        }
        cout << "\n";
    }
    return 0;
}
