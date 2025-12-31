import java.util.*;

class Solution {
    public String pileSplitGame(int n) {
        if (n == 0) return "Second";
        int[] g = new int[n + 1];
        
        for (int i = 3; i <= n; i++) {
            Set<Integer> reachable = new HashSet<>();
            // Split into j and i-j. j starts at 1.
            // Condition: j != i-j => 2*j != i.
            // Also j < i-j to avoid duplicates => 2*j < i.
            for (int j = 1; 2 * j < i; j++) {
                reachable.add(g[j] ^ g[i - j]);
            }
            
            // Calculate mex
            int mex = 0;
            while (reachable.contains(mex)) {
                mex++;
            }
            g[i] = mex;
        }
        
        return g[n] > 0 ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.pileSplitGame(n));
        }
        sc.close();
    }
}
