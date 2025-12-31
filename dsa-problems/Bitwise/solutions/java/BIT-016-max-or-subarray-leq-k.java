import java.util.*;

class Solution {
    public int maxOrSubarrayLeqK(int[] a, int K) {
        int n = a.length;
        int[] bitCounts = new int[32];
        int currentOr = 0;
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < n; right++) {
            // Add a[right] to window
            int val = a[right];
            for (int i = 0; i < 31; i++) {
                if (((val >> i) & 1) == 1) {
                    bitCounts[i]++;
                    // If count becomes > 0, set the bit in currentOr
                    if (bitCounts[i] == 1) {
                        currentOr |= (1 << i);
                    }
                }
            }
            
            // Shrink
            while (left <= right && currentOr > K) {
                int removeVal = a[left];
                for (int i = 0; i < 31; i++) {
                    if (((removeVal >> i) & 1) == 1) {
                        bitCounts[i]--;
                        // If count drops to 0, unset the bit
                        if (bitCounts[i] == 0) {
                            currentOr &= ~(1 << i);
                        }
                    }
                }
                left++;
            }
            
            // Check valid
            if (currentOr <= K) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }
        
        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int K = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxOrSubarrayLeqK(a, K));
        sc.close();
    }
}
