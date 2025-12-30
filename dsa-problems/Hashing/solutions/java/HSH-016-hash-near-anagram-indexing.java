import java.util.*;

class Solution {
    class UnionFind {
        int[] parent;
        int count;
        
        public UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
            count = n;
        }
        
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent[rootX] = rootY;
                count--;
            }
        }
    }
    
    public int countNearAnagramGroups(String[] words) {
        int n = words.length;
        UnionFind uf = new UnionFind(n);
        Map<String, List<Integer>> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            char[] chars = words[i].toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);
            
            // Generate all reduced forms
            // Since word is sorted, removing char at j maintains sorted order mostly
            // but duplicates might exist.
            
            for (int j = 0; j < sortedWord.length(); j++) {
                String reduced = sortedWord.substring(0, j) + sortedWord.substring(j + 1);
                map.putIfAbsent(reduced, new ArrayList<>());
                map.get(reduced).add(i);
            }
        }
        
        for (List<Integer> group : map.values()) {
            int first = group.get(0);
            for (int k = 1; k < group.size(); k++) {
                uf.union(first, group.get(k));
            }
        }
        
        return uf.count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            sc.nextLine();
            String[] words = new String[n];
            for (int i = 0; i < n; i++) {
                words[i] = sc.nextLine();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.countNearAnagramGroups(words));
        }
        sc.close();
    }
}
