import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    int count = 0;
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public int[] findMinimumPrefixLengths(String[] words) {
        // Build trie with counts
        for (String word : words) {
            insert(word);
        }

        // Find minimum prefix length for each word
        int[] result = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            result[i] = findMinLength(words[i]);
        }

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

    private int findMinLength(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            node = node.children.get(word.charAt(i));
            if (node.count == 1) {
                return i + 1;
            }
        }
        return word.length();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        int[] result = solution.findMinimumPrefixLengths(words);

        System.out.print("[");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(",");
        }
        System.out.println("]");

        sc.close();
    }
}
