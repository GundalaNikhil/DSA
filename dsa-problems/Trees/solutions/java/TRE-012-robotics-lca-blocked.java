import java.util.*;

class Solution {
    public int lcaBlocked(int n, int[] values, int[] blocked, int[] left, int[] right, int u, int v) {
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        
        // 1. Build Parent Map using BFS
        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        
        while (!q.isEmpty()) {
            int curr = q.poll();
            if (left[curr] != -1) {
                parent[left[curr]] = curr;
                q.offer(left[curr]);
            }
            if (right[curr] != -1) {
                parent[right[curr]] = curr;
                q.offer(right[curr]);
            }
        }
        
        // 2. Find Standard LCA using Ancestor Set
        Set<Integer> ancestors = new HashSet<>();
        int curr = u;
        while (curr != -1) {
            ancestors.add(curr);
            curr = parent[curr];
        }
        
        int lca = -1;
        curr = v;
        while (curr != -1) {
            if (ancestors.contains(curr)) {
                lca = curr;
                break;
            }
            curr = parent[curr];
        }
        
        if (lca == -1) return -1; // Should not happen if u, v in tree
        
        // 3. Climb up if blocked
        while (lca != -1 && blocked[lca] == 1) {
            lca = parent[lca];
        }
        
        return (lca != -1) ? values[lca] : -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] blocked = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            blocked[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        int u = sc.nextInt();
        int v = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.lcaBlocked(n, values, blocked, left, right, u, v));
        sc.close();
    }
}
