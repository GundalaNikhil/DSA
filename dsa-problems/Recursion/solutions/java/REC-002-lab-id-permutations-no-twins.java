import java.util.*;

class Solution {
    public List<String> generatePermutations(String s) {
        List<String> result = new ArrayList<>();
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        boolean[] used = new boolean[chars.length];
        backtrack(chars, used, new StringBuilder(), result);
        return result;
    }

    private void backtrack(char[] chars, boolean[] used, StringBuilder current, List<String> result) {
        if (current.length() == chars.length) {
            result.add(current.toString());
            return;
        }

        for (int i = 0; i < chars.length; i++) {
            // Skip used characters
            if (used[i]) continue;

            // Skip duplicates: if current is same as previous and previous was not used,
            // it means we are in a new branch for the same character value, which leads to duplicates.
            if (i > 0 && chars[i] == chars[i - 1] && !used[i - 1]) continue;

            // Constraint: No adjacent twins
            if (current.length() > 0 && current.charAt(current.length() - 1) == chars[i]) continue;

            used[i] = true;
            current.append(chars[i]);
            backtrack(chars, used, current, result);
            current.deleteCharAt(current.length() - 1);
            used[i] = false;
        }
    }
}





class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Solution sol = new Solution();
        List<String> res = sol.generatePermutations(s);
        for(String out_s : res) System.out.println(out_s);
        if(res.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
