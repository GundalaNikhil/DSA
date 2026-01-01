import java.util.*;
import java.io.*;

class Solution {
    public int countUnsafe(int[] d) {
        int count = 0;
        for (int i = 0; i < d.length - 1; i++) {
            if (d[i+1] > d[i]) {
                count++;
            }
        }
        return count;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        int n = Integer.parseInt(line.trim());
        
        // Read Array (robust)
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
        
        int[] d = new int[list.size()];
        for(int i=0; i<list.size(); i++) d[i] = list.get(i);
        
        Solution sol = new Solution();
        System.out.println(sol.countUnsafe(d));
    }
}
