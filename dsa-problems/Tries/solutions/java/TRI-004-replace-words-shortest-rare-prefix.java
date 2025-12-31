class TrieNode {
    Map<Character, TrieNode> children;
    String word;
    int rarity;

    TrieNode() {
        children = new HashMap<>();
        word = null;
        rarity = Integer.MAX_VALUE;
    }
}

class Solution {
    private TrieNode root;

    public String replaceWords(Map<String, Integer> dictionary, String sentence) {
        root = new TrieNode();

        // Build trie
        for (Map.Entry<String, Integer> entry : dictionary.entrySet()) {
            insert(entry.getKey(), entry.getValue());
        }

        // Process sentence
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            if (i > 0) result.append(" ");
            result.append(findReplacement(words[i]));
        }

        return result.toString();
    }

    private void insert(String word, int rarity) {
        TrieNode curr = root;

        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }

        // Update only if this is better
        if (rarity < curr.rarity ||
            (rarity == curr.rarity && (curr.word == null || word.length() < curr.word.length()))) {
            curr.word = word;
            curr.rarity = rarity;
        }
    }

    private String findReplacement(String word) {
        TrieNode curr = root;
        String best = null;
        int bestRarity = Integer.MAX_VALUE;

        for (char c : word.toCharArray()) {
            if (!curr.children.containsKey(c)) break;

            curr = curr.children.get(c);

            if (curr.word != null) {
                if (curr.rarity < bestRarity ||
                    (curr.rarity == bestRarity && curr.word.length() < best.length())) {
                    best = curr.word;
                    bestRarity = curr.rarity;
                }
            }
        }

        return best != null ? best : word;
    }
}

// Time: O(M×K + N×L), Space: O(M×K)
