import java.util.*;

class Solution {
    static class Node {
        Node[] children = new Node[26];
        Node fail;
        Node output; // Nearest terminal node via fail links
        List<Integer> lens = new ArrayList<>();
        List<Long> weights = new ArrayList<>();
    }

    public long maxCooldownScore(String text, String[] patterns, long[] weights, int g) {
        Node root = new Node();
        
        // 1. Build Trie
        for (int i = 0; i < patterns.length; i++) {
            Node curr = root;
            for (char c : patterns[i].toCharArray()) {
                int idx = c - 'a';
                if (curr.children[idx] == null) curr.children[idx] = new Node();
                curr = curr.children[idx];
            }
            curr.lens.add(patterns[i].length());
            curr.weights.add(weights[i]);
        }
        
        // 2. Build Failure Links
        Queue<Node> q = new LinkedList<>();
        for (int i = 0; i < 26; i++) {
            if (root.children[i] != null) {
                root.children[i].fail = root;
                q.add(root.children[i]);
            } else {
                root.children[i] = root;
            }
        }
        
        while (!q.isEmpty()) {
            Node curr = q.poll();
            // Compute output link
            if (!curr.fail.lens.isEmpty()) curr.output = curr.fail;
            else curr.output = curr.fail.output;
            
            for (int i = 0; i < 26; i++) {
                if (curr.children[i] != null) {
                    curr.children[i].fail = curr.fail.children[i];
                    q.add(curr.children[i]);
                } else {
                    curr.children[i] = curr.fail.children[i];
                }
            }
        }
        
        // 3. DP
        int n = text.length();
        long[] dp = new long[n + 1];
        Node curr = root;
        
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i];
            curr = curr.children[text.charAt(i) - 'a'];
            
            Node temp = curr;
            while (temp != root) {
                if (!temp.lens.isEmpty()) {
                    for (int k = 0; k < temp.lens.size(); k++) {
                        int len = temp.lens.get(k);
                        long w = temp.weights.get(k);
                        int prevIdx = i + 1 - len - g;
                        long prevScore = (prevIdx < 0) ? 0 : dp[prevIdx];
                        dp[i + 1] = Math.max(dp[i + 1], prevScore + w);
                    }
                }
                if (temp.output == null) break;
                temp = temp.output;
            }
        }
        
        return dp[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int k = sc.nextInt();
        String[] patterns = new String[k];
        long[] weights = new long[k];
        for (int i = 0; i < k; i++) {
            patterns[i] = sc.next();
            weights[i] = sc.nextLong();
        }
        int g = sc.nextInt();
        String text = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.maxCooldownScore(text, patterns, weights, g));
        sc.close();
    }
}
