import java.util.*;

class Solution {
    int N, K, Target;
    List<Integer> Nums;
    Map<String, Boolean> memo;

    public boolean countAssignments(List<Integer> nums, int k, int target) {
        Nums = nums;
        N = nums.size();
        K = k;
        Target = target;
        memo = new HashMap<>();
        return backtrack(0, 0, 0);
    }

    private boolean backtrack(int index, long current_sum, int negations) {
        if (index == N) return current_sum == Target;

        String key = index + "," + current_sum + "," + negations;
        if (memo.containsKey(key)) return memo.get(key);

        // Positive
        if (backtrack(index + 1, current_sum + Nums.get(index), negations)) {
            memo.put(key, true);
            return true;
        }

        // Negative
        if (negations < K) {
            if (backtrack(index + 1, current_sum - Nums.get(index), negations + 1)) {
                memo.put(key, true);
                return true;
            }
        }

        memo.put(key, false);
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int target = sc.nextInt();
        
        List<Integer> nums = new ArrayList<>();
        for(int i=0; i<n; i++) nums.add(sc.nextInt());
        
        Solution sol = new Solution();
        if(sol.countAssignments(nums, k, target)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
