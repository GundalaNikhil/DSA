#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxStages(int n, long long B, vector<long long>& bandwidths) {
        sort(bandwidths.begin(), bandwidths.end());
        
        long long currentSum = 0;
        int count = 0;
        
        for (long long b : bandwidths) {
            if (currentSum + b <= B) {
                currentSum += b;
                count++;
            } else {
                break;
            }
        }
        
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long B;
    if (!(cin >> n >> B)) return 0;

    vector<long long> bandwidths(n);
    for (int i = 0; i < n; i++) {
        cin >> bandwidths[i];
    }

    Solution solution;
    cout << solution.maxStages(n, B, bandwidths) << "\n";

    return 0;
}
