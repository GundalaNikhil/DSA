import java.util.*;
import java.io.*;

class Solution {
    private int findNearestGreater(List<Integer> stack, int val, int[] arr) {
        // Stack stores indices. 
        // arr[stack[i]] is decreasing as i increases.
        // We want largest index (largest i) such that arr[stack[i]] > val.
        // Since decreasing, valid prefix: [0 ... k]. We want k.
        
        if (stack.isEmpty()) return -1;
        
        int l = 0, r = stack.size() - 1;
        int ansIdx = -1;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int idx = stack.get(mid);
            if (arr[idx] > val) {
                ansIdx = idx;
                l = mid + 1; // Try to find rightmost (larger index/smaller value that is still > val)
            } else {
                r = mid - 1;
            }
        }
        return ansIdx;
    }

    public int[] prevGreaterOppositeParity(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        
        List<Integer> evenStack = new ArrayList<>();
        List<Integer> oddStack = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int val = arr[i];
            
            if (val % 2 == 0) {
                // Look in Odd
                int idx = findNearestGreater(oddStack, val, arr);
                if (idx != -1) result[i] = arr[idx];
                
                // Update Even
                while (!evenStack.isEmpty() && arr[evenStack.get(evenStack.size() - 1)] <= val) {
                    evenStack.remove(evenStack.size() - 1);
                }
                evenStack.add(i);
            } else {
                // Look in Even
                int idx = findNearestGreater(evenStack, val, arr);
                if (idx != -1) result[i] = arr[idx];
                
                // Update Odd
                while (!oddStack.isEmpty() && arr[oddStack.get(oddStack.size() - 1)] <= val) {
                    oddStack.remove(oddStack.size() - 1);
                }
                oddStack.add(i);
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N (ignores empty lines)
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        String startLine = line;
        // The numbers could be on same line or next line
        // Use StringTokenizer
        StringTokenizer st = new StringTokenizer(startLine);
        if (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int loaded = 0;
        
        while (loaded < n) {
            if (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (st.hasMoreTokens()) {
                arr[loaded++] = Integer.parseInt(st.nextToken());
            }
        }
        
        Solution sol = new Solution();
        int[] res = sol.prevGreaterOppositeParity(arr);
        for (int v : res) {
            System.out.println(v);
        }
    }
}
