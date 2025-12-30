import java.util.*;

class Solution {
    private List<List<Integer>> adj;
    private int[] height, diam;
    private int[] upHeight, upDiam;
    private int maxDiam = 0;

    public int maxDiameterAfterRemoval(int n, int[][] edges) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        height = new int[n];
        diam = new int[n];
        upHeight = new int[n];
        upDiam = new int[n];

        dfs1(0, -1);
        dfs2(0, -1);

        return maxDiam;
    }

    private void dfs1(int u, int p) {
        int maxH1 = -1, maxH2 = -1;
        int maxD = 0;

        for (int v : adj.get(u)) {
            if (v == p) continue;
            dfs1(v, u);
            maxD = Math.max(maxD, diam[v]);
            if (height[v] > maxH1) {
                maxH2 = maxH1;
                maxH1 = height[v];
            } else if (height[v] > maxH2) {
                maxH2 = height[v];
            }
        }

        height[u] = 1 + maxH1; // -1 if leaf -> 0
        diam[u] = Math.max(maxD, (maxH1 + 1) + (maxH2 + 1));
    }

    private void dfs2(int u, int p) {
        if (p != -1) {
            // Calculate answer for edge (u, p)
            // Component 1: Subtree u -> diam[u]
            // Component 2: Rest -> upDiam[u]
            maxDiam = Math.max(maxDiam, Math.max(diam[u], upDiam[u]));
        }

        int k = adj.get(u).size();
        // Collect children data
        List<Integer> children = new ArrayList<>();
        for (int v : adj.get(u)) {
            if (v != p) children.add(v);
        }

        int m = children.size();
        int[] prefH = new int[m + 1];
        int[] suffH = new int[m + 1];
        int[] prefD = new int[m + 1];
        int[] suffD = new int[m + 1];

        Arrays.fill(prefH, -1); Arrays.fill(suffH, -1);
        
        for (int i = 0; i < m; i++) {
            int v = children.get(i);
            prefH[i + 1] = Math.max(prefH[i], height[v]);
            prefD[i + 1] = Math.max(prefD[i], diam[v]);
        }
        for (int i = m - 1; i >= 0; i--) {
            int v = children.get(i);
            suffH[i] = Math.max(suffH[i + 1], height[v]);
            suffD[i] = Math.max(suffD[i + 1], diam[v]);
        }

        // To compute diam passing through u from children
        // We need top 2 heights from prefix and suffix
        // This is tricky with just max.
        // Better: Precompute top 2 heights for u excluding v?
        // Or just use the prefix/suffix max height logic.
        // 1. upDiam[u]
        // 2. diam[other_child]
        // 3. upHeight[u] + 1 + height[other_child] + 1
        // 4. height[other_a] + 1 + height[other_b] + 1 (path through u)
        
        // Refine.
        // For child v at index i:
        // Max height among others: max(prefH[i], suffH[i+1])
        // Max diam among others: max(prefD[i], suffD[i+1])
        // Path through u using up: upHeight[u] + 1 + (max height among others) + 1
        // Path through u using two others: We need top 2 heights among others.
        // Prefix/Suffix only gives max.
        
        // Alternative: Just find top 3 heights and top 2 diams of all children + up.
        // Since degree can be large, we can't iterate all pairs.
        // But we only need to exclude 'v'.
        // So finding top 3 is enough.
        
        // Gather all "arms" from u:
        // 1. Upwards: len = upHeight[u] + 1, diam = upDiam[u]
        // 2. Children: len = height[child] + 1, diam = diam[child]
        
        // We want to form upDiam[v] using these, excluding v's arm.
        // New upDiam[v] = max(
        //    max(diam of other arms),
        //    sum of top 2 lengths of other arms
        // )
        // New upHeight[v] = 1 + max(length of other arms)
        
        // Collect all arms
        // Arm: {len, diam}
        // Child arm: {height[child], diam[child]} (height is length starting u going down)

        // height[u] represents max distance to leaf. The arm length is height[child] + 1.
        // upHeight[u] represents max distance from u upwards.
        
        List<int[]> arms = new ArrayList<>();
        if (p != -1) arms.add(new int[]{upHeight[u], upDiam[u]}); // Up arm
        
        for (int v : children) {
            arms.add(new int[]{height[v] + 1, diam[v]});
        }
        
        // Find top 3 lengths and top 2 diams
        // We need to pass this info to each child efficiently.
        // Prefix/Suffix is best.
        
        // Simplify.
        // upDiam[v] depends on:
        // 1. upDiam[u]
        // 2. diam[siblings]
        // 3. Longest path through u formed by (up + sibling) or (sibling + sibling).
        
        // Use the prefix/suffix approach for "path through u using siblings".
        // Max path through u using siblings = max(prefH[i] + suffH[i+1] + 2) ?? No.
        // We need max(height[a] + height[b] + 2) where a, b != v.
        
        // Compute top 3 heights and top 2 diams for every node in O(deg).
        // Then for each child, pick the best ones that are not it.
        
        int[] topHeights = {-1, -1, -1}; // values
        int[] topDiams = {-1, -1};
        
        // Include Up
        update(topHeights, upHeight[u]);
        update(topDiams, upDiam[u]);
        
        for (int v : children) {
            update(topHeights, height[v] + 1);
            update(topDiams, diam[v]);
        }
        
        for (int v : children) {
            // upHeight[v] = 1 + max(others height)
            int h1 = getMaxExcluding(topHeights, height[v] + 1);
            upHeight[v] = 1 + h1;
            
            // upDiam[v]
            int d1 = getMaxExcluding(topDiams, diam[v]); // Max diam of others
            
            // Path through u
            // Top 2 heights excluding v
            int[] h2 = getTop2Excluding(topHeights, height[v] + 1);
            int pathThroughU = h2[0] + h2[1]; // lengths are already from u
            
            upDiam[v] = Math.max(d1, pathThroughU);
            
            dfs2(v, u);
        }
    }
    
    private void update(int[] top, int val) {
        for (int i = 0; i < top.length; i++) {
            if (val > top[i]) {
                for (int j = top.length - 1; j > i; j--) {
                    top[j] = top[j-1];
                }
                top[i] = val;
                break;
            }
        }
    }
    
    private int getMaxExcluding(int[] top, int val) {
        if (top[0] == val) return top[1];
        return top[0];
    }
    
    private int[] getTop2Excluding(int[] top, int val) {
        int[] res = new int[2];
        int idx = 0;
        int count = 0;
        for (int x : top) {
            if (x == val && count == 0) { // Skip first occurrence
                count++;
                continue;
            }
            if (idx < 2) res[idx++] = x;
        }
        return res;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxDiameterAfterRemoval(n, edges));
        sc.close();
    }
}
