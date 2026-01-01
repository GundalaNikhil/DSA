import java.util.*;

class Solution {
    public int minLargerGroupSize(int[] a, int D) {
        int n = a.length;
        int total = 0;
        for (int x : a) total += x;

        List<Set<Integer>> dp = new ArrayList<>();
        for (int i = 0; i <= n; i++) dp.add(new HashSet<>());
        dp.get(0).add(0);

        for (int x : a) {
            for (int k = n - 1; k >= 0; k--) {
                for (int s : new ArrayList<>(dp.get(k))) {
                    dp.get(k + 1).add(s + x);
                }
            }
        }

        int ans = Integer.MAX_VALUE;
        for (int k = 0; k <= n; k++) {
            for (int s : dp.get(k)) {
                if (Math.abs(total - 2 * s) <= D) {
                    ans = Math.min(ans, Math.max(k, n - k));
                }
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int D = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        System.out.println(new Solution().minLargerGroupSize(a, D));
        sc.close();
    }
}
