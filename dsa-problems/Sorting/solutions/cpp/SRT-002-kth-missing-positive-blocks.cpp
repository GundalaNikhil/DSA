#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<long long> solve(const vector<int>& arr, const vector<pair<long long,long long>>& queries) {
        vector<long long> results;
        results.reserve(queries.size());
        int n = arr.size();
        
        for (const auto& q : queries) {
            long long m = q.first * q.second;
            
            int low = 0, high = n - 1;
            int idx = -1;
            
            while (low <= high) {
                int mid = low + (high - low) / 2;
                long long missingCount = arr[mid] - (mid + 1);
                if (missingCount < m) {
                    idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            
            results.push_back(m + idx + 1);
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    vector<pair<long long, long long>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        long long k, b;
        cin >> k >> b;
        queries.push_back({k, b});
    }
    Solution solution;
    vector<long long> results = solution.solve(arr, queries);
    for (long long v : results) {
        cout << v << "\n";
    }
    return 0;
}
