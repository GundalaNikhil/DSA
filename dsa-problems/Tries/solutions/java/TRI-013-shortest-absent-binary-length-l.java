import java.util.*;

class TrieNode {
    TrieNode[] children = new TrieNode[2];  // 0 and 1
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public String findShortestAbsent(String[] binaryStrings, int L) {
        // Early exit if all possible strings exist
        if (binaryStrings.length == Math.pow(2, L)) {
            return "";
        }

        // Build trie
        for (String s : binaryStrings) {
            insert(s);
        }

        // DFS to find first missing
        return dfs(root, "", L);
    }

    private void insert(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            int idx = c - '0';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    private String dfs(TrieNode node, String path, int L) {
        // Reached target length
        if (path.length() == L) {
            return node.isEnd ? null : path;
        }

        // Try '0' first (lexicographically smaller)
        if (node.children[0] == null) {
            // Missing '0' path - fill rest with '0's
            StringBuilder result = new StringBuilder(path);
            result.append('0');
            while (result.length() < L) {
                result.append('0');
            }
            return result.toString();
        }

        String result = dfs(node.children[0], path + '0', L);
        if (result != null) return result;

        // Try '1'
        if (node.children[1] == null) {
            // Missing '1' path - fill rest with '0's
            StringBuilder sb = new StringBuilder(path);
            sb.append('1');
            while (sb.length() < L) {
                sb.append('0');
            }
            return sb.toString();
        }

        return dfs(node.children[1], path + '1', L);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int L = sc.nextInt();
        int n = sc.nextInt();

        String[] binaryStrings = new String[n];
        for (int i = 0; i < n; i++) {
            if (sc.hasNext()) {
                binaryStrings[i] = sc.next();
            } else {
                binaryStrings[i] = "";
            }
        }

        Solution solution = new Solution();
        String result = solution.findShortestAbsent(binaryStrings, L);

        System.out.println(result.isEmpty() ? "" : result);
        sc.close();
    }
}
