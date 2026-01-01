#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Seg {
    long long x1, y1, x2, y2;
};

int orient(long long ax, long long ay, long long bx, long long by, long long cx, long long cy) {
    long long v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
    if (v == 0) return 0;
    return (v > 0) ? 1 : -1;
}

bool onSeg(long long ax, long long ay, long long bx, long long by, long long cx, long long cy) {
    return min(ax, bx) <= cx && cx <= max(ax, bx) &&
           min(ay, by) <= cy && cy <= max(ay, by);
}

bool intersects(const Seg& s, const Seg& t) {
    int o1 = orient(s.x1, s.y1, s.x2, s.y2, t.x1, t.y1);
    int o2 = orient(s.x1, s.y1, s.x2, s.y2, t.x2, t.y2);
    int o3 = orient(t.x1, t.y1, t.x2, t.y2, s.x1, s.y1);
    int o4 = orient(t.x1, t.y1, t.x2, t.y2, s.x2, s.y2);

    if (((o1 > 0 && o2 < 0) || (o1 < 0 && o2 > 0)) &&
        ((o3 > 0 && o4 < 0) || (o3 < 0 && o4 > 0))) return true;

    if (o1 == 0 && onSeg(s.x1, s.y1, s.x2, s.y2, t.x1, t.y1)) return true;
    if (o2 == 0 && onSeg(s.x1, s.y1, s.x2, s.y2, t.x2, t.y2)) return true;
    if (o3 == 0 && onSeg(t.x1, t.y1, t.x2, t.y2, s.x1, s.y1)) return true;
    if (o4 == 0 && onSeg(t.x1, t.y1, t.x2, t.y2, s.x2, s.y2)) return true;

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Seg> segs(n);
    for (int i = 0; i < n; i++) {
        cin >> segs[i].x1 >> segs[i].y1 >> segs[i].x2 >> segs[i].y2;
    }

    long long count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (intersects(segs[i], segs[j])) count++;
        }
    }

    cout << count << endl;

    return 0;
}
