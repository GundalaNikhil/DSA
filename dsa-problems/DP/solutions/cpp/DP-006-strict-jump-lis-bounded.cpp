#include <bits/stdc++.h>
using namespace std;

struct SegTree {
    int n;
    vector<int> t;
    SegTree(int n): n(n), t(4*n, 0) {}
    void update(int idx, int val) { update(1, 0, n-1, idx, val); }
    void update(int node, int l, int r, int idx, int val) {
        if (l==r) { t[node]=max(t[node], val); return; }
        int mid=(l+r)/2;
        if (idx<=mid) update(node*2, l, mid, idx, val);
        else update(node*2+1, mid+1, r, idx, val);
        t[node]=max(t[node*2], t[node*2+1]);
    }
    int query(int ql, int qr) {
        if (ql>qr) return 0;
        return query(1, 0, n-1, ql, qr);
    }
    int query(int node, int l, int r, int ql, int qr) {
        if (qr<l || r<ql) return 0;
        if (ql<=l && r<=qr) return t[node];
        int mid=(l+r)/2;
        return max(query(node*2, l, mid, ql, qr), query(node*2+1, mid+1, r, ql, qr));
    }
};

class Solution {
public:
    int longestBoundedDiffSubsequence(const vector<long long>& a, long long d, long long g) {
        vector<long long> vals = a;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());

        SegTree st((int)vals.size());
        int ans = 1;

        for (long long x : a) {
            long long lo = x - g;
            long long hi = x - d;
            int L = (int)(lower_bound(vals.begin(), vals.end(), lo) - vals.begin());
            int R = (int)(upper_bound(vals.begin(), vals.end(), hi) - vals.begin()) - 1;
            int best = st.query(L, R);
            int dp = best + 1;
            int idx = (int)(lower_bound(vals.begin(), vals.end(), x) - vals.begin());
            st.update(idx, dp);
            ans = max(ans, dp);
        }
        return ans;
    }
};
