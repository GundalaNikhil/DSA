import java.util.*;
import java.io.*;

class Main {
// Implement sweep with events and a lazy segment tree storing covered length when sum>=W.

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        int W = sc.nextInt();
        long[] x1 = new long[m]; long[] y1 = new long[m];
        long[] x2 = new long[m]; long[] y2 = new long[m]; long[] w = new long[m];
        for(int i=0; i<m; i++) {
            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();
            x2[i] = sc.nextLong(); y2[i] = sc.nextLong(); w[i] = sc.nextLong();
        }
        System.out.println(new Solution().weightedArea(x1, y1, x2, y2, w, W));
    }
}
