import java.util.*;

class Solution {
    public double findMedian(int[] maxHeap, int[] minHeap) {
        int n = maxHeap.length;
        int m = minHeap.length;
        int[] all = new int[n + m];
        
        System.arraycopy(maxHeap, 0, all, 0, n);
        System.arraycopy(minHeap, 0, all, n, m);
        
        Arrays.sort(all);
        
        int total = n + m;
        if (total == 0) return 0.0;
        
        if (total % 2 == 1) {
            return (double) all[total / 2];
        } else {
            long sum = (long) all[total / 2 - 1] + all[total / 2];
            return sum / 2.0;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] maxHeap = new int[n];
            int[] minHeap = new int[m];
            for (int i = 0; i < n; i++) maxHeap[i] = sc.nextInt();
            for (int i = 0; i < m; i++) minHeap[i] = sc.nextInt();
            
            Solution solution = new Solution();
            double result = solution.findMedian(maxHeap, minHeap);
            if (result == (long) result) {
                System.out.println((long) result);
            } else {
                System.out.println(result);
            }
        }
        sc.close();
    }
}
