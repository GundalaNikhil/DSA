import java.util.*;

class Solution {
    static class Node {
        int len;
        int link;
        Map<Character, Integer> next = new HashMap<>();

        Node(int len, int link) {
            this.len = len;
            this.link = link;
        }
    }

    public int countDistinctPalindromes(String s) {
        List<Node> tree = new ArrayList<>();
        // Node 0: root with len -1 (odd root)
        tree.add(new Node(-1, 0));
        // Node 1: root with len 0 (even root)
        tree.add(new Node(0, 0));
        
        int last = 1; // Start at even root (empty string)
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            int curr = last;
            
            // Find the longest palindromic suffix of s[0...i-1] that can be extended with c
            while (true) {
                int len = tree.get(curr).len;
                if (i - 1 - len >= 0 && s.charAt(i - 1 - len) == c) {
                    break;
                }
                curr = tree.get(curr).link;
            }
            
            if (tree.get(curr).next.containsKey(c)) {
                last = tree.get(curr).next.get(c);
                continue;
            }
            
            // Create new node
            int newNodeIdx = tree.size();
            tree.add(new Node(tree.get(curr).len + 2, 0));
            tree.get(curr).next.put(c, newNodeIdx);
            
            // Find suffix link for new node
            if (tree.get(newNodeIdx).len == 1) {
                tree.get(newNodeIdx).link = 1; // Link to even root
            } else {
                int temp = tree.get(curr).link;
                while (true) {
                    int len = tree.get(temp).len;
                    if (i - 1 - len >= 0 && s.charAt(i - 1 - len) == c) {
                        break;
                    }
                    temp = tree.get(temp).link;
                }
                tree.get(newNodeIdx).link = tree.get(temp).next.get(c);
            }
            
            last = newNodeIdx;
        }
        
        return tree.size() - 2; // Exclude the two roots
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.countDistinctPalindromes(s));
        }
        sc.close();
    }
}
