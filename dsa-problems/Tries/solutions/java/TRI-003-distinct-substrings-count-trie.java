class TrieNode {
    Map<Character, TrieNode> children;

    TrieNode() {
        children = new HashMap<>();
    }
}

class Solution {
    private int nodeCount = 0;

    public int countDistinctSubstrings(String s) {
        if (s == null || s.length() == 0) return 0;

        TrieNode root = new TrieNode();
        int n = s.length();

        // Insert all suffixes
        for (int i = 0; i < n; i++) {
            insertSuffix(root, s, i);
        }

        return nodeCount;
    }

    private void insertSuffix(TrieNode root, String s, int start) {
        TrieNode curr = root;

        for (int i = start; i < s.length(); i++) {
            char c = s.charAt(i);

            if (!curr.children.containsKey(c)) {
                curr.children.put(c, new TrieNode());
                nodeCount++;  // New node = new distinct substring
            }

            curr = curr.children.get(c);
        }
    }
}

// Time: O(n²), Space: O(n²)
