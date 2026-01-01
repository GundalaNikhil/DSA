#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> stableSort(vector<vector<int>> records) {
        // C++ std::sort is NOT stable. Use std::stable_sort.
        stable_sort(records.begin(), records.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] != b[0]) {
                return a[0] < b[0];
            }
            return a[1] < b[1]; // Ascending for key2
        });
        return records;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> records(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> records[i][0] >> records[i][1];
    }
    Solution solution;
    vector<vector<int>> result = solution.stableSort(records);
    for (const auto& rec : result) {
        if (rec.size() >= 2) {
            cout << rec[0] << " " << rec[1] << "\n";
        }
    }
    return 0;
}
