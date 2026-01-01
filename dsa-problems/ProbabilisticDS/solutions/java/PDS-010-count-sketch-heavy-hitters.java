import java.util.*;

class Solution {
    public int countSketchEstimate(int[] count, int[] sign) {
        int d = count.length;
        int[] estimates = new int[d];
        for (int i = 0; i < d; i++) {
            estimates[i] = count[i] * sign[i];
        }
        Arrays.sort(estimates);
        return estimates[d / 2];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int d = sc.nextInt();
            int[] count = new int[d];
            int[] sign = new int[d];
            for (int i = 0; i < d; i++) {
                count[i] = sc.nextInt();
                sign[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            System.out.println(solution.countSketchEstimate(count, sign));
        }
        sc.close();
    }
}
