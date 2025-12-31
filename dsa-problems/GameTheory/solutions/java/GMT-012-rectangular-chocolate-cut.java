import java.util.*;

class Solution {
    public String chocolateCut(long R, long C) {
        long area = R * C;
        return (area % 2 == 0) ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long R = sc.nextLong();
            long C = sc.nextLong();

            Solution solution = new Solution();
            System.out.println(solution.chocolateCut(R, C));
        }
        sc.close();
    }
}
