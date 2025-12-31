import java.util.*;

class Solution {

    public int[] sortWithSwapsFixed(int[] arr, long S) {
        int n = arr.length;
        Queue<Integer> q0 = new LinkedList<>();
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) q0.add(i);
            else if (arr[i] == 1) q1.add(i);
            else q2.add(i);
        }

        int[] bit = new int[n + 1];
        for (int i = 0; i < n; i++) update(bit, i + 1, 1);

        int[] res = new int[n];

        for (int i = 0; i < n; i++) {
            Integer idx0 = q0.peek();
            Integer idx1 = q1.peek();
            Integer idx2 = q2.peek();

            long cost0 = (idx0 != null) ? query(bit, idx0) : Long.MAX_VALUE;
            long cost1 = (idx1 != null) ? query(bit, idx1) : Long.MAX_VALUE;

            if (cost0 <= S) {
                S -= cost0;
                res[i] = 0;
                q0.poll();
                update(bit, idx0 + 1, -1);
            } else if (cost1 <= S) {

                S -= cost1;
                res[i] = 1;
                q1.poll();
                update(bit, idx1 + 1, -1);
            } else {
                // Pick the element with minimum index (cost 0)
                int minIdx = Integer.MAX_VALUE;
                if (idx0 != null) minIdx = Math.min(minIdx, idx0);
                if (idx1 != null) minIdx = Math.min(minIdx, idx1);
                if (idx2 != null) minIdx = Math.min(minIdx, idx2);

                if (idx0 != null && minIdx == idx0) { res[i]=0; q0.poll(); update(bit, idx0+1, -1); }
                else if (idx1 != null && minIdx == idx1) { res[i]=1; q1.poll(); update(bit, idx1+1, -1); }
                else { res[i]=2; q2.poll(); update(bit, idx2+1, -1); }
            }
        }
        return res;
    }

    private void update(int[] bit, int idx, int val) {
        for (; idx < bit.length; idx += idx & -idx) bit[idx] += val;
    }

    private int query(int[] bit, int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
        return sum;
    }
}
