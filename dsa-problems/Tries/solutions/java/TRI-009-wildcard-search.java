import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public void insertWord(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEnd = true;
    }

    public boolean search(String pattern) {
        return dfs(root, pattern, 0);
    }

    private boolean dfs(TrieNode node, String pattern, int index) {
        if (index == pattern.length()) {
            return node.isEnd;
        }

        char c = pattern.charAt(index);

        if (c == '?') {
            // Match any single character
            for (TrieNode child : node.children.values()) {
                if (dfs(child, pattern, index + 1)) {
                    return true;
                }
            }
            return false;
        } else if (c == '*') {
            // Match zero or more characters
            // Try matching 0 characters
            if (dfs(node, pattern, index + 1)) {
                return true;
            }
            // Try matching 1+ characters
            for (TrieNode child : node.children.values()) {
                if (dfs(child, pattern, index)) {
                    return true;
                }
            }
            return false;
        } else {
            // Regular character
            if (!node.children.containsKey(c)) {
                return false;
            }
            return dfs(node.children.get(c), pattern, index + 1);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        Solution solution = new Solution();
        for (int i = 0; i < n; i++) {
            solution.insertWord(sc.nextLine().trim());
        }

        String pattern = sc.nextLine().trim();
        boolean result = solution.search(pattern);

        System.out.println(result);

        sc.close();
    }
}
