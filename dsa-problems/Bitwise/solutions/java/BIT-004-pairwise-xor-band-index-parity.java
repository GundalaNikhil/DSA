import java.util.*;

class Solution {
    static class TrieNode {
        TrieNode[] children = new TrieNode[2];
        int count = 0;
    }

    private void insert(TrieNode root, int num) {
        TrieNode curr = root;
        for (int i = 29; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
            curr.count++;
        }
    }

    private int countLessEqual(TrieNode root, int num, int K) {
        TrieNode curr = root;
        int count = 0;
        for (int i = 29; i >= 0; i--) {
            if (curr == null) break;
            int bitNum = (num >> i) & 1;
            int bitK = (K >> i) & 1;

            if (bitK == 1) {
                // If we choose path that aligns with bitNum, XOR result is 0 (0 < 1).
                // All nums in that subtree are strictly smaller.
                if (curr.children[bitNum] != null) {
                    count += curr.children[bitNum].count;
                }
                // Continue to the path that makes XOR 1 (equal to bitK)
                curr = curr.children[1 - bitNum];
            } else {
                // bitK is 0. We MUST make XOR 0. So must go to child matching bitNum.
                curr = curr.children[bitNum];
            }
        }
        if (curr != null) count += curr.count;
        return count;
    }

    private long countPairsWithLimit(List<Integer> nums, int K) {
        TrieNode root = new TrieNode();
        long total = 0;
        for (int num : nums) {
            total += countLessEqual(root, num, K);
            insert(root, num);
        }
        return total;
    }

    public long countPairwiseXorBandParity(int[] a, int L, int U) {
        List<Integer> evens = new ArrayList<>();
        List<Integer> odds = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            if (i % 2 == 0) evens.add(a[i]);
            else odds.add(a[i]);
        }

        long countEvens = countPairsWithLimit(evens, U) - countPairsWithLimit(evens, L - 1);
        long countOdds = countPairsWithLimit(odds, U) - countPairsWithLimit(odds, L - 1);

        return countEvens + countOdds;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int L = sc.nextInt();
        int U = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countPairwiseXorBandParity(a, L, U));
        sc.close();
    }
}
