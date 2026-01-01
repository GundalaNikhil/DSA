import java.util.*;
import java.io.*;

class Solution {
    public int[] nextTallerWithin(int[] h, int w) {
        int n = h.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>(); // Indices
        
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && h[stack.peek()] <= h[i]) {
                stack.pop();
            }
            
            if (!stack.isEmpty()) {
                int j = stack.peek();
                if (j - i <= w) {
                    result[i] = h[j];
                }
            }
            
            stack.push(i);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N (Line 1) or first token
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        // We might need to handle token-based parsing robustly
        // Problem format: N, then Array, then W.
        // Array tokens might be on second line. W on third line.
        // Or all spread out.
        // Let's use a tokenizer approach.
        
        StringTokenizer st = new StringTokenizer(line);
        if (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int[] h = new int[n];
        
        int loaded = 0;
        while (loaded < n) {
            if (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (st.hasMoreTokens()) {
                h[loaded++] = Integer.parseInt(st.nextToken());
            }
        }
        
        // Read W
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int w = 0;
        if (st.hasMoreTokens()) {
            w = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        int[] res = sol.nextTallerWithin(h, w);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
