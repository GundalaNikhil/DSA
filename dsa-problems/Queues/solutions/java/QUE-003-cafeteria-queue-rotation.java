import java.util.*;

class Solution {
    public int[] rotateQueue(int[] values, long k) {
        int n = values.length;
        if (n == 0) return new int[0];
        
        int rotations = (int)(k % n);
        if (rotations == 0) return values;
        
        int[] result = new int[n];
        // Copy from rotations to end -> start of result
        // System.arraycopy(src, srcPos, dest, destPos, length)
        
        // Part 1: values[rotations...n-1] -> result[0...]
        System.arraycopy(values, rotations, result, 0, n - rotations);
        
        // Part 2: values[0...rotations-1] -> result[n-rotations...]
        System.arraycopy(values, 0, result, n - rotations, rotations);
        
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
            long k = sc.nextLong();
    
            Solution solution = new Solution();
            int[] result = solution.rotateQueue(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
