import java.util.*;

class Solution {
    public List<List<Integer>> placeLights(int n, int k, int d) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(0, k, n, d, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int index, int k, int n, int d, List<Integer> current, List<List<Integer>> result) {
        if (k == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        if (index >= n) {
            return;
        }

        // Option 1: Place light at 'index'
        current.add(index);
        // Next valid position must be at least 'd' away.
        // If d=2 and we pick 0, next is 0+2=2.
        backtrack(index + d, k - 1, n, d, current, result);
        current.remove(current.size() - 1);

        // Option 2: Skip 'index'
        backtrack(index + 1, k, n, d, current, result);
    }
}
