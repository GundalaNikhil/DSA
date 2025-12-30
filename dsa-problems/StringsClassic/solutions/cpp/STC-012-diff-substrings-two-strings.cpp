#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countExclusiveSubstrings(const string& a, const string& b) {
        string s = a + "#" + b;
        int n = s.length();
        int splitIdx = a.length();
        
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
        vector<int> lcp(n);
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == 0) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] - 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Max Match B
        vector<int> maxMatchB(n, 0);
        
        // Forward
        int currentLCP = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0) currentLCP = min(currentLCP, lcp[i]);
            if (sa[i] > splitIdx) {
                currentLCP = n;
            } else if (sa[i] < splitIdx) {
                maxMatchB[i] = max(maxMatchB[i], currentLCP);
            }
        }
        
        // Backward
        currentLCP = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1) currentLCP = min(currentLCP, lcp[i + 1]);
            if (sa[i] > splitIdx) {
                currentLCP = n;
            } else if (sa[i] < splitIdx) {
                maxMatchB[i] = max(maxMatchB[i], currentLCP);
            }
        }
        
        // 4. Count
        long long count = 0;
        int prevALCP = 0;
        
        for (int i = 0; i < n; i++) {
            if (i > 0) prevALCP = min(prevALCP, lcp[i]);
            
            if (sa[i] < splitIdx) {
                int len = splitIdx - sa[i];
                int deduct = max(prevALCP, maxMatchB[i]);
                if (len > deduct) {
                    count += (len - deduct);
                }
                prevALCP = n;
            }
        }
        
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (cin >> a >> b) {
        Solution solution;
        cout << solution.countExclusiveSubstrings(a, b) << "\n";
    }
    return 0;
}
