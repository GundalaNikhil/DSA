import java.util.*;

class Solution {
    public long countCombinations(List<Integer> values, int target) {
        return backtrack(0, 0, values, target);
    }

    private long backtrack(int index, int currentSum, List<Integer> values, int target) {
        if (currentSum == target) {
            return 1;
        }
        if (currentSum > target || index == values.size()) {
            return 0;
        }

        long count = 0;
        int value = values.get(index);

        // Option 1: Don't take any of the current value
        count += backtrack(index + 1, currentSum, values, target);

        // Option 2: Take 1 or more of this value
        int count_used = 1;
        while (currentSum + (long)value * count_used <= target) {
            count += backtrack(index + 1, currentSum + value * count_used, values, target);
            count_used++;
        }
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int target = sc.nextInt();
        
        List<Integer> values = new ArrayList<>();
        // Read remaining ints
        while(sc.hasNextInt()) {
            values.add(sc.nextInt());
        }
        
        Solution sol = new Solution();
        System.out.println(sol.countCombinations(values, target));
        sc.close();
    }
}
