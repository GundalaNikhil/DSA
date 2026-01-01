import java.util.*;
import java.io.*;

class Solution {
    int[] tree;
    int[] h;
    int n;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = h[start];
        } else {
            int mid = (start + end) / 2;
            build(2 * node, start, mid);
            build(2 * node + 1, mid + 1, end);
            tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
        }
    }

    int findLastLess(int node, int start, int end, int l, int r, int val) {
        if (l > r || tree[node] >= val) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        int mid = (start + end) / 2;
        int res = -1;
        if (mid < r) {
            res = findLastLess(2 * node + 1, mid + 1, end, l, r, val);
        }
        if (res != -1) return res;
        if (l <= mid) {
            return findLastLess(2 * node, start, mid, l, r, val);
        }
        return -1;
    }

    int findFirstLess(int node, int start, int end, int l, int r, int val) {
        if (l > r || tree[node] >= val) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        int mid = (start + end) / 2;
        int res = -1;
        if (l <= mid) {
            res = findFirstLess(2 * node, start, mid, l, r, val);
        }
        if (res != -1) return res;
        if (mid < r) {
            return findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
        }
        return -1;
    }

    public long maxAreaWithBoost(int[] h, int b) {
        this.h = h;
        this.n = h.length;
        this.tree = new int[4 * n];
        build(1, 0, n - 1);
        
        long maxArea = 0;
        
        for (int i = 0; i < n; i++) {
            // Case 1: Boosted h[i]
            long boostedH = (long)h[i] + b;
            int L = findLastLess(1, 0, n - 1, 0, i - 1, (int)Math.min(boostedH, Integer.MAX_VALUE)); 
            // Caution: boostedH might exceed int, but tree stores ints.
            // If boostedH > all ints in tree, logic works (tree[node] < val).
            // However, findLastLess expects int val.
            // If boostedH > Integer.MAX_VALUE, then tree[node] < val is always true if tree has only valid ints.
            // So capping at MAX_VALUE is safe if h[i] are standard ints.
            // Wait, h[i] could be large? Problem constraints? Standard int array.
            
            int R = findFirstLess(1, 0, n - 1, i + 1, n - 1, (int)Math.min(boostedH, Integer.MAX_VALUE));
            if (R == -1) R = n;
            maxArea = Math.max(maxArea, boostedH * (R - L - 1));
            
            // Case 2: Normal h[i]
            long normalH = h[i];
            int L1 = findLastLess(1, 0, n - 1, 0, i - 1, (int)normalH);
            int R1 = findFirstLess(1, 0, n - 1, i + 1, n - 1, (int)normalH);
            if (R1 == -1) R1 = n;
            
            maxArea = Math.max(maxArea, normalH * (R1 - L1 - 1));
            
            if (L1 != -1 && (long)h[L1] + b >= normalH) {
                int L2 = findLastLess(1, 0, n - 1, 0, L1 - 1, (int)normalH);
                maxArea = Math.max(maxArea, normalH * (R1 - L2 - 1));
            }
            
            if (R1 != n && (long)h[R1] + b >= normalH) {
                int R2 = findFirstLess(1, 0, n - 1, R1 + 1, n - 1, (int)normalH);
                if (R2 == -1) R2 = n;
                maxArea = Math.max(maxArea, normalH * (R2 - L1 - 1));
            }
        }
        return maxArea;
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
        
        int[] h = new int[list.size()];
        for(int i=0; i<list.size(); i++) h[i] = list.get(i);
        
        // Read B
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int b = 0;
        if (st.hasMoreTokens()) {
            b = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        System.out.println(sol.maxAreaWithBoost(h, b));
    }
}
