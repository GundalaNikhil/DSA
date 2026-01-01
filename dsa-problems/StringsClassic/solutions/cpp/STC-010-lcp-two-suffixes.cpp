#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    vector<int> rank;
    vector<vector<int>> st;
    vector<int> logs;

public:
    vector<int> lcpQueries(const string& s, const vector<pair<int, int>>& queries) {
        int n = s.length();
        if (n == 0) return vector<int>(queries.size(), 0);
        
        // Build SA
        vector<int> sa(n), newRank(n);
        rank.resize(n);
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
        
        // Build LCP
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
        
        // Build Sparse Table
        int m = lcp.size();
        if (m > 0) {
            logs.resize(m + 1);
            logs[1] = 0;
            for (int i = 2; i <= m; i++) logs[i] = logs[i / 2] + 1;
            
            int K = logs[m];
            st.assign(K + 1, vector<int>(m));
            for (int i = 0; i < m; i++) st[0][i] = lcp[i];
            
            for (int j = 1; j <= K; j++) {
                for (int i = 0; i + (1 << j) <= m; i++) {
                    st[j][i] = min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
                }
            }
        }
        
        vector<int> ans;
        for (auto& q : queries) {
            int i = q.first;
            int j = q.second;
            if (i == j) {
                ans.push_back(n - i);
            } else {
                int r1 = rank[i];
                int r2 = rank[j];
                if (r1 > r2) swap(r1, r2);
                
                if (m == 0) ans.push_back(0);
                else {
                    int L = r1;
                    int R = r2 - 1;
                    int lg = logs[R - L + 1];
                    ans.push_back(min(st[lg][L], st[lg][R - (1 << lg) + 1]));
                }
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        vector<pair<int, int>> queries;
        int i, j;
        while (cin >> i >> j) {
            queries.push_back({i, j});
        }

        Solution solution;
        vector<int> ans = solution.lcpQueries(s, queries);
        for (int x : ans) cout << x << "\n";
    }
    return 0;
}
