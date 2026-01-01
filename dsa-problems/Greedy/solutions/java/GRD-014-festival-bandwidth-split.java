import java.util.*;

class Solution {
    public int maxStages(int n, long B, long[] bandwidths) {
        Arrays.sort(bandwidths);
        
        long currentSum = 0;
        int count = 0;
        
        for (long b : bandwidths) {
            if (currentSum + b <= B) {
                currentSum += b;
                count++;
            } else {
                break;
            }
        }
        
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long B = sc.nextLong();
        
        long[] bandwidths = new long[n];
        for (int i = 0; i < n; i++) {
            bandwidths[i] = sc.nextLong();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.maxStages(n, B, bandwidths));
        sc.close();
    }
}
