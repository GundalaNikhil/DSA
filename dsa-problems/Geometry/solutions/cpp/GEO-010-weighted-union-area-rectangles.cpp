#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <unordered_map>
using namespace std;

long long weightedArea(const vector<long long>& x1, const vector<long long>& y1,
                       const vector<long long>& x2, const vector<long long>& y2,
                       const vector<long long>& w, long long W) {
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
    int m = (int)ys.size() - 1;
    if (m <= 0) return 0;

    vector<long long> widths(m);
    for (int i = 0; i < m; ++i) widths[i] = ys[i + 1] - ys[i];
    unordered_map<long long, int> ymap;
    ymap.reserve(ys.size() * 2);
    for (int i = 0; i < (int)ys.size(); ++i) ymap[ys[i]] = i;

    struct Event { long long x; int type; long long y1; long long y2; long long w; };
    vector<Event> events;
    events.reserve(2 * n);
    for (int i = 0; i < n; ++i) {
        events.push_back({x1[i], 1, y1[i], y2[i], w[i]});
        events.push_back({x2[i], -1, y1[i], y2[i], w[i]});
    }
    sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type < b.type;
    });

    vector<long long> curr_weights(m, 0);
    long long total_area = 0;
    long long prev_x = events[0].x;
    for (int i = 0; i < (int)events.size(); ++i) {
        const auto& e = events[i];
        if (i > 0) {
            long long width = e.x - prev_x;
            if (width > 0) {
                long long covered = 0;
                for (int j = 0; j < m; ++j) {
                    if (curr_weights[j] >= W) covered += widths[j];
                }
                total_area += covered * width;
            }
        }
        int l = ymap[e.y1];
        int r = ymap[e.y2];
        long long delta = e.w * e.type;
        for (int j = l; j < r; ++j) curr_weights[j] += delta;
        prev_x = e.x;
    }
    return total_area;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m, W; cin >> m >> W;
    vector<long long> x1(m), y1(m), x2(m), y2(m), w(m);
    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i] >> w[i];
    cout << weightedArea(x1, y1, x2, y2, w, W) << endl;
    return 0;
}
