import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

class WordMetadata {
    int frequency;
    int lastUsed;

    WordMetadata(int freq, int time) {
        this.frequency = freq;
        this.lastUsed = time;
    }
}

class Solution {
    private TrieNode root = new TrieNode();
    private Map<String, WordMetadata> metadata = new HashMap<>();

    public void insertWord(String word, int frequency, int timestamp) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
        metadata.put(word, new WordMetadata(frequency, timestamp));
    }

    public List<String> autocomplete(String prefix, int currentTime, int D, int k) {
        // Navigate to prefix node
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return new ArrayList<>(); // No matches
            }
            node = node.children.get(c);
        }

        // Collect all words with this prefix
        List<String> matches = new ArrayList<>();
        collectWords(node, prefix, matches);

        // Compute decay scores
        PriorityQueue<WordScore> heap = new PriorityQueue<>((a, b) -> {
            if (Math.abs(a.score - b.score) > 1e-9) {
                return Double.compare(b.score, a.score); // Descending by score
            }
            return a.word.compareTo(b.word); // Ascending lexicographically
        });

        for (String word : matches) {
            WordMetadata meta = metadata.get(word);
            double decay = Math.exp(-(currentTime - meta.lastUsed) / (double) D);
            double score = meta.frequency * decay;
            heap.offer(new WordScore(word, score));
        }

        // Extract top k
        List<String> result = new ArrayList<>();
        for (int i = 0; i < k && !heap.isEmpty(); i++) {
            result.add(heap.poll().word);
        }

        return result;
    }

    private void collectWords(TrieNode node, String prefix, List<String> result) {
        if (node.isEndOfWord) {
            result.add(prefix);
        }
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            collectWords(entry.getValue(), prefix + entry.getKey(), result);
        }
    }

    static class WordScore {
        String word;
        double score;

        WordScore(String w, double s) {
            word = w;
            score = s;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // Number of words
        Solution solution = new Solution();

        for (int i = 0; i < n; i++) {
            String word = sc.next();
            int freq = sc.nextInt();
            int time = sc.nextInt();
            solution.insertWord(word, freq, time);
        }

        String prefix = sc.next();
        int currentTime = sc.nextInt();
        int D = sc.nextInt();
        int k = sc.nextInt();

        List<String> result = solution.autocomplete(prefix, currentTime, D, k);
        System.out.println(result);

        sc.close();
    }
}
