#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    int orient(long long ax, long long ay, long long bx, long long by, long long cx, long long cy) {
        long long v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
        if (v > 0) return 1;
        if (v < 0) return -1;
        return 0;
    }

    bool onSeg(long long ax, long long ay, long long bx, long long by, long long cx, long long cy) {
        return orient(ax, ay, bx, by, cx, cy) == 0 &&
               min(ax, bx) <= cx && cx <= max(ax, bx) &&
               min(ay, by) <= cy && cy <= max(ay, by);
    }

    bool segInter(long long ax, long long ay, long long bx, long long by, long long cx, long long cy, long long dx, long long dy) {
        int o1 = orient(ax, ay, bx, by, cx, cy);
        int o2 = orient(ax, ay, bx, by, dx, dy);
        int o3 = orient(cx, cy, dx, dy, ax, ay);
        int o4 = orient(cx, cy, dx, dy, bx, by);

        if (o1 == 0 && onSeg(ax, ay, bx, by, cx, cy)) return true;
        if (o2 == 0 && onSeg(ax, ay, bx, by, dx, dy)) return true;
        if (o3 == 0 && onSeg(cx, cy, dx, dy, ax, ay)) return true;
        if (o4 == 0 && onSeg(cx, cy, dx, dy, bx, by)) return true;

        return o1 != o2 && o3 != o4;
    }

public:
    bool intersects(long long xL, long long yB, long long xR, long long yT, long long x1, long long y1, long long x2, long long y2) {
        bool inside1 = (xL <= x1 && x1 <= xR && yB <= y1 && y1 <= yT);
        bool inside2 = (xL <= x2 && x2 <= xR && yB <= y2 && y2 <= yT);
        if (inside1 || inside2) return true;

        long long edges[4][4] = {
            {xL, yB, xR, yB},
            {xR, yB, xR, yT},
            {xR, yT, xL, yT},
            {xL, yT, xL, yB}
        };

        for (int i = 0; i < 4; i++) {
            if (segInter(x1, y1, x2, y2, edges[i][0], edges[i][1], edges[i][2], edges[i][3])) return true;
        }

        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long xL, yB, xR, yT, x1, y1, x2, y2;
    if (cin >> xL >> yB >> xR >> yT >> x1 >> y1 >> x2 >> y2) {
        Solution sol;
        cout << (sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false") << "\n";
    }
    return 0;
}
