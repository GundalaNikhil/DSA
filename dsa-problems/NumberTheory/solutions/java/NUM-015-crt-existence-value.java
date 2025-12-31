import java.util.*;
import java.math.BigInteger;

class Solution {
    // Extended Euclidean Algorithm
    // Returns [g, x, y] such that ax + by = g
    private BigInteger[] extendedGCD(BigInteger a, BigInteger b) {
        if (b.equals(BigInteger.ZERO)) return new BigInteger[]{a, BigInteger.ONE, BigInteger.ZERO};
        BigInteger[] vals = extendedGCD(b, a.mod(b));
        BigInteger g = vals[0];
        BigInteger x1 = vals[1];
        BigInteger y1 = vals[2];
        BigInteger x = y1;
        BigInteger y = x1.subtract(a.divide(b).multiply(y1));
        return new BigInteger[]{g, x, y};
    }

    public String crtSolve(long[] a, long[] m) {
        BigInteger curA = BigInteger.ZERO;
        BigInteger curM = BigInteger.ONE;
        
        for (int i = 0; i < a.length; i++) {
            BigInteger A = BigInteger.valueOf(a[i]);
            BigInteger M = BigInteger.valueOf(m[i]);
            
            // Solve: x = curA (mod curM), x = A (mod M)
            // curA + k * curM = A (mod M)
            // k * curM = A - curA (mod M)
            
            BigInteger rhs = A.subtract(curA).mod(M);
            if (rhs.signum() < 0) rhs = rhs.add(M);
            
            BigInteger[] gcdRes = extendedGCD(curM, M);
            BigInteger g = gcdRes[0];
            BigInteger x = gcdRes[1];
            
            if (!rhs.mod(g).equals(BigInteger.ZERO)) return null;
            
            BigInteger mod = M.divide(g);
            // k = (rhs/g) * x (mod M/g)
            BigInteger k = rhs.divide(g).multiply(x.mod(mod).add(mod).mod(mod)).mod(mod);
            
            BigInteger newM = curM.multiply(M.divide(g));
            curA = curA.add(k.multiply(curM)).mod(newM);
            curM = newM;
        }
        
        return curA.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            long[] a = new long[k];
            long[] m = new long[k];
            for (int i = 0; i < k; i++) {
                a[i] = sc.nextLong();
                m[i] = sc.nextLong();
            }

            Solution solution = new Solution();
            String res = solution.crtSolve(a, m);
            if (res == null) {
                System.out.println("NO");
            } else {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
