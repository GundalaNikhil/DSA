import java.util.*;

class Solution {
    static class Node {
        int count;
        Node left, right;
        
        Node(int count, Node left, Node right) {
            this.count = count;
            this.left = left;
            this.right = right;
        }
    }
    
    private Node[] roots;
    private int[] unique;
    
    public int[] kthPrefix(int[] arr, int[][] queries) {
        int n = arr.length;
        
        // Coordinate Compression
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        // Remove duplicates
        int m = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sorted[i] != sorted[i-1]) {
                m++;
            }
        }
        unique = new int[m];
        m = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sorted[i] != sorted[i-1]) {
                unique[m++] = sorted[i];
            }
        }
        
        // Build Persistent Segment Tree
        roots = new Node[n];
        Node nullNode = build(0, m - 1);
        
        for (int i = 0; i < n; i++) {
            int idx = Arrays.binarySearch(unique, arr[i]);
            Node prev = (i == 0) ? nullNode : roots[i - 1];
            roots[i] = update(prev, 0, m - 1, idx);
        }
        
        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int r = queries[i][0];
            int k = queries[i][1];
            int idx = query(roots[r], 0, m - 1, k);
            results[i] = unique[idx];
        }
        return results;
    }
    
    private Node build(int l, int r) {
        if (l == r) return new Node(0, null, null);
        int mid = (l + r) / 2;
        return new Node(0, build(l, mid), build(mid + 1, r));
    }
    
    private Node update(Node node, int l, int r, int idx) {
        if (l == r) {
            return new Node(node.count + 1, null, null);
        }
        int mid = (l + r) / 2;
        Node left = node.left;
        Node right = node.right;
        if (idx <= mid) {
            left = update(left, l, mid, idx);
        } else {
            right = update(right, mid + 1, r, idx);
        }
        return new Node(left.count + right.count, left, right);
    }
    
    private int query(Node node, int l, int r, int k) {
        if (l == r) return l;
        int mid = (l + r) / 2;
        int leftCount = node.left.count;
        if (k <= leftCount) {
            return query(node.left, l, mid, k);
        } else {
            return query(node.right, mid + 1, r, k - leftCount);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[][] queries = new int[q][2];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // PREFIX
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.kthPrefix(arr, queries);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
