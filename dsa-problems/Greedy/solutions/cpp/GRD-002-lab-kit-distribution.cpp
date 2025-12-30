#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
public:
    pair<int,int> distributeKits(int k, int m, vector<int>& quantities) {
        priority_queue<int> pq;
        long long totalKits = 0;
        
        for (int q : quantities) {
            if (q > 0) {
                pq.push(q);
                totalKits += q;
            }
        }
        
        int fulfilled = min((long long)m, totalKits);
        int toDistribute = fulfilled;
        
        while (toDistribute > 0 && !pq.empty()) {
            int maxQ = pq.top();
            pq.pop();
            
            maxQ--;
            toDistribute--;
            
            if (maxQ > 0) {
                pq.push(maxQ);
            }
        }
        
        int remainingTypes = pq.size();
        int zeroedTypes = k - remainingTypes;
        
        return {fulfilled, zeroedTypes};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, m;
    if (!(cin >> k >> m)) return 0;

    vector<int> quantities(k);
    for (int i = 0; i < k; i++) {
        cin >> quantities[i];
    }

    Solution solution;
    pair<int,int> result = solution.distributeKits(k, m, quantities);
    cout << result.first << " " << result.second << "\n";

    return 0;
}
