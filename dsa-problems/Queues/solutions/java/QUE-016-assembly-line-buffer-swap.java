import java.util.*;

class Solution {
    public int[][] swapQueues(int[] q1, int[] q2) {
        return new int[][]{q2, q1};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] q1, q2;

            // If we have exactly 2n values
            if (remaining.size() == 2 * n) {
                q1 = new int[n];
                q2 = new int[n];
                for (int i = 0; i < n; i++) {
                    q1[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    q2[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as q1, create default q2
                q1 = new int[n];
                q2 = new int[n];
                for (int i = 0; i < n; i++) {
                    q1[i] = remaining.get(i);
                    q2[i] = 0;
                }
            } else {
                // Fallback
                int q1Len = Math.min(n, remaining.size());
                q1 = new int[q1Len];
                q2 = new int[q1Len];

                for (int i = 0; i < q1Len; i++) {
                    q1[i] = remaining.get(i);
                    if (i < remaining.size() - n) {
                        q2[i] = remaining.get(n + i);
                    } else {
                        q2[i] = 0;
                    }
                }
            }

            Solution sol = new Solution();
            int[][] result = sol.swapQueues(q1, q2);
            for (int j = 0; j < 2; j++) {
                for (int i = 0; i < result[j].length; i++) {
                    if (i > 0) System.out.print(" ");
                    System.out.print(result[j][i]);
                }
                System.out.println();
            }
        }
    }
}
