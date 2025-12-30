class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private int L;

    public String kthMissingString(List<String> inserted, int L, int k) {
        this.L = L;
        TrieNode root = new TrieNode();

        // Build trie
        for (String word : inserted) {
            insert(root, word);
        }

        return dfs(root, 0, new int[]{k}, new StringBuilder());
    }

    private void insert(TrieNode root, String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }
        curr.isEnd = true;
    }

    private String dfs(TrieNode node, int depth, int[] k, StringBuilder current) {
        if (depth > L) return null;

        for (char c = 'a'; c <= 'z'; c++) {
            TrieNode child = node.children.get(c);

            // Check if this string is missing
            if (depth < L && (child == null || !child.isEnd)) {
                if (k[0] == 1) {
                    return current.toString() + c;
                }
                k[0]--;
            }

            // Recurse to children
            if (child != null && depth < L) {
                current.append(c);
                String result = dfs(child, depth + 1, k, current);
                if (result != null) return result;
                current.deleteCharAt(current.length() - 1);
            }
        }

        return null;
    }
}

// Time: O(26×L×k), Space: O(n×avgLen)
