import java.util.*;

class Solution {
    public long countArrangements(int n, int k, int d) {
        // Use Long for result to prevent overflow, though N=15 fits in int
        return backtrack(0, k, n, d);
    }

    private long backtrack(int index, int k, int n, int d) {
        // Base case: all students placed
        if (k == 0) return 1;
        
        // Base case: out of seats
        if (index >= n) return 0;

        long count = 0;

        // Option 1: Place student at 'index'
        // Next student must be at least d+1 seats away
        count += backtrack(index + d + 1, k - 1, n, d);

        // Option 2: Don't place student at 'index', move to next
        count += backtrack(index + 1, k, n, d);

        return count;
    }
}
