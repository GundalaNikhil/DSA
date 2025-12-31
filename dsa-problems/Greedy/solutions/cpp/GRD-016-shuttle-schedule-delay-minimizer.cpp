#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minTotalDelay(int n, vector<pair<int,int>>& trips) {
        sort(trips.begin(), trips.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
            return (long long)a.first + a.second < (long long)b.first + b.second;
        });
        
        long long currentTime = 0;
        long long totalDelay = 0;
        
        for (const auto& trip : trips) {
            int s = trip.first;
            int d = trip.second;
            
            long long delay = max(0LL, currentTime - s);
            totalDelay += delay;
            currentTime += d;
        }
        
        return totalDelay;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<pair<int,int>> trips(n);
    for (int i = 0; i < n; i++) {
        cin >> trips[i].first >> trips[i].second;
    }
    
    Solution solution;
    cout << solution.minTotalDelay(n, trips) << "\n";
    
    return 0;
}
