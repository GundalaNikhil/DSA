#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Point {
    long long x, y;
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

long long cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    int theta;
    cin >> theta;

    // Remove duplicates
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());

    if (pts.size() <= 1) {
        if (pts.empty()) cout << "0\n";
        else cout << "1\n" << pts[0].x << " " << pts[0].y << "\n";
        return 0;
    }

    // Monotone Chain
    vector<Point> lower, upper;
    for (const auto& p : pts) {
        while (lower.size() >= 2 && cross(lower[lower.size()-2], lower.back(), p) <= 0) {
            lower.pop_back();
        }
        lower.push_back(p);
    }
    for (int i = pts.size() - 1; i >= 0; i--) {
        const auto& p = pts[i];
        while (upper.size() >= 2 && cross(upper[upper.size()-2], upper.back(), p) <= 0) {
            upper.pop_back();
        }
        upper.push_back(p);
    }

    vector<Point> hull = lower;
    hull.pop_back();
    hull.insert(hull.end(), upper.begin(), upper.end());
    hull.pop_back();

    if (hull.size() <= 2) {
        cout << hull.size() << "\n";
        for (const auto& p : hull) cout << p.x << " " << p.y << "\n";
        return 0;
    }

    long long h = hull.size();
    double cosT = cos(theta * M_PI / 180.0);
    vector<Point> keep;

    for (int i = 0; i < h; ++i) {
        Point prev = hull[(i - 1 + h) % h];
        Point curr = hull[i];
        Point nxt = hull[(i + 1) % h];

        double ux = (double)prev.x - curr.x;
        double uy = (double)prev.y - curr.y;
        double vx = (double)nxt.x - curr.x;
        double vy = (double)nxt.y - curr.y;

        double lenU = hypot(ux, uy);
        double lenV = hypot(vx, vy);

        if (lenU == 0 || lenV == 0) {
            keep.push_back(curr);
            continue;
        }

        double dot = ux * vx + uy * vy;
        double cosA = dot / (lenU * lenV); // Note: Python logic: cosA = dot / ...
        
        // Wait, Python logic:
        // ux, uy vector from curr to prev? No: prev - curr. So vector CP.
        // vx, vy vector from curr to nxt? No: nxt - curr. So vector CN.
        // Angle at C is angle betwen CP and CN.
        // dot = |CP||CN|cos(angle)
        // Check my previous C++ implementation (step 271) used cosA = -dot / ... ?
        // Python code (step 270):
        // ux, uy = prev[0]-curr[0], prev[1]-curr[1]  -> Vector CP
        // vx, vy = nxt[0]-curr[0], nxt[1]-curr[1]    -> Vector CN
        // dot = ux*vx + uy*vy
        // cosA = dot / (lenU*lenV)
        // if cosA <= cosT: keep
        // This is correct. My previous C++ at 271 had `cosA = -dot` which was probably wrong.
        
        if (cosA <= cosT + 1e-9) { // strict inequality + epsilon for safety
            keep.push_back(curr);
        }
    }

    cout << keep.size() << "\n";
    for (const auto& p : keep) {
        cout << p.x << " " << p.y << "\n";
    }

    return 0;
}
