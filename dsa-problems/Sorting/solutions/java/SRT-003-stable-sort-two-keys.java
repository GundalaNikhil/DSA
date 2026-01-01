import java.util.*;

class Solution {
    public int[][] stableSort(int[][] records) {
        // Java's Arrays.sort for objects (int[]) is stable (TimSort)
        Arrays.sort(records, (a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            } else {
                return Integer.compare(a[1], b[1]); // Ascending for key2
            }
        });
        return records;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int[][] records = new int[n][2];
        for (int i = 0; i < n; i++) {
            records[i][0] = sc.nextInt();
            records[i][1] = sc.nextInt();
        }
        Solution solution = new Solution();
        int[][] result = solution.stableSort(records);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append('\n');
            sb.append(result[i][0]).append(' ').append(result[i][1]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
