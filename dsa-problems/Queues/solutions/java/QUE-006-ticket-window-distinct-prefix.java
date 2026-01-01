import java.util.*;

class Solution {
    public List<String> firstNonRepeating(String s) {
        Map<Character, Integer> count = new HashMap<>();
        Queue<Character> queue = new LinkedList<>();
        List<String> result = new ArrayList<>();

        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
            queue.offer(c);

            while (!queue.isEmpty() && count.get(queue.peek()) > 1) {
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

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            if (!sb.isEmpty()) sb.append("\n");
            sb.append(line);
        }
        sc.close();

        String s = sb.toString();
        // Remove leading/trailing whitespace
        s = s.replaceAll("^\\s+|\\s+$", "");

        if (!s.isEmpty()) {
            Solution solution = new Solution();
            List<String> result = solution.firstNonRepeating(s);
            System.out.println(String.join(" ", result));
        }
    }
}
