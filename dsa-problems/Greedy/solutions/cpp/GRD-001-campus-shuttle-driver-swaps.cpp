#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDriverSwaps(vector<pair<int,int>>& trips, pair<int,int> driverA, pair<int,int> driverB) {
        int n = trips.size();
        const int INF = 1e9;
        
        int costA = INF;
        int costB = INF;
        
        auto canCover = [](pair<int,int>& trip, pair<int,int>& driver) {
            return driver.first <= trip.first && trip.second <= driver.second;
        };
        
        // Base case
        if (canCover(trips[0], driverA)) costA = 0;
        if (canCover(trips[0], driverB)) costB = 0;
        
        for (int i = 1; i < n; i++) {
            int nextCostA = INF;
            int nextCostB = INF;
            
            if (canCover(trips[i], driverA)) {
                nextCostA = min(costA, costB + 1);
            }
            
            if (canCover(trips[i], driverB)) {
                nextCostB = min(costB, costA + 1);
            }
            
            costA = nextCostA;
            costB = nextCostB;
        }
        
        int result = min(costA, costB);
        return result >= INF ? -1 : result;
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
    
    pair<int,int> driverA, driverB;
    cin >> driverA.first >> driverA.second;
    cin >> driverB.first >> driverB.second;
    
    Solution solution;
    cout << solution.minDriverSwaps(trips, driverA, driverB) << "\n";
    
    return 0;
}
