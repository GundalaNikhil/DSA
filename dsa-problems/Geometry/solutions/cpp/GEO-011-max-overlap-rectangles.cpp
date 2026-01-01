#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <unordered_map>
#include <functional>
using namespace std;

// Same sweep; compress ys; segment tree supports range add and tracks max at root.

long long maxOverlap(const vector<long long>& x1, const vector<long long>& y1,
                     const vector<long long>& x2, const vector<long long>& y2) {
    int n = x1.size();
    if (n == 0) return 0;
    vector<long long> ys;
    ys.reserve(2 * n);
    for (int i = 0; i < n; ++i) {
        ys.push_back(y1[i]);
        ys.push_back(y2[i]);
    }
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    int m = ys.size();
    if (m == 0) return 0;
    unordered_map<long long, int> ymap;
    ymap.reserve(ys.size() * 2);
    for (int i = 0; i < (int)ys.size(); ++i) ymap[ys[i]] = i;

    struct Event { long long x; int type; int l; int r; };
    vector<Event> events;
    events.reserve(2 * n);
    for (int i = 0; i < n; ++i) {
        int l = ymap[y1[i]];
        int r = ymap[y2[i]] + 1;
        events.push_back({x1[i], -1, l, r});
        events.push_back({x2[i], 1, l, r});
    }
    sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type < b.type;
    });

    vector<int> add(4 * m, 0);
    vector<int> mx(4 * m, 0);

    function<void(int,int,int,int,int,int)> update = [&](int node, int l, int r, int ql, int qr, int val) {
        if (qr <= l || r <= ql) return;
        if (ql <= l && r <= qr) {
            int real_val = -val;
            add[node] += real_val;
            mx[node] += real_val;
            return;
        }
        int mid = (l + r) / 2;
        update(node * 2, l, mid, ql, qr, val);
        update(node * 2 + 1, mid, r, ql, qr, val);
        mx[node] = add[node] + max(mx[node * 2], mx[node * 2 + 1]);
    };

    int ans = 0;
    for (const auto& e : events) {
        update(1, 0, m, e.l, e.r, e.type);
        ans = max(ans, mx[1]);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m; cin >> m;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    cout << maxOverlap(x1, y1, x2, y2) << endl;
    return 0;
}
