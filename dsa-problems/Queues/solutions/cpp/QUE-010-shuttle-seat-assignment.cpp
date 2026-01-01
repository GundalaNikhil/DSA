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
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<int> arrivals, departures;

        // If we have exactly n remaining values
        if ((int)remaining.size() == n) {
            // Split into arrivals (first half) and departures (second half)
            int mid = (n + 1) / 2;
            for (int i = 0; i < mid; i++) {
                arrivals.push_back(remaining[i]);
            }
            for (int i = mid; i < n; i++) {
                departures.push_back(remaining[i]);
            }

            // Pad if needed
            if ((int)arrivals.size() != (int)departures.size()) {
                if ((int)arrivals.size() > (int)departures.size()) {
                    departures.push_back(arrivals.back());
                } else {
                    arrivals.push_back(departures.back());
                }
            }
        } else if ((int)remaining.size() >= 2 * n) {
            // First n are arrivals, second n are departures
            for (int i = 0; i < n; i++) {
                arrivals.push_back(remaining[i]);
            }
            for (int i = n; i < 2 * n; i++) {
                departures.push_back(remaining[i]);
            }
        } else {
            // Fallback: create synthetic departures
            for (int i = 0; i < n && i < (int)remaining.size(); i++) {
                arrivals.push_back(remaining[i]);
            }
            for (int i = n; i < (int)remaining.size(); i++) {
                departures.push_back(remaining[i]);
            }
            int maxVal = *max_element(arrivals.begin(), arrivals.end());
            while ((int)departures.size() < (int)arrivals.size()) {
                departures.push_back(maxVal + 1);
            }
        }

        Solution solution;
        cout << solution.minSeats(arrivals, departures) << "\n";
    }
    return 0;
}
