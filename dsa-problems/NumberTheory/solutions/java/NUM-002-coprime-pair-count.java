import java.util.*;

class Solution {
    public long countCoprimePairs(int N) {
        if (N < 2) return 0;
        
        int[] phi = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            phi[i] = i;
        }
        
        for (int i = 2; i <= N; i++) {
            if (phi[i] == i) { // i is prime
                for (int j = i; j <= N; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        
        long total = 0;
        for (int i = 2; i <= N; i++) {
            total += phi[i];
        }
        
        return total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int N = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.countCoprimePairs(N));
        }
        sc.close();
    }
}
