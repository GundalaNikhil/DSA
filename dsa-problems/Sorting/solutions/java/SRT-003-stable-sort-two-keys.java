import java.util.*;

class Solution {
    public int[][] stableSort(int[][] records) {
        // Java's Arrays.sort for objects (int[]) is stable (TimSort)
        Arrays.sort(records, (a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            } else {
                return Integer.compare(b[1], a[1]); // Descending for key2
            }
        });
        return records;
    }
}
