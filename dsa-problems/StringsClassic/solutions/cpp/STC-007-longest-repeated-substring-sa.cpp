#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestRepeated(const string& s) {
        int n = s.length();
        if (n == 0) return "NONE";
        
        // 1. Build SA
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
                if (cmp(sa[i - 1], sa[i])) newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                else newRank[sa[i]] = newRank[sa[i - 1]];
            }
            rank = newRank;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        // 2. Build LCP
        vector<int> lcp(n - 1);
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Find Max
        int maxLen = 0;
        int startIdx = -1;
        for (int i = 0; i < n - 1; i++) {
            if (lcp[i] > maxLen) {
                maxLen = lcp[i];
                startIdx = sa[i];
            }
        }
        
        if (maxLen == 0) return "NONE";
        return s.substr(startIdx, maxLen);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.longestRepeated(s) << "\n";
    }
    return 0;
}
