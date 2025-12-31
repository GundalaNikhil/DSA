import java.util.*;

class Solution {
    public List<Integer> findSubset(int[] arr, int k, int target) {
        List<Integer> result = new ArrayList<>();
        if (backtrack(0, 0, 0, arr, k, target, result)) {
            return result;
        }
        return new ArrayList<>();
    }

    private boolean backtrack(int index, int count, int currentSum, int[] arr, int k, int target, List<Integer> result) {
        if (count == k) {
            return currentSum == target;
        }
        if (index == arr.length) {
            return false;
        }
        
        // Pruning: if remaining elements are not enough to fill k
        if (arr.length - index < k - count) {
            return false;
        }

        // Option 1: Include arr[index]
        result.add(arr[index]);
        if (backtrack(index + 1, count + 1, currentSum + arr[index], arr, k, target, result)) {
            return true;
        }
        result.remove(result.size() - 1); // Backtrack

        // Option 2: Exclude arr[index]
        if (backtrack(index + 1, count, currentSum, arr, k, target, result)) {
            return true;
        }

        return false;
    }
}
