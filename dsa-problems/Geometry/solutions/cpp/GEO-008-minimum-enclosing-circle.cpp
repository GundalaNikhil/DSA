#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <iomanip>

using namespace std;

struct Point {
    double x, y;
};

struct Circle {
    double x, y, r;
};

class Solution {
    double dist(Point a, Point b) {
        return hypot(a.x - b.x, a.y - b.y);
    }

    Circle fromTwo(Point a, Point b) {
        Point center = {(a.x + b.x) / 2.0, (a.y + b.y) / 2.0};
        return {center.x, center.y, dist(a, b) / 2.0};
    }

    Circle fromThree(Point a, Point b, Point c) {
        double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
        if (abs(d) < 1e-15) return {0, 0, -1};
        double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
        double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
        return {ux, uy, dist({ux, uy}, a)};
    }

    bool inside(Point p, Circle c) {
        return dist(p, {c.x, c.y}) <= c.r + 1e-12;
    }

public:
    vector<double> minEnclosingCircle(vector<int>& xs, vector<int>& ys) {
        int n = xs.size();
        vector<Point> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {(double)xs[i], (double)ys[i]};
        
        random_device rd;
        mt19937 g(rd());
        shuffle(pts.begin(), pts.end(), g);

        Circle c = {pts[0].x, pts[0].y, 0};

        for (int i = 1; i < n; i++) {
            if (inside(pts[i], c)) continue;
            c = {pts[i].x, pts[i].y, 0};
            for (int j = 0; j < i; j++) {
                if (inside(pts[j], c)) continue;
                c = fromTwo(pts[i], pts[j]);
                for (int k = 0; k < j; k++) {
                    if (inside(pts[k], c)) continue;
                    c = fromThree(pts[i], pts[j], pts[k]);
                }
            }
        }
        return {c.x, c.y, c.r};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> xs(n), ys(n);
    for(int i=0; i<n; ++i) cin >> xs[i];
    for(int i=0; i<n; ++i) cin >> ys[i];
    
    Solution sol;
    vector<double> res = sol.minEnclosingCircle(xs, ys);
    
    cout << fixed << setprecision(6) << res[0] << " " << res[1] << " " << res[2] << "\n";
    
    return 0;
}
