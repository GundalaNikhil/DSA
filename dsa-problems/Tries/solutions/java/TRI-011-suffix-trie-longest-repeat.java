import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    int suffixCount = 0;  // Number of suffixes passing through this node
}

class Solution {
    private TrieNode root = new TrieNode();
    private int maxLength = 0;

    public int longestRepeatedSubstring(String s) {
        // Build suffix trie
        for (int i = 0; i < s.length(); i++) {
            insertSuffix(s.substring(i));
        }

        // Find longest path where 2+ suffixes pass through
        dfs(root, 0);
        return maxLength;
    }

    private void insertSuffix(String suffix) {
        TrieNode node = root;
        for (char c : suffix.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.suffixCount++;  // Increment count for each suffix passing through
        }
    }

    private void dfs(TrieNode node, int depth) {
        // A repeated substring exists if 2+ suffixes pass through this node
        if (node.suffixCount >= 2 && depth > 0) {
            maxLength = Math.max(maxLength, depth);
        }

        for (TrieNode child : node.children.values()) {
            dfs(child, depth + 1);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();

        Solution solution = new Solution();
        int result = solution.longestRepeatedSubstring(s);
        System.out.println(result);

        sc.close();
    }
}
