import java.util.*;

class Solution {
    public int[] closestPair(int[] arr, int target) {
        Arrays.sort(arr);
        int n = arr.length;
        int left = 0;
        int right = n - 1;
        
        long minDiff = Long.MAX_VALUE;
        int resLeft = -1;
        int resRight = -1;
        
        while (left < right) {
            long sum = (long) arr[left] + arr[right];
            long diff = Math.abs(sum - target);
            
            if (diff < minDiff) {
                minDiff = diff;
                resLeft = arr[left];
                resRight = arr[right];
            }
            // If diff is equal, we prefer smaller arr[left], which we already have
            // since left increases. So no update needed.
            
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return new int[]{resLeft, resRight};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int target = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        int[] result = solution.closestPair(arr, target);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
