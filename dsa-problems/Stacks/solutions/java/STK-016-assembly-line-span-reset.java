import java.util.*;
import java.io.*;

class Solution {
    public int[] spans(int[] counts) {
        int n = counts.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && counts[stack.peek()] < counts[i]) {
                stack.pop();
            }
            
            if (stack.isEmpty()) {
                result[i] = i + 1;
            } else {
                result[i] = i - stack.peek();
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
        
        int n = Integer.parseInt(line.trim());
        
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] counts = new int[list.size()];
        for(int i=0; i<list.size(); i++) counts[i] = list.get(i);
        
        Solution sol = new Solution();
        int[] res = sol.spans(counts);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
