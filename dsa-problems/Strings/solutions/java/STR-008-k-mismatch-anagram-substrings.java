class Solution {
    public int countKMismatchAnagrams(String s, String p, int k) {
        int m = p.length();
        int n = s.length();

        if (n < m) return 0;

        // Build pattern frequency
        int[] freqP = new int[26];
        for (char c : p.toCharArray()) {
            freqP[c - 'a']++;
        }

        // Initialize window frequency
        int[] freqWindow = new int[26];
        for (int i = 0; i < m; i++) {
            freqWindow[s.charAt(i) - 'a']++;
        }

        int count = 0;

        // Check first window
        if (mismatchCost(freqWindow, freqP) <= k) {
            count++;
        }

        // Slide window
        for (int i = 1; i <= n - m; i++) {
            // Remove leftmost
            freqWindow[s.charAt(i - 1) - 'a']--;
            // Add rightmost
            freqWindow[s.charAt(i + m - 1) - 'a']++;

            if (mismatchCost(freqWindow, freqP) <= k) {
                count++;
            }
        }

        return count;
    }

    private int mismatchCost(int[] freqW, int[] freqP) {
        int cost = 0;
        for (int i = 0; i < 26; i++) {
            if (freqP[i] > freqW[i]) {
                cost += freqP[i] - freqW[i];
            }
        }
        return cost;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String p = sc.next();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countKMismatchAnagrams(s, p, k));
        sc.close();
    }
}
