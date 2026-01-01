#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countCombinations(const vector<int>& values, int target) {
        return backtrack(0, 0, values, target);
    }

private:
    long long backtrack(int index, int currentSum, const vector<int>& values, int target) {
        if (currentSum == target) {
            return 1;
        }
        if (currentSum > target || index == values.size()) {
            return 0;
        }

        long long count = 0;
        int value = values[index];

        // Option 1: Don't take any of the current value
        count += backtrack(index + 1, currentSum, values, target);

        // Option 2: Take 1 or more of this value
        int count_used = 1;
        while (currentSum + (long long)value * count_used <= target) {
            count += backtrack(index + 1, currentSum + value * count_used, values, target);
            count_used++;
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, target;
    if (!(cin >> n >> target)) return 0;
    
    vector<int> values(n);
    for(int i=0; i<n; i++) cin >> values[i];
    
    Solution sol;
    cout << sol.countCombinations(values, target) << endl;
    return 0;
}
