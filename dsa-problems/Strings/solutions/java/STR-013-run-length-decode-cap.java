import java.util.*;

class Solution {
    public String decodeWithCap(String s, int cap) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        int n = s.length();

        while (i < n) {
            // Read character
            char ch = s.charAt(i);
            i++;

            // Read count
            StringBuilder countStr = new StringBuilder();
            while (i < n && Character.isDigit(s.charAt(i))) {
                countStr.append(s.charAt(i));
                i++;
            }

            // Decode with cap
            int count = countStr.length() > 0 ? Integer.parseInt(countStr.toString()) : 1;
            int actualCount = Math.min(count, cap);

            for (int j = 0; j < actualCount; j++) {
                result.append(ch);
            }
        }

        return result.toString();
    }
}

















class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int cap = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.decodeWithCap(s, cap));
        sc.close();
    }
}
