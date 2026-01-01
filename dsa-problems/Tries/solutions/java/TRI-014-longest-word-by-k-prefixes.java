import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public String longestWordWithKPrefixes(String[] words, int k) {
        // Build trie
        for (String word : words) {
            insert(word);
        }

        String result = "";
        int maxLen = 0;

        // Check each word
        for (String word : words) {
            int prefixCount = countPrefixes(word);
            if (prefixCount >= k) {
                // Update result if this word is longer or same length but lexicographically smaller
                if (word.length() > maxLen ||
                    (word.length() == maxLen && word.compareTo(result) < 0)) {
                    result = word;
                    maxLen = word.length();
                }
            }
        }

        return result;
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEnd = true;
    }

    private int countPrefixes(String word) {
        TrieNode node = root;
        int count = 0;

        // Traverse path, count END markers (excluding the final position)
        for (int i = 0; i < word.length(); i++) {
            node = node.children.get(word.charAt(i));
            if (i < word.length() - 1 && node.isEnd) {
                count++;
            }
        }

        return count;
    }
}

class Main {
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
        String result = solution.longestWordWithKPrefixes(words, k);

        System.out.println(result);
        sc.close();
    }
}
