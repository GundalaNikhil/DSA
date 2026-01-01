#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <set>
using namespace std;


using namespace std;

struct Seg { long long x1,y1,x2,y2; };

int orient(const Seg& s, long long cx, long long cy) {
    long long v = (s.x2 - s.x1) * (cy - s.y1) - (s.y2 - s.y1) * (cx - s.x1);
    return (v>0) - (v<0);
}

bool onSeg(const Seg& s, long long cx, long long cy) {
    return orient(s, cx, cy) == 0 && min(s.x1, s.x2) <= cx && cx <= max(s.x1, s.x2)
                                && min(s.y1, s.y2) <= cy && cy <= max(s.y1, s.y2);
}

bool inter(const Seg& a, const Seg& b) {
    int o1 = orient(a, b.x1, b.y1), o2 = orient(a, b.x2, b.y2);
    int o3 = orient(b, a.x1, a.y1), o4 = orient(b, a.x2, a.y2);
    if (o1 == 0 && onSeg(a, b.x1, b.y1)) return true;
    if (o2 == 0 && onSeg(a, b.x2, b.y2)) return true;
    if (o3 == 0 && onSeg(b, a.x1, a.y1)) return true;
    if (o4 == 0 && onSeg(b, a.x2, a.y2)) return true;
    return (long long)o1 * o2 < 0 && (long long)o3 * o4 < 0;
}

long long countIntersections(const vector<long long>& x1, const vector<long long>& y1,
                             const vector<long long>& x2, const vector<long long>& y2) {
    int m = x1.size();
    vector<Seg> segs(m);
    for (int i = 0; i < m; ++i) {
        segs[i] = {x1[i], y1[i], x2[i], y2[i]};
        if (make_pair(segs[i].x1, segs[i].y1) > make_pair(segs[i].x2, segs[i].y2))
            swap(segs[i].x1, segs[i].x2), swap(segs[i].y1, segs[i].y2);
    }
    if (m <= 3000) {
        long long cnt = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = i + 1; j < m; ++j) {
                if (inter(segs[i], segs[j])) cnt++;
            }
        }
        return cnt;
    }

    struct Event { long long x; int type; int id; long long y; };
    vector<Event> evs; evs.reserve(2*m);
    for (int i = 0; i < m; ++i) {
        evs.push_back({segs[i].x1, 0, i, segs[i].y1});
        evs.push_back({segs[i].x2, 1, i, segs[i].y2});
    }
    sort(evs.begin(), evs.end(), [](const Event& a, const Event& b){
        if (a.x != b.x) return a.x < b.x;
        if (a.type != b.type) return a.type < b.type;
        return a.y < b.y;
    });

    auto yAt = [&](const Seg& s, long long x)->long double{
        if (s.x1 == s.x2) return min(s.y1, s.y2);
        return s.y1 + (long double)(s.y2 - s.y1) * (x - s.x1) / (long double)(s.x2 - s.x1);
    };

    long double curX = 0;
    struct Cmp {
        vector<Seg>* ps; long double* cx;
        bool operator()(int a, int b) const {
            if (a == b) return false;
            auto& sa = (*ps)[a]; auto& sb = (*ps)[b];
            long double ya = sa.x1==sa.x2 ? min(sa.y1, sa.y2) : sa.y1 + (long double)(sa.y2-sa.y1)*((*cx)-sa.x1)/(sa.x2-sa.x1);
            long double yb = sb.x1==sb.x2 ? min(sb.y1, sb.y2) : sb.y1 + (long double)(sb.y2-sb.y1)*((*cx)-sb.x1)/(sb.x2-sb.x1);
            if (ya == yb) return a < b;
            return ya < yb;
        }
    } cmp{&segs, &curX};

    set<int, Cmp> status(cmp);
    long long ans = 0;
    for (auto &e : evs) {
        curX = e.x;
        int id = e.id;
        if (e.type == 0) {
            auto it = status.insert(id).first;
            auto prev = it, next = it;
            if (it != status.begin()) { --prev; if (inter(segs[*prev], segs[id])) ans++; }
            ++next;
            if (next != status.end() && inter(segs[*next], segs[id])) ans++;
        } else {
            auto it = status.find(id);
            if (it != status.end()) {
                auto prev = it, next = it;
                bool hasPrev = (it != status.begin());
                if (hasPrev) --prev;
                ++next;
                if (hasPrev && next != status.end() && inter(segs[*prev], segs[*next])) ans++;
                status.erase(it);
            }
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m; cin >> m;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    cout << countIntersections(x1, y1, x2, y2) << endl;
    return 0;
}
