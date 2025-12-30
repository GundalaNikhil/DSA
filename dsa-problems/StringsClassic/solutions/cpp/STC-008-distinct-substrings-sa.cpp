#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countDistinct(const string& s) {
        int n = s.length();
        if (n == 0) return 0;
        
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
        
        // 2. Build LCP Sum
        long long lcpSum = 0;
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
            lcpSum += k;
            if (k > 0) k--;
        }
        
        long long totalSubstrings = (long long)n * (n + 1) / 2;
        return totalSubstrings - lcpSum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.countDistinct(s) << "\n";
    }
    return 0;
}
