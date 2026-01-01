import java.util.*;

class Solution {
    public long maxFinalStrength(int[] strengths, int[] priority) {
        long totalSum = 0;
        boolean has1 = false;
        boolean has2 = false;
        boolean has3 = false;
        
        for (int i = 0; i < strengths.length; i++) {
            totalSum += strengths[i];
            if (priority[i] == 1) has1 = true;
            else if (priority[i] == 2) has2 = true;
            else if (priority[i] == 3) has3 = true;
        }
        
        long penalty = 0;
        
        if (has1 && has2 && has3) {
            penalty = 2; // 3->2 (1) + 2->1 (1)
        } else if (has1 && has2) {
            penalty = 1;
        } else if (has2 && has3) {
            penalty = 1;
        } else if (has1 && has3) {
            penalty = 2;
        }
        
        return totalSum - penalty;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] strengths = new int[n];
            int[] priority = new int[n];
            for (int i = 0; i < n; i++) {
                strengths[i] = sc.nextInt();
            }
            for (int i = 0; i < n; i++) {
                priority[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maxFinalStrength(strengths, priority));
        }
        sc.close();
    }
}
