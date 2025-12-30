#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

class Solution {
public:
    long long cross(long long ox, long long oy, long long ax, long long ay, long long bx, long long by) {
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
    }

    vector<pair<int, int>> cappedHull(vector<int>& xs, vector<int>& ys, int theta) {
        int n = xs.size();
        vector<pair<long long, long long>> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {xs[i], ys[i]};
        
        sort(pts.begin(), pts.end());
        pts.erase(unique(pts.begin(), pts.end()), pts.end());
        
        if (pts.size() <= 1) {
            vector<pair<int, int>> res;
            for(auto p : pts) res.push_back({(int)p.first, (int)p.second});
            return res;
        }

        vector<pair<long long, long long>> lower, upper;
        for (const auto& p : pts) {
            while (lower.size() >= 2 && cross(lower[lower.size()-2].first, lower[lower.size()-2].second,
                                              lower.back().first, lower.back().second,
                                              p.first, p.second) <= 0) {
                lower.pop_back();
            }
            lower.push_back(p);
        }
        for (int i = pts.size() - 1; i >= 0; i--) {
            const auto& p = pts[i];
            while (upper.size() >= 2 && cross(upper[upper.size()-2].first, upper[upper.size()-2].second,
                                              upper.back().first, upper.back().second,
                                              p.first, p.second) <= 0) {
                upper.pop_back();
            }
            upper.push_back(p);
        }

        vector<pair<long long, long long>> hull = lower;
        hull.pop_back();
        hull.insert(hull.end(), upper.begin(), upper.end());
        hull.pop_back();

        int h = hull.size();
        if (h <= 2) {
            vector<pair<int, int>> res;
            for(auto p : hull) res.push_back({(int)p.first, (int)p.second});
            return res;
        }

        double cosT = cos(theta * M_PI / 180.0);
        vector<pair<int, int>> keep;
        
        for (int i = 0; i < h; i++) {
            auto prev = hull[(i - 1 + h) % h];
            auto curr = hull[i];
            auto nxt = hull[(i + 1) % h];
            
            long long ux = prev.first - curr.first;
            long long uy = prev.second - curr.second;
            long long vx = nxt.first - curr.first;
            long long vy = nxt.second - curr.second;
            
            double lenU = hypot(ux, uy);
            double lenV = hypot(vx, vy);
            
            if (lenU == 0 || lenV == 0) {
                keep.push_back({(int)curr.first, (int)curr.second});
                continue;
            }
            
            double dot = (double)ux * vx + (double)uy * vy;
            double cosA = -dot / (lenU * lenV);
            
            if (cosA <= cosT) {
                keep.push_back({(int)curr.first, (int)curr.second});
            }
        }
        
        return keep;
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
    
    int theta;
    cin >> theta;
    
    Solution sol;
    vector<pair<int, int>> res = sol.cappedHull(xs, ys, theta);
    
    if (res.empty()) {
        cout << "0\n";
    } else {
        cout << res.size() << "\n";
        for(const auto& p : res) {
            cout << p.first << " " << p.second << "\n";
        }
    }
    return 0;
}
