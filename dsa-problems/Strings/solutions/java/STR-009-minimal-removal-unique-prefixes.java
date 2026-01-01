import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    List<String> strings = new ArrayList<>();
}

class Solution {
    private int totalDeletions = 0;

    public int minimalRemovalUniquePrefixes(int L, List<String> strings) {
        TrieNode root = new TrieNode();

        // Build trie
        for (String s : strings) {
            TrieNode node = root;
            for (int i = 0; i < Math.min(s.length(), L); i++) {
                char c = s.charAt(i);
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
            }
            node.strings.add(s);
        }

        // Find conflicts
        totalDeletions = 0;
        findConflicts(root, 0, L);
        return totalDeletions;
    }

    private void findConflicts(TrieNode node, int depth, int L) {
        if (depth == L) {
            if (node.strings.size() > 1) {
                // Sort by length descending
                node.strings.sort((a, b) -> Integer.compare(b.length(), a.length()));

                // Delete all except longest
                for (int i = 1; i < node.strings.size(); i++) {
                    String s = node.strings.get(i);
                    if (s.length() >= L) {
                        totalDeletions += s.length() - (L - 1);
                    }
                }
            }
            return;
        }

        for (TrieNode child : node.children.values()) {
            findConflicts(child, depth + 1, L);
        }
    }
}

















class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        int strings_n = sc.nextInt();
        List<String> strings = new ArrayList<>();
        for(int i=0; i<strings_n; i++) strings.add(sc.next());
        Solution sol = new Solution();
        System.out.println(sol.minimalRemovalUniquePrefixes(L, strings));
        sc.close();
    }
}
