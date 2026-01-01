import java.util.*;

class Solution {
    public long countExclusiveSubstrings(String a, String b) {
        String s = a + "#" + b;
        int n = s.length();
        int splitIdx = a.length();
        
        // 1. Build SA
        Integer[] sa = new Integer[n];
        int[] rank = new int[n];
        int[] newRank = new int[n];
        
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s.charAt(i);
        }
        
        for (int k = 1; k < n; k *= 2) {
            int len = k;
            Arrays.sort(sa, (i, j) -> {
                if (rank[i] != rank[j]) return rank[i] - rank[j];
                int ri = (i + len < n) ? rank[i + len] : -1;
                int rj = (j + len < n) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                int prev = sa[i - 1];
                int curr = sa[i];
                int r1 = rank[prev];
                int r2 = (prev + len < n) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < n) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) newRank[curr] = newRank[prev];
                else newRank[curr] = newRank[prev] + 1;
            }
            System.arraycopy(newRank, 0, rank, 0, n);
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        // 2. Build LCP
        int[] lcp = new int[n]; // lcp[i] is between sa[i-1] and sa[i]
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == 0) { // First in SA
                k = 0;
                continue;
            }
            int j = sa[rank[i] - 1];
            while (i + k < n && j + k < n && s.charAt(i + k) == s.charAt(j + k)) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Compute max_match_b for each suffix of a
        int[] maxMatchB = new int[n];
        
        // Forward pass
        int currentLCP = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0) currentLCP = Math.min(currentLCP, lcp[i]);
            if (sa[i] > splitIdx) { // Suffix from b
                currentLCP = Integer.MAX_VALUE; // Reset match length (effectively infinite for next)
                // The LCP between this b-suffix and subsequent a-suffixes is limited by lcp array.
                // When we see a b-suffix, the "distance" to it is 0 (conceptually), but we track LCP.
                // Let's rephrase: currentLCP tracks LCP(sa[i], nearest_prev_b).
                // If sa[i] is b, nearest_prev_b is sa[i], so LCP is infinite (length of suffix).
                // But we need LCP(sa[next], sa[i]).
                currentLCP = n; // Max possible
            } else if (sa[i] < splitIdx) { // Suffix from a
                maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
            }
        }
        
        // Backward pass
        currentLCP = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1) currentLCP = Math.min(currentLCP, lcp[i + 1]); // lcp[i+1] is between sa[i] and sa[i+1]
            if (sa[i] > splitIdx) { // Suffix from b
                currentLCP = n;
            } else if (sa[i] < splitIdx) { // Suffix from a
                maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
            }
        }
        
        // 4. Calculate result
        long count = 0;
        int prevALCP = 0; // LCP with previous suffix from A
        
        for (int i = 0; i < n; i++) {
            if (i > 0) prevALCP = Math.min(prevALCP, lcp[i]);
            
            if (sa[i] < splitIdx) { // Suffix from a
                // prevALCP now holds min(lcp) since last 'a' suffix.
                // This is exactly LCP(current_a, prev_a).
                
                int len = splitIdx - sa[i];
                int deduct = Math.max(prevALCP, maxMatchB[i]);
                if (len > deduct) {
                    count += (len - deduct);
                }
                
                // Reset prevALCP for the *next* a-suffix.
                // The LCP between *this* a-suffix and the *next* a-suffix will start being tracked.
                prevALCP = n; 
            }
        }
        
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String a = sc.next();
            if (sc.hasNext()) {
                String b = sc.next();
                Solution solution = new Solution();
                System.out.println(solution.countExclusiveSubstrings(a, b));
            }
        }
        sc.close();
    }
}
