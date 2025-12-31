import java.util.*;

class Solution {
    public long subsetAndEqualsX(int[] a, int X) {
        // Pruning: Keep only elements that are supermasks of X
        ArrayList<Integer> candidates = new ArrayList<>();
        for (int v : a) {
            if ((v & X) == X) {
                candidates.add(v);
            }
        }
        
        int n = candidates.size();
        long count = 0;
        
        // Iterate subsets of filtered array
        // Loop limit is 1<<n. Since n <= 20, loop fits in int.
        int limit = 1 << n;
        for (int mask = 1; mask < limit; mask++) {
            // Compute AND of this subset
            // Initialize with all 1s (identity for AND) 
            // OR simpler: initialize with first element found
            int currentAnd = -1; 
            boolean empty = true;
            
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    if (empty) {
                        currentAnd = candidates.get(i);
                        empty = false;
                    } else {
                        currentAnd &= candidates.get(i);
                    }
                    
                    // Optimization: If currentAnd drops below X (missing bits), simplify break?
                    // We know (v & X) == X, so currentAnd will always have bits of X set.
                    // It will never be "less" than X in set-bit terms. 
                    // It will only converge towards X.
                }
            }
            
            if (!empty && currentAnd == X) {
                count++;
            }
        }
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int X = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.subsetAndEqualsX(a, X));
        sc.close();
    }
}
