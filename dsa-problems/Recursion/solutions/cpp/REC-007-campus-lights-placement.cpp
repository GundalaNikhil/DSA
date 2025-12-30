#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> placeLights(int n, int k, int d) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(0, k, n, d, current, result);
        return result;
    }

private:
    void backtrack(int index, int k, int n, int d, vector<int>& current, vector<vector<int>>& result) {
        if (k == 0) {
            result.push_back(current);
            return;
        }
        if (index >= n) {
            return;
        }

        // Option 1: Place light
        current.push_back(index);
        backtrack(index + d, k - 1, n, d, current, result);
        current.pop_back();

        // Option 2: Skip
        backtrack(index + 1, k, n, d, current, result);
    }
};
