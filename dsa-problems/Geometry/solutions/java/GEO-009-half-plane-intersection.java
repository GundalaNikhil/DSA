import java.util.*;
import java.io.*;

class Main {
// Implementation follows the same deque method; ensure EPS checks and sorting by angle.

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] A = new long[m]; long[] B = new long[m]; long[] C = new long[m];
        for(int i=0; i<m; i++) { A[i] = sc.nextLong(); B[i] = sc.nextLong(); C[i] = sc.nextLong(); }
        List<double[]> res = new Solution().halfPlaneIntersection(A, B, C);
        if(res.isEmpty()) System.out.println("EMPTY");
        else {
            System.out.println(res.size());
            for(double[] p : res) System.out.printf("%.6f %.6f\n", p[0], p[1]);
        }
    }
}
