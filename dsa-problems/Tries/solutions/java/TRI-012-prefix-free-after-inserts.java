import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();
    
    public boolean insert(String number) {
        TrieNode node = root;
        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            
            // If current node is end of another number, new number extends it
            if (node.isEnd) return false;
            
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        
        // If node has children, this number is prefix of existing numbers
        if (!node.children.isEmpty()) return false;
        
        node.isEnd = true;
        return true;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        
        Solution solution = new Solution();
        List<Boolean> results = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            String number = sc.nextLine().trim();
            results.add(solution.insert(number));
        }
        
        System.out.print("[");
        for (int i = 0; i < results.size(); i++) {
            System.out.print(results.get(i));
            if (i < results.size() - 1) System.out.print(",");
        }
        System.out.println("]");
        sc.close();
    }
}
