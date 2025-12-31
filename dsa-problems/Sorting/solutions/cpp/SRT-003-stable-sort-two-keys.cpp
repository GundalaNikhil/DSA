#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> stableSort(vector<vector<int>> records) {
        // C++ std::sort is NOT stable. Use std::stable_sort.
        stable_sort(records.begin(), records.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] != b[0]) {
                return a[0] < b[0];
            }
            return a[1] > b[1]; // Descending for key2
        });
        return records;
    }
};
