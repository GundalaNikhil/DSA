#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> medianAfterBatches(int k, int t, vector<vector<int>>& batches) {
        priority_queue<int> lower;
        priority_queue<int, vector<int>, greater<int>> upper;
        
        unordered_map<int, int> freq;
        unordered_map<int, pair<int, int>> location; // val -> {lower_cnt, upper_cnt}
        
        int validLower = 0;
        int validUpper = 0;
        vector<string> results;
        
        for (const auto& batch : batches) {
            for (int x : batch) {
                freq[x]++;
                int f = freq[x];
                
                if (f > t + 1) continue;
                
                if (f == t + 1) {
                    validLower -= location[x].first;
                    validUpper -= location[x].second;
                    continue;
                }
                
                if (lower.empty() || x <= lower.top()) {
                    lower.push(x);
                    location[x].first++;
                    validLower++;
                } else {
                    upper.push(x);
                    location[x].second++;
                    validUpper++;
                }
            }
            
            while (true) {
                while (!lower.empty() && freq[lower.top()] > t) lower.pop();
                while (!upper.empty() && freq[upper.top()] > t) upper.pop();
                
                if (validLower > validUpper + 1) {
                    int val = lower.top(); lower.pop();
                    location[val].first--;
                    location[val].second++;
                    upper.push(val);
                    validLower--;
                    validUpper++;
                } else if (validUpper > validLower) {
                    int val = upper.top(); upper.pop();
                    location[val].second--;
                    location[val].first++;
                    lower.push(val);
                    validUpper--;
                    validLower++;
                } else {
                    break;
                }
            }
            
            if (validLower + validUpper == 0) {
                results.push_back("NA");
            } else {
                long long med;
                if ((validLower + validUpper) % 2 == 1) {
                    med = lower.top();
                } else {
                    long long v1 = lower.top();
                    long long v2 = upper.top();
                    med = floor((v1 + v2) / 2.0);
                }
                results.push_back(to_string(med));
            }
        }
        
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, t;
    if (!(cin >> k >> t)) return 0;

    vector<vector<int>> batches(k);
    for (int i = 0; i < k; i++) {
        int m;
        cin >> m;
        batches[i].resize(m);
        for (int j = 0; j < m; j++) {
            cin >> batches[i][j];
        }
    }

    Solution solution;
    vector<string> result = solution.medianAfterBatches(k, t, batches);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << "\n";

    return 0;
}
