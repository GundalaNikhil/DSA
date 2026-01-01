#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;


using namespace std;

vector<pair<long long,long long>> sortByAngle(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    vector<pair<long long,long long>> pts(n);
    for (int i = 0; i < n; ++i) pts[i] = {xs[i], ys[i]};
    auto half = [](const pair<long long,long long>& p) {
        return (p.second > 0 || (p.second == 0 && p.first > 0)) ? 0 : 1;
    };
    sort(pts.begin(), pts.end(), [&](auto &a, auto &b){
        int ha = half(a), hb = half(b);
        if (ha != hb) return ha < hb;
        long long cross = a.first * b.second - a.second * b.first;
        if (cross != 0) return cross > 0;
        long long ra = a.first * a.first + a.second * a.second;
        long long rb = b.first * b.first + b.second * b.second;
        return ra < rb;
    });
    return pts;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    auto res = sortByAngle(xs, ys);
    for(auto p : res) cout << p.first << " " << p.second << endl;
    return 0;
}
