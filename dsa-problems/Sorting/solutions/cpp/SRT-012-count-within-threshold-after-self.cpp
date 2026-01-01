#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> countWithinThreshold(const vector<int>& arr, long long T) {
        int n = arr.size();
        vector<long long> counts(n, 0);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((long long)arr[j] - (long long)arr[i] <= T) {
                    counts[i]++;
                }
            }
        }

        return counts;
    }
};
