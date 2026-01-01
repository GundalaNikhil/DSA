import java.util.*;
import java.io.*;
import java.math.BigInteger;

class Solution {
    public int countVisible(BigInteger[] h) {
        int n = h.length;
        Stack<Integer> stack = new Stack<>();
        int count = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && h[stack.peek()].compareTo(h[i]) < 0) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                count++;
            }
            stack.push(i);
        }
        return count;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1 = br.readLine();
        if (line1 == null) return;
        
        String line2 = br.readLine();
        if (line2 == null) return;
        
        String[] parts = line2.trim().split("\\s+");
        List<BigInteger> hList = new ArrayList<>();
        
        for (String p : parts) {
            if (!p.isEmpty()) {
                hList.add(new BigInteger(p));
            }
        }
        
        BigInteger[] h = hList.toArray(new BigInteger[0]);
        Solution sol = new Solution();
        System.out.println(sol.countVisible(h));
    }
}
