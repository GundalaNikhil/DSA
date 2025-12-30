#include <vector>

using namespace std;

class Solution {
public:
    long long countAssignments(const vector<int>& nums, int K, int target) {
        return backtrack(0, 0, 0, nums, K, target);
    }

private:
    long long backtrack(int index, int currentSum, int negations, const vector<int>& nums, int K, int target) {
        if (index == nums.size()) {
            return currentSum == target ? 1 : 0;
        }

        long long count = 0;

        // Option 1: +
        count += backtrack(index + 1, currentSum + nums[index], negations, nums, K, target);

        // Option 2: -
        if (negations < K) {
            count += backtrack(index + 1, currentSum - nums[index], negations + 1, nums, K, target);
        }

        return count;
    }
};
