#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <numeric>

using namespace std;

class Solution {
    long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

public:
    int maxPointsOnSegment(const vector<vector<int>>& points, int L) {
        int n = points.size();
        if (n <= 1) return n;
        
        map<pair<int, int>, int> pointCounts;
        for (const auto& p : points) {
            pointCounts[{p[0], p[1]}]++;
        }
        
        vector<pair<int, int>> uniquePts;
        vector<int> counts;
        for (auto const& [pt, count] : pointCounts) {
            uniquePts.push_back(pt);
            counts.push_back(count);
        }
        
        int maxPts = 0;
        for (int c : counts) maxPts = max(maxPts, c);
        
        int m = uniquePts.size();
        for (int i = 0; i < m; i++) {
            map<pair<long long, long long>, int> slopeMap;
            long long x1 = uniquePts[i].first;
            long long y1 = uniquePts[i].second;
            
            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                long long x2 = uniquePts[j].first;
                long long y2 = uniquePts[j].second;
                
                long long dx = x2 - x1;
                long long dy = y2 - y1;
                double dist = sqrt((double)dx * dx + (double)dy * dy);
                
                if (dist > L + 1e-9) continue;
                
                long long g = gcd(abs(dx), abs(dy));
                slopeMap[{dx / g, dy / g}] += counts[j];
            }
            
            for (auto const& [slope, count] : slopeMap) {
                maxPts = max(maxPts, counts[i] + count);
            }
        }
        
        return maxPts;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, L;
    if (cin >> n >> L) {
        vector<vector<int>> points(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> points[i][0] >> points[i][1];
        }

        Solution solution;
        cout << solution.maxPointsOnSegment(points, L) << "\n";
    }
    return 0;
}
