#include <vector>
#include <algorithm>

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
