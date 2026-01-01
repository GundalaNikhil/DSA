import java.util.*;

class Solution {
    public double hllEstimate(int m, int[] registers) {
        double alpha;
        if (m == 16) alpha = 0.673;
        else if (m == 32) alpha = 0.697;
        else if (m == 64) alpha = 0.709;
        else alpha = 0.7213 / (1.0 + 1.079 / m);
        
        double sum = 0.0;
        int zeros = 0;
        for (int val : registers) {
            sum += Math.pow(2.0, -val);
            if (val == 0) zeros++;
        }
        
        double E = alpha * m * m / sum;
        
        if (E <= 2.5 * m) {
            if (zeros > 0) {
                E = m * Math.log((double)m / zeros);
            }
        }
        
        return E;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int[] registers = new int[m];
            for (int i = 0; i < m; i++) {
                registers[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.hllEstimate(m, registers)));
        }
        sc.close();
    }
}
