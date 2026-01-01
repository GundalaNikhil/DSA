#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>

using namespace std;

struct Point {
    int x, y, id;
};

struct Edge {
    long long w;
    int u, v;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

class DSU {
    vector<int> parent;
public:
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
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

class Solution {
    void add_edges(vector<Point>& pts, vector<Edge>& edges) {
        sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
            if (a.x != b.x) return a.x < b.x;
            return a.y < b.y;
        });
        
        vector<int> diffs;
        for(auto& p : pts) diffs.push_back(p.y - p.x);
        sort(diffs.begin(), diffs.end());
        diffs.erase(unique(diffs.begin(), diffs.end()), diffs.end());
        
        auto get_idx = [&](int val) {
            return lower_bound(diffs.begin(), diffs.end(), val) - diffs.begin() + 1;
        };
        
        int m = diffs.size();
        vector<pair<int, int>> bit(m + 1, {-2000000000, -1}); // max val, id
        
        auto update = [&](int idx, int val, int id) {
            for (; idx > 0; idx -= idx & -idx) {
                if (val > bit[idx].first) bit[idx] = {val, id};
            }
        };
        
        auto query = [&](int idx) {
            pair<int, int> res = {-2000000000, -1};
            for (; idx <= m; idx += idx & -idx) {
                if (bit[idx].first > res.first) res = bit[idx];
            }
            return res;
        };
        
        for (int i = 0; i < pts.size(); ++i) {
            auto& p = pts[i];
            int key = p.y - p.x;
            int idx = get_idx(key);
            pair<int, int> res = query(idx);
            if (res.second != -1) {
                // res.second is index in current sorted pts array
                auto& q = pts[res.second];
                long long w = abs(p.x - q.x) + abs(p.y - q.y);
                edges.push_back({w, p.id, q.id});
            }
            update(idx, p.x + p.y, i);
        }
    }

public:
    long long manhattanMST(vector<int>& xs, vector<int>& ys) {
        int n = xs.size();
        vector<Point> pts(n);
        for(int i=0; i<n; ++i) pts[i] = {xs[i], ys[i], i};
        
        vector<Edge> edges;
        
        // 4 sweeps
        for(int k=0; k<4; ++k) {
            add_edges(pts, edges);
            // Rotate 90 degrees: (x, y) -> (y, -x)
            for(auto& p : pts) {
                int tmp = p.x;
                p.x = p.y;
                p.y = -tmp;
            }
        }
        
        sort(edges.begin(), edges.end());
        
        DSU dsu(n);
        long long mst_weight = 0;
        int edges_count = 0;
        
        for(const auto& e : edges) {
            if(dsu.unite(e.u, e.v)) {
                mst_weight += e.w;
                edges_count++;
            }
        }
        
        return mst_weight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> xs(n), ys(n);
    for(int i=0; i<n; ++i) {
        cin >> xs[i] >> ys[i];
    }
    
    Solution sol;
    cout << sol.manhattanMST(xs, ys) << "\n";
    
    return 0;
}
