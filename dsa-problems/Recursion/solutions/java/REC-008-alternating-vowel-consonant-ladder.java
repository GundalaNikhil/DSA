import java.util.*;

class Solution {
    Set<String> results;
    boolean[] used;
    String S;
    int N;

    public List<String> getAlternatingPermutations(String s) {
        S = s;
        N = s.length();
        results = new TreeSet<>(); // TreeSet for sorted order
        used = new boolean[N];
        backtrack(new StringBuilder());
        return new ArrayList<>(results);
    }

    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }

    private void backtrack(StringBuilder current) {
        if (current.length() == N) {
            results.add(current.toString());
            return;
        }

        char lastChar = current.length() > 0 ? current.charAt(current.length() - 1) : '\0';
        boolean lastIsVowel = current.length() > 0 ? isVowel(lastChar) : false;

        for (int i = 0; i < N; i++) {
            if (!used[i]) {
                char nextChar = S.charAt(i);
                boolean nextIsVowel = isVowel(nextChar);
                
                if (current.length() == 0 || lastIsVowel != nextIsVowel) {
                    used[i] = true;
                    current.append(nextChar);
                    backtrack(current);
                    current.deleteCharAt(current.length() - 1);
                    used[i] = false;
                }
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNext()) return;
        String s = sc.next();
        
        Solution sol = new Solution();
        List<String> res = sol.getAlternatingPermutations(s);
        if(res.isEmpty()) {
            System.out.println("NONE");
        } else {
            for(String p : res) System.out.println(p);
        }
        sc.close();
    }
}
