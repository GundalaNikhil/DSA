import java.util.*;

class Solution {
    public int toggleRangesMinFlips(int[] A, int[] B) {
        int n = A.length;
        int count = 0;
        int prevDiff = 0;
        
        for (int i = 0; i < n; i++) {
            int currDiff = A[i] ^ B[i];
            
            // If current is mismatch (1) and previous was match (0),
            // we have entered a new island of mismatches.
            // We greedily "start" a flip here. The flip "continues"
            // until the mismatch run ends, handled implicitly.
            if (currDiff == 1 && prevDiff == 0) {
                count++;
            }
            prevDiff = currDiff;
        }
        
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();
        int[] B = new int[n];
        for (int i = 0; i < n; i++) B[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.toggleRangesMinFlips(A, B));
        sc.close();
    }
}
