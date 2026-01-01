#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <set>

using namespace std;

typedef long double ld;

struct Point {
    ld x, y;
};

ld getRadius(ld x, ld y, int xL, int yB, int xR, int yT, int n, const vector<int>& xs, const vector<int>& ys, const vector<int>& rs) {
    ld r = min({x - (ld)xL, (ld)xR - x, y - (ld)yB, (ld)yT - y});
    if (r <= 0) return 0.0;
    for (int i = 0; i < n; i++) {
        ld dx = x - (ld)xs[i];
        ld dy = y - (ld)ys[i];
        ld d = sqrt(dx * dx + dy * dy);
        r = min(r, d - (ld)rs[i]);
        if (r <= 0) return 0.0;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int xL, yB, xR, yT, n;
    if (!(cin >> xL >> yB >> xR >> yT >> n)) return 0;
    
    vector<int> xs(n), ys(n), rs(n);
    for (int i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i] >> rs[i];
    }
    
    struct Candidate {
        ld x, y, r;
        bool operator>(const Candidate& other) const {
            return r > other.r;
        }
    };
    
    vector<Candidate> cands;
    int gridRes = 120;
    for (int i = 0; i <= gridRes; i++) {
        ld cx = xL + (ld)(xR - xL) * i / (ld)gridRes;
        for (int j = 0; j <= gridRes; j++) {
            ld cy = yB + (ld)(yT - yB) * j / (ld)gridRes;
            ld r = getRadius(cx, cy, xL, yB, xR, yT, n, xs, ys, rs);
            if (r > 0) cands.push_back({cx, cy, r});
        }
    }
    
    for (int i = 0; i < n; i++) {
        cands.push_back({(ld)xs[i], (ld)yB, getRadius(xs[i], yB, xL, yB, xR, yT, n, xs, ys, rs)});
        cands.push_back({(ld)xs[i], (ld)yT, getRadius(xs[i], yT, xL, yB, xR, yT, n, xs, ys, rs)});
        cands.push_back({(ld)xL, (ld)ys[i], getRadius(xL, ys[i], xL, yB, xR, yT, n, xs, ys, rs)});
        cands.push_back({(ld)xR, (ld)ys[i], getRadius(xR, ys[i], xL, yB, xR, yT, n, xs, ys, rs)});
        for (int j = i + 1; j < n; j++) {
            ld mx = (xs[i] + xs[j]) / 2.0L;
            ld my = (ys[i] + ys[j]) / 2.0L;
            cands.push_back({mx, my, getRadius(mx, my, xL, yB, xR, yT, n, xs, ys, rs)});
        }
    }
    
    ld bestR = 0.0;
    if (cands.empty()) {
        bestR = max(bestR, getRadius((xL + xR) / 2.0L, (yB + yT) / 2.0L, xL, yB, xR, yT, n, xs, ys, rs));
    } else {
        sort(cands.begin(), cands.end(), greater<Candidate>());
        int count = 0;
        set<pair<long long, long long>> seen;
        for (const auto& cand : cands) {
            if (count >= 60) break;
            pair<long long, long long> key = {round((double)cand.x * 10), round((double)cand.y * 10)};
            if (seen.count(key)) continue;
            seen.insert(key);
            count++;
            
            ld currX = cand.x, currY = cand.y, currR = cand.r;
            ld step = max((ld)(xR - xL), (ld)(yT - yB)) / (ld)gridRes;
            while (step > 1e-13L) {
                bool improved = false;
                ld dirs[10][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {0.7,0.7}, {0.7,-0.7}, {-0.7,0.7}, {-0.7,-0.7}, {0.3,0.9}, {0.9,0.3}};
                for (int i = 0; i < 10; i++) {
                    ld nx = currX + dirs[i][0] * step, ny = currY + dirs[i][1] * step;
                    if (nx >= xL && nx <= xR && ny >= yB && ny <= yT) {
                        ld nr = getRadius(nx, ny, xL, yB, xR, yT, n, xs, ys, rs);
                        if (nr > currR) {
                            currR = nr; currX = nx; currY = ny;
                            improved = true;
                        }
                    }
                }
                if (!improved) step *= 0.5L;
            }
            bestR = max(bestR, currR);
        }
    }
    cout << fixed << setprecision(6) << (double)max(0.0L, bestR) << endl;
    return 0;
}
