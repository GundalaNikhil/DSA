import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    Set<Integer> wordIds = new HashSet<>();
}

class Solution {
    private TrieNode root = new TrieNode();
    private String longestPrefix = "";

    public String longestCommonPrefixAfterOneDeletion(String[] words) {
        int n = words.length;

        // Insert all variants into trie
        for (int wordId = 0; wordId < n; wordId++) {
            String word = words[wordId];

            // Insert original word
            insertWord(word, wordId);

            // Insert all single-deletion variants
            for (int i = 0; i < word.length(); i++) {
                String variant = word.substring(0, i) + word.substring(i + 1);
                insertWord(variant, wordId);
            }
        }

        // DFS to find longest prefix with all word IDs
        dfs(root, "", n);

        return longestPrefix;
    }

    private void insertWord(String word, int wordId) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.wordIds.add(wordId);
        }
    }

    private void dfs(TrieNode node, String prefix, int totalWords) {
        // If all words are represented at this node, update longest prefix
        if (node.wordIds.size() == totalWords) {
            if (prefix.length() > longestPrefix.length()) {
                longestPrefix = prefix;
            }
        }

        // Continue DFS
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            dfs(entry.getValue(), prefix + entry.getKey(), totalWords);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }

        Solution solution = new Solution();
        String result = solution.longestCommonPrefixAfterOneDeletion(words);

        System.out.println(result);
        sc.close();
    }
}
