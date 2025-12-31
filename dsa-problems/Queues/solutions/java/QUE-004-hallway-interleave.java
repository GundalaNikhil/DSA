import java.util.*;

class Solution {
    public int[] interleaveQueue(int[] values) {
        int n = values.length;
        int[] result = new int[n];
        int mid = n / 2;
        
        for (int i = 0; i < mid; i++) {
            result[2 * i] = values[i];
            result[2 * i + 1] = values[mid + i];
        }
        
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
    
            Solution solution = new Solution();
            int[] result = solution.interleaveQueue(values);
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
