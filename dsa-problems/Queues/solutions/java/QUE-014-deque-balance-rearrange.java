import java.util.*;

class Solution {
    public int[] buildDeque(int[] values) {
        int n = values.length;
        int[] result = new int[n];
        int left = 0;
        int right = n - 1;
        int index = 0;
        
        while (left <= right) {
            // Take from front
            result[index++] = values[left];
            
            // Take from back if it's not the same element
            if (left != right) {
                result[index++] = values[right];
            }
            
            left++;
            right--;
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
            
            Solution sol = new Solution();
            int[] result = sol.buildDeque(values);
            for (int i = 0; i < result.length; i++) {
                if (i > 0) System.out.print(" ");
                System.out.print(result[i]);
            }
            System.out.println();
        }
    }
}
