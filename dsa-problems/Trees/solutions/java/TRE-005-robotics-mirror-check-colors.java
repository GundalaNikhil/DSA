import java.util.*;

class Solution {
    public boolean mirrorCheck(int n, int[] values, int[] colors, int[] left, int[] right) {
        if (n == 0) return true;
        
        // 1. Check Structural & Value Symmetry
        if (!isSymmetric(0, values, left, right)) return false;
        
        // 2. Check Color Balance Level-by-Level
        if (left[0] == -1 && right[0] == -1) return true; // Single node
        if (left[0] == -1 || right[0] == -1) return false; // Should be caught by symmetry, but safe check
        
        return checkColorBalance(left[0], right[0], colors, left, right);
    }
    
    private boolean isSymmetric(int root, int[] values, int[] left, int[] right) {
        if (root == -1) return true;
        return checkMirror(left[root], right[root], values, left, right);
    }
    
    private boolean checkMirror(int u, int v, int[] values, int[] left, int[] right) {
        if (u == -1 && v == -1) return true;
        if (u == -1 || v == -1) return false;
        if (values[u] != values[v]) return false;
        return checkMirror(left[u], right[v], values, left, right) &&
               checkMirror(right[u], left[v], values, left, right);
    }
    
    private boolean checkColorBalance(int rootLeft, int rootRight, int[] colors, int[] left, int[] right) {
        Queue<Integer> qL = new LinkedList<>();
        Queue<Integer> qR = new LinkedList<>();
        qL.add(rootLeft);
        qR.add(rootRight);
        
        while (!qL.isEmpty() && !qR.isEmpty()) {
            int sizeL = qL.size();
            int sizeR = qR.size();
            if (sizeL != sizeR) return false; // Should be caught by symmetry
            
            int sumL = 0;
            int sumR = 0;
            
            for (int i = 0; i < sizeL; i++) {
                int u = qL.poll();
                sumL += colors[u];
                if (left[u] != -1) qL.add(left[u]);
                if (right[u] != -1) qL.add(right[u]);
            }
            
            for (int i = 0; i < sizeR; i++) {
                int v = qR.poll();
                sumR += colors[v];
                if (left[v] != -1) qR.add(left[v]);
                if (right[v] != -1) qR.add(right[v]);
            }
            
            if (sumL != sumR) return false;
        }
        
        return qL.isEmpty() && qR.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] colors = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            colors[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false");
        sc.close();
    }
}
