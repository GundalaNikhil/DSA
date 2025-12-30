import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new TreeMap<>();  // TreeMap for alphabetical order
    boolean isEnd = false;
    int count = 0;  // Number of strings in this subtree
}

class Solution {
    private TrieNode root = new TrieNode();
    private String result = "";
    private int remaining;

    public String kthSmallest(String[] words, int k) {
        // Build trie with counts
        for (String word : words) {
            insert(word);
        }

        remaining = k;
        dfs(root, new StringBuilder());

        return result;
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.count++;
        }
        node.isEnd = true;
    }

    private boolean dfs(TrieNode node, StringBuilder path) {
        if (node.isEnd) {
            remaining--;
            if (remaining == 0) {
                result = path.toString();
                return true;
            }
        }

        // Traverse children in alphabetical order (TreeMap ensures this)
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            char c = entry.getKey();
            TrieNode child = entry.getValue();

            // Check if k-th string is in this subtree
            if (child.count >= remaining) {
                path.append(c);
                if (dfs(child, path)) {
                    return true;
                }
                path.deleteCharAt(path.length() - 1);
            } else {
                // Skip this entire subtree
                remaining -= child.count;
            }
        }

        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        String result = solution.kthSmallest(words, k);

        System.out.println(result);
        sc.close();
    }
}
