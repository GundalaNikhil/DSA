#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <random>

using namespace std;

struct Point {
    double x, y;
};

struct Circle {
    double x, y, r;
};

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

Circle circleTwo(Point a, Point b) {
    Point c = {(a.x + b.x) / 2.0, (a.y + b.y) / 2.0};
    return {c.x, c.y, dist(a, b) / 2.0};
}

Circle circleThree(Point a, Point b, Point c) {
    double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
    if (abs(d) < 1e-9) return {0, 0, -1}; // Invalid
    double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
    double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
    return {ux, uy, dist({ux, uy}, a)};
}

bool inside(Point p, Circle c) {
    return dist(p, {c.x, c.y}) <= c.r + 1e-9;
}

Circle minEnclosingCircle(vector<Point>& pts) {
    if (pts.empty()) return {0, 0, 0};
    if (pts.size() == 1) return {pts[0].x, pts[0].y, 0};

    // Shuffle points
    mt19937 rng(1337);
    shuffle(pts.begin(), pts.end(), rng);

    Circle c = {pts[0].x, pts[0].y, 0};

    for (int i = 1; i < pts.size(); ++i) {
        if (inside(pts[i], c)) continue;
        c = {pts[i].x, pts[i].y, 0};
        for (int j = 0; j < i; ++j) {
            if (inside(pts[j], c)) continue;
            c = circleTwo(pts[i], pts[j]);
            for (int k = 0; k < j; ++k) {
                if (inside(pts[k], c)) continue;
                c = circleThree(pts[i], pts[j], pts[k]);
            }
        }
    }
    return c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> xs(n), ys(n);
    // Correct input parsing: Python reads xs then ys interleaved?
    // Wait, the Python code:
    // for _ in range(n): xs.append(int(next(it))); ys.append(int(next(it)))
    // So inputs are X1 Y1 X2 Y2 ...
    // My C++ fixes batch script fixed input parsing for GEO-008 to be interleaved.
    // I should maintain that.
    
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
    }

    Circle c = minEnclosingCircle(pts);

    cout << fixed << setprecision(6);
    if (abs(c.r) < 1e-9) c.r = 0.0;
    if (abs(c.x) < 1e-9) c.x = 0.0;
    if (abs(c.y) < 1e-9) c.y = 0.0;

    cout << c.x << "\n" << c.y << "\n" << c.r << "\n";

    return 0;
}
