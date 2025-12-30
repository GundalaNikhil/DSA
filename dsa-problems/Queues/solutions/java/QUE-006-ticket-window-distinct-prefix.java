import java.util.*;

class Solution {
    public List<String> firstNonRepeating(String s) {
        int[] count = new int[26];
        Queue<Character> queue = new LinkedList<>();
        List<String> result = new ArrayList<>();
        
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
            queue.offer(c);
            
            while (!queue.isEmpty() && count[queue.peek() - 'a'] > 1) {
                queue.poll();
            }
            
            if (queue.isEmpty()) {
                result.add("#");
            } else {
                result.add(String.valueOf(queue.peek()));
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            List<String> result = solution.firstNonRepeating(s);
            System.out.println(String.join(" ", result));
        }
        sc.close();
    }
}
