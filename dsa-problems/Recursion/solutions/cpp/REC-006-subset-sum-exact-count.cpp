#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findSubset(const vector<int>& arr, int k, int target) {
        vector<int> current;
        if (backtrack(0, 0, 0, arr, k, target, current)) {
            return current;
        }
        return {};
    }

private:
    bool backtrack(int index, int count, int currentSum, const vector<int>& arr, int k, int target, vector<int>& current) {
        if (count == k) {
            return currentSum == target;
        }
        if (index == arr.size()) {
            return false;
        }
        
        // Pruning
        if (arr.size() - index < k - count) {
            return false;
        }

        // Option 1: Include
        current.push_back(arr[index]);
        if (backtrack(index + 1, count + 1, currentSum + arr[index], arr, k, target, current)) {
            return true;
        }
        current.pop_back();

        // Option 2: Exclude
        if (backtrack(index + 1, count, currentSum, arr, k, target, current)) {
            return true;
        }

        return false;
    }
};
