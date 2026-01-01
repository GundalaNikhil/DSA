#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

struct Part {
    long long w;
    int q;

    // For priority_queue, we want max quality at top, then min weight if tied.
    // Default is max-heap, so operator< should return true if 'this' is smaller than 'other'.
    bool operator<(const Part& other) const {
        if (q != other.q) return q < other.q;
        return w > other.w;  // If quality is equal, prefer smaller weight (min-heap on weight)
    }
};

class Solution {
public:
    long long maxBundleWeight(int n, int T, vector<int>& weights, vector<int>& qualities) {
        priority_queue<Part> pq;
        
        for (int i = 0; i < n; i++) {
            pq.push({(long long)weights[i], qualities[i]});
        }
        
        while (pq.size() > 1) {
            Part p1 = pq.top(); pq.pop();
            Part p2 = pq.top(); pq.pop();
            
            int newQ = min(p1.q, p2.q) - 1;
            
            if (newQ < T) {
                return -1;
            }
            
            long long minW = min(p1.w, p2.w);
            long long loss = floor(0.1 * minW);
            long long newW = p1.w + p2.w - loss;
            
            pq.push({newW, newQ});
        }
        
        return pq.empty() ? -1 : pq.top().w;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, T;
    if (!(cin >> n >> T)) return 0;

    vector<int> weights(n), qualities(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> qualities[i];
    }

    Solution solution;
    cout << solution.maxBundleWeight(n, T, weights, qualities) << "\n";

    return 0;
}
