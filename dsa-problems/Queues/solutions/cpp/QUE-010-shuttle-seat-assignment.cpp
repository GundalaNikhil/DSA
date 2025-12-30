#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    int minSeats(const vector<int>& arrivals, const vector<int>& departures) {
        int n = arrivals.size();
        vector<pair<int, int>> intervals(n);
        for (int i = 0; i < n; i++) {
            intervals[i] = {arrivals[i], departures[i]};
        }
        
        sort(intervals.begin(), intervals.end());
        
        priority_queue<int, vector<int>, greater<int>> pq; // Min-heap
        int maxSeats = 0;
        
        for (const auto& interval : intervals) {
            int start = interval.first;
            int end = interval.second;
            
            while (!pq.empty() && pq.top() <= start) {
                pq.pop();
            }
            
            pq.push(end);
            maxSeats = max(maxSeats, (int)pq.size());
        }
        return maxSeats;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> arrivals(n), departures(n);
        for (int i = 0; i < n; i++) {
            cin >> arrivals[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> departures[i];
        }
    
        Solution solution;
        cout << solution.minSeats(arrivals, departures) << "\n";
    }
    return 0;
}
