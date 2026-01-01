import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();
    private int nodeCount = 1; // Start with root

    public int countTrieNodes(String[] words) {
        for (String word : words) {
            insert(word);
        }
        return nodeCount;
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                node.children.put(c, new TrieNode());
                nodeCount++;
            }
            node = node.children.get(c);
        }
        node.isEnd = true;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            if (sc.hasNext()) {
                words[i] = sc.next();
            } else {
                words[i] = "";
            }
        }

        Solution solution = new Solution();
        int result = solution.countTrieNodes(words);

        System.out.println(result);

        sc.close();
    }
}
