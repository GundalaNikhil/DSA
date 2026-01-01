import java.util.*;
import java.io.*;

class Solution {
    public int[] spans(int[] demand) {
        int n = demand.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>(); // Stores indices
        
        for (int i = 0; i < n; i++) {
            // Pop elements strictly smaller than current
            while (!stack.isEmpty() && demand[stack.peek()] < demand[i]) {
                stack.pop();
            }
            
            int prevIdx = stack.isEmpty() ? -1 : stack.peek();
            
            // Logic match Python:
            // if not stack: result[i] = i
            // elif equal: result[i] = 0
            // else: i - stack[-1] - 1
            
            if (stack.isEmpty()) {
                result[i] = i;
            } else if (demand[prevIdx] == demand[i]) {
                result[i] = 0;
            } else {
                result[i] = i - prevIdx - 1;
            }
            
            stack.push(i);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        // Read N
        int n = Integer.parseInt(line.trim());
        
        // Read Array
        // Could be on same line or next line or multiline
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine()); // Try next line
        
        // If next line is empty or null, keep reading?
        // Let's robustly token read
        // Actually, Python reads lines[1].split(). Just one line.
        // Let's mimic robust reading just in case.
        
        while (list.size() < n) {
            while (st != null && !st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) { st = null; break; }
                st = new StringTokenizer(l);
            }
            if (st == null) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] demand = new int[list.size()];
        for(int i=0; i<list.size(); i++) demand[i] = list.get(i);
        
        Solution sol = new Solution();
        int[] res = sol.spans(demand);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
