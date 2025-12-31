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

    public boolean hasEditDistance1(String query) {
        return dfs(root, query, 0, 0);
    }

    private boolean dfs(TrieNode node, String query, int index, int edits) {
        // If we've used more than 1 edit, prune
        if (edits > 1) {
            return false;
        }

        // If we've consumed the query
        if (index == query.length()) {
            // Check if this is a word end and we used exactly 1 edit
            // OR we can delete remaining trie characters (each is 1 edit)
            if (node.isEnd && edits == 1) {
                return true;
            }
            // Can we reach a word by deleting one more char?
            if (edits == 0) {
                for (TrieNode child : node.children.values()) {
                    if (child.isEnd) {
                        return true;
                    }
                }
            }
            return false;
        }

        char c = query.charAt(index);

        // 1. Match current character (no edit)
        if (node.children.containsKey(c)) {
            if (dfs(node.children.get(c), query, index + 1, edits)) {
                return true;
            }
        }

        // Only try edit operations if budget allows
        if (edits < 1) {
            // 2. Substitute (replace query char with trie char)
            for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
                if (entry.getKey() != c) {
                    if (dfs(entry.getValue(), query, index + 1, edits + 1)) {
                        return true;
                    }
                }
            }

            // 3. Delete from query (insert into result)
            if (dfs(node, query, index + 1, edits + 1)) {
                return true;
            }

            // 4. Insert into query (delete from trie)
            for (TrieNode child : node.children.values()) {
                if (dfs(child, query, index, edits + 1)) {
                    return true;
                }
            }
        }

        return false;
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

        String query = sc.nextLine().trim();
        boolean result = solution.hasEditDistance1(query);

        System.out.println(result);

        sc.close();
    }
}
