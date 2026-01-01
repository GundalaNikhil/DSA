#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string weightedMedian(const vector<int>& A, const vector<int>& B, long long wA, long long wB) {
        vector<int> combined;
        combined.reserve(A.size() + B.size());
        combined.insert(combined.end(), A.begin(), A.end());
        combined.insert(combined.end(), B.begin(), B.end());
        sort(combined.begin(), combined.end());

        int n = combined.size();
        if (n % 2 == 1) {
            return to_string(combined[n / 2]);
        }

        int mid1 = combined[n / 2 - 1];
        int mid2 = combined[n / 2];
        int avg = (mid1 + mid2) / 2;
        return to_string(avg);
    }
};
