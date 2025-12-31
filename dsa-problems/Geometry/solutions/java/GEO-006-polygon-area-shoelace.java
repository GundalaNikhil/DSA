class Solution {
    public long polygonArea(int[] xs, int[] ys) {
        int n = xs.length;
        long sum = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            sum += 1L * xs[i] * ys[j] - 1L * xs[j] * ys[i];
        }
        return Math.abs(sum) / 2;
    }
}
