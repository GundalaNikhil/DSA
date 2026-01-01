import java.util.*;
import java.io.*;

class Main {
static class Solution {
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

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().polygonArea(xs, ys));
    }
}
