#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimalRotationIndex(const string& s) {
        int n = s.length();
        if (n == 0) return 0;
        string text = s + s;
        int m = text.length();
        
        vector<int> sa(m), rank(m), newRank(m);
        for (int i = 0; i < m; i++) {
            sa[i] = i;
            rank[i] = text[i];
        }
        
        for (int k = 1; k < m; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < m) ? rank[i + k] : -1;
                int rj = (j + k < m) ? rank[j + k] : -1;
                return ri < rj;
            };
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < m; i++) {
                if (cmp(sa[i - 1], sa[i])) newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                else newRank[sa[i]] = newRank[sa[i - 1]];
            }
            rank = newRank;
            if (rank[sa[m - 1]] == m - 1) break;
        }
        
        for (int i = 0; i < m; i++) {
            if (sa[i] < n) return sa[i];
        }
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.minimalRotationIndex(s) << "\n";
    }
    return 0;
}
