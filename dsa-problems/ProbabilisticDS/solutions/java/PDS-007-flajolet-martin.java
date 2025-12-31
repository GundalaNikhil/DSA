import java.util.*;

class Solution {
    public double estimateDistinct(int R) {
        return Math.pow(2, R) / 0.77351;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int R = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.estimateDistinct(R)));
        }
        sc.close();
    }
}
