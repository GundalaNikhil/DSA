#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Point {
    double x, y;
};

class Solution {
    double dist(Point p, Point q) {
        return hypot(p.x - q.x, p.y - q.y);
    }

    double distToEdge(Point p, int xL, int yB, int xR, int yT) {
        return min({p.x - xL, (double)xR - p.x, p.y - yB, (double)yT - p.y});
    }

    bool insideRect(Point p, int xL, int yB, int xR, int yT) {
        double EPS = 1e-12;
        return p.x >= xL - EPS && p.x <= xR + EPS && p.y >= yB - EPS && p.y <= yT + EPS;
    }

public:
    double largestEmptyCircle(int xL, int yB, int xR, int yT, vector<int>& xs, vector<int>& ys) {
        int n = xs.size();
        vector<Point> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {(double)xs[i], (double)ys[i]};

        vector<Point> candidates;
        // Corners
        candidates.push_back({(double)xL, (double)yB});
        candidates.push_back({(double)xL, (double)yT});
        candidates.push_back({(double)xR, (double)yB});
        candidates.push_back({(double)xR, (double)yT});

        // Edge projections
        for (const auto& p : pts) {
            candidates.push_back({p.x, (double)yB});
            candidates.push_back({p.x, (double)yT});
            candidates.push_back({(double)xL, p.y});
            candidates.push_back({(double)xR, p.y});
        }

        // Midpoints
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                candidates.push_back({(pts[i].x + pts[j].x) / 2.0, (pts[i].y + pts[j].y) / 2.0});
            }
        }

        // Circumcenters (small n)
        if (n <= 60) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        Point a = pts[i], b = pts[j], c = pts[k];
                        double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
                        if (abs(d) < 1e-12) continue;
                        double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
                        double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
                        candidates.push_back({ux, uy});
                    }
                }
            }
        }

        double best = 0.0;
        for (const auto& c : candidates) {
            if (!insideRect(c, xL, yB, xR, yT)) continue;
            double r = distToEdge(c, xL, yB, xR, yT);
            for (const auto& p : pts) {
                r = min(r, dist(c, p));
            }
            best = max(best, r);
        }
        return best;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int xL, yB, xR, yT;
    if (!(cin >> xL >> yB >> xR >> yT)) return 0;
    
    int n;
    cin >> n;
    
    vector<int> xs(n), ys(n);
    for(int i=0; i<n; ++i) cin >> xs[i];
    for(int i=0; i<n; ++i) cin >> ys[i];
    
    Solution sol;
    cout << fixed << setprecision(6) << sol.largestEmptyCircle(xL, yB, xR, yT, xs, ys) << "\n";
    
    return 0;
}
