#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int highestOccupiedRow(int r, vector<int>& capacities, vector<pair<int,int>>& refunds) {
        long long totalCapacity = 0;
        for (int cap : capacities) {
            totalCapacity += cap;
        }
        
        long long totalPeople = totalCapacity - refunds.size();
        
        if (totalPeople <= 0) return 0;
        
        for (int i = 0; i < r; i++) {
            totalPeople -= capacities[i];
            if (totalPeople <= 0) {
                return i + 1;
            }
        }
        
        return r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, n;
    if (!(cin >> r >> n)) return 0;

    vector<int> capacities(r);
    for (int i = 0; i < r; i++) {
        cin >> capacities[i];
    }

    vector<pair<int,int>> refunds(n);
    for (int i = 0; i < n; i++) {
        cin >> refunds[i].first >> refunds[i].second;
    }

    Solution solution;
    cout << solution.highestOccupiedRow(r, capacities, refunds) << "\n";

    return 0;
}
