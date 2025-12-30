import java.util.*;

class Solution {
    public long countAssignments(int[] nums, int K, int target) {
        return backtrack(0, 0, 0, nums, K, target);
    }

    private long backtrack(int index, int currentSum, int negations, int[] nums, int K, int target) {
        if (index == nums.length) {
            return currentSum == target ? 1 : 0;
        }

        long count = 0;

        // Option 1: Assign +
        count += backtrack(index + 1, currentSum + nums[index], negations, nums, K, target);

        // Option 2: Assign - (if limit allows)
        if (negations < K) {
            count += backtrack(index + 1, currentSum - nums[index], negations + 1, nums, K, target);
        }

        return count;
    }
}
