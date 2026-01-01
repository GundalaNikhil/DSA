import java.util.*;

class Solution {
    public int findFlipIndex(List<Integer> nums, String ops, int target) {
        int n_ops = ops.length();
        for (int flip_idx = 0; flip_idx < n_ops; flip_idx++) {
            long current_sum = nums.get(0);
            for (int i = 0; i < n_ops; i++) {
                char op;
                if (i == flip_idx) {
                    op = (ops.charAt(i) == '+') ? '-' : '+';
                } else {
                    op = ops.charAt(i);
                }

                if (op == '+') {
                    current_sum += nums.get(i + 1);
                } else {
                    current_sum -= nums.get(i + 1);
                }
            }
            if (current_sum == target) {
                return flip_idx;
            }
        }
        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<Integer> nums = new ArrayList<>();
        for(int i=0; i<n; i++) nums.add(sc.nextInt());
        
        String ops = sc.next();
        int target = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.findFlipIndex(nums, ops, target));
        sc.close();
    }
}
