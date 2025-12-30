import java.util.*;

class Solution {
    public List<List<Integer>> packCombinations(int[] values, int[] packs, int target) {
        List<List<Integer>> result = new ArrayList<>();
        // We need to pass index, current sum, and current list of values
        backtrack(0, 0, new ArrayList<>(), values, packs, target, result);
        
        // The problem asks for "unique combinations". 
        // If the problem implies set uniqueness based on content (multiset of values),
        // we should deduplicate. Given "List all unique combinations", let's use a Set to be safe
        // or ensure we generate them in a specific order.
        // However, usually distinct indices constitute distinct solutions. 
        // Let's stick to simple backtracking first.
        // Sorting the internal lists is required for the output format "nondecreasing order".
        
        for (List<Integer> list : result) {
            Collections.sort(list);
        }
        
        // Deduplicate based on content
        Set<List<Integer>> uniqueResults = new HashSet<>(result);
        List<List<Integer>> finalResult = new ArrayList<>(uniqueResults);
        
        // Sort the list of lists for consistent output
        finalResult.sort((a, b) -> {
            for (int i = 0; i < Math.min(a.size(), b.size()); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return a.size() - b.size();
        });
        
        return finalResult;
    }

    private void backtrack(int index, int currentSum, List<Integer> currentList, 
                          int[] values, int[] packs, int target, List<List<Integer>> result) {
        if (currentSum == target) {
            result.add(new ArrayList<>(currentList));
            return;
        }
        if (currentSum > target || index == values.length) {
            return;
        }

        // Option 1: Include current pack
        int packVal = values[index];
        int packSize = packs[index];
        int totalVal = packVal * packSize;

        if (currentSum + totalVal <= target) {
            for (int k = 0; k < packSize; k++) currentList.add(packVal);
            backtrack(index + 1, currentSum + totalVal, currentList, values, packs, target, result);
            for (int k = 0; k < packSize; k++) currentList.remove(currentList.size() - 1);
        }

        // Option 2: Exclude current pack
        backtrack(index + 1, currentSum, currentList, values, packs, target, result);
    }
}
