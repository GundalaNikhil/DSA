import java.util.*;

class Solution {
    public long minOvertimeCost(int n, long H, int[][] shifts) {
        long totalStandard = 0;
        int minRate = Integer.MAX_VALUE;
        
        for (int[] shift : shifts) {
            totalStandard += shift[0];
            if (shift[1] < minRate) {
                minRate = shift[1];
            }
        }
        
        if (totalStandard >= H) {
            return 0;
        }
        
        long needed = H - totalStandard;
        return needed * minRate;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long H = sc.nextLong();

        int[][] shifts = new int[n][2];
        for (int i = 0; i < n; i++) {
            shifts[i][0] = sc.nextInt();
            shifts[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minOvertimeCost(n, H, shifts));
        sc.close();
    }
}
