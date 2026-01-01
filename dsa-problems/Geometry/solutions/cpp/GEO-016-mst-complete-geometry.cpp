#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Point {
    int x, y, id;
};

struct Edge {
    int u, v;
    long long w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

struct BIT {
    int n;
    vector<long long> min_val;
    vector<int> id;
    BIT(int n) : n(n), min_val(n + 1, 4e18), id(n + 1, -1) {}
    void update(int i, long long val, int p_id) {
        for (; i > 0; i -= i & -i) {
            if (val < min_val[i]) {
                min_val[i] = val;
                id[i] = p_id;
            }
        }
    }
    int query(int i) {
        long long res_val = 4e18;
        int res_id = -1;
        for (; i <= n; i += i & -i) {
            if (min_val[i] < res_val) {
                res_val = min_val[i];
                res_id = id[i];
            }
        }
        return res_id;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        return parent[i] == i ? i : parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 1) {
        cout << 0 << endl;
        return 0;
    }

    vector<Point> pts(n);
    for (int i = 0; i < n; i++) {
        cin >> pts[i].x >> pts[i].y;
        pts[i].id = i;
    }

    vector<Edge> edges;
    for (int s1 = 0; s1 < 2; s1++) {
        for (int s2 = 0; s2 < 2; s2++) {
            for (int sw = 0; sw < 2; sw++) {
                sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
                    return a.x != b.x ? a.x > b.x : a.y > b.y;
                });
                
                vector<int> ys(n);
                for (int i = 0; i < n; i++) ys[i] = pts[i].y - pts[i].x;
                vector<int> sorted_ys = ys;
                sort(sorted_ys.begin(), sorted_ys.end());
                sorted_ys.erase(unique(sorted_ys.begin(), sorted_ys.end()), sorted_ys.end());
                
                int m = sorted_ys.size();
                BIT bit(m);
                for (int i = 0; i < n; i++) {
                    int pos = lower_bound(sorted_ys.begin(), sorted_ys.end(), ys[i]) - sorted_ys.begin() + 1;
                    int idx = bit.query(pos);
                    if (idx != -1) {
                        long long d = abs((long long)pts[i].x - pts[idx].x) + abs((long long)pts[i].y - pts[idx].y);
                        edges.push_back({pts[i].id, pts[idx].id, d});
                    }
                    bit.update(pos, (long long)pts[i].x + pts[i].y, i);
                }

                for (auto& p : pts) swap(p.x, p.y);
            }
            for (auto& p : pts) p.y = -p.y;
        }
        for (auto& p : pts) p.x = -p.x;
    }

    sort(edges.begin(), edges.end());
    DSU dsu(n);
    long long mst = 0;
    int count = 0;
    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst += e.w;
            if (++count == n - 1) break;
        }
    }
    cout << mst << endl;

    return 0;
}
