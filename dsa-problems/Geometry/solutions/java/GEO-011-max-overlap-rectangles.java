import java.util.*;
import java.io.*;

class Main {
// Sweep events sorted by x; segment tree with add[] and mx[] storing max coverage.

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] x1 = new long[m]; long[] y1 = new long[m];
        long[] x2 = new long[m]; long[] y2 = new long[m];
        for(int i=0; i<m; i++) {
            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();
            x2[i] = sc.nextLong(); y2[i] = sc.nextLong();
        }
        System.out.println(new Solution().maxOverlap(x1, y1, x2, y2));
    }
}
