#include <bits/stdc++.h>
using namespace std;

long long dist2(const pair<long long,long long>& a, const pair<long long,long long>& b) {
    long long dx = a.first - b.first, dy = a.second - b.second;
    return dx*dx + dy*dy;
}

long long solve(vector<pair<long long,long long>>& pts) {
    int n = pts.size();
    if (n <= 3) {
        long long best = LLONG_MAX;
        for (int i = 0; i < n; ++i)
            for (int j = i+1; j < n; ++j)
                best = min(best, dist2(pts[i], pts[j]));
        sort(pts.begin(), pts.end(), [](auto &a, auto &b){ return a.second < b.second; });
        return best;
    }
    int mid = n/2;
    long long midx = pts[mid].first;
    vector<pair<long long,long long>> left(pts.begin(), pts.begin()+mid);
    vector<pair<long long,long long>> right(pts.begin()+mid, pts.end());
    long long d = min(solve(left), solve(right));
    merge(left.begin(), left.end(), right.begin(), right.end(), pts.begin(),
          [](auto &a, auto &b){ return a.second < b.second; });
    vector<pair<long long,long long>> strip;
    for (auto &p : pts) {
        long long dx = p.first - midx;
        if (dx*dx < d) strip.push_back(p);
    }
    for (int i = 0; i < (int)strip.size(); ++i) {
        for (int j = i+1; j < (int)strip.size() && j <= i+7; ++j) {
            long long dy = strip[j].second - strip[i].second;
            if (dy*dy >= d) break;
            d = min(d, dist2(strip[i], strip[j]));
        }
    }
    return d;
}

long long closestPair(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    vector<pair<long long,long long>> pts(n);
    for (int i = 0; i < n; ++i) pts[i] = {xs[i], ys[i]};
    sort(pts.begin(), pts.end());
    if (adjacent_find(pts.begin(), pts.end()) != pts.end()) return 0;
    return solve(pts);
}
