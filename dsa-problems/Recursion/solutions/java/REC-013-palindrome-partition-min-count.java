import java.util.*;

class Solution {
    int N, L;
    String S;
    boolean[][] is_pal;
    List<String> best_partition;
    int current_min;

    public String minPalindromePartitions(String s, int l) {
        S = s;
        L = l;
        N = s.length();
        
        is_pal = new boolean[N][N];
        for (int len = 1; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1;
                if (S.charAt(i) == S.charAt(j)) {
                    if (len <= 2 || is_pal[i + 1][j - 1]) {
                        is_pal[i][j] = true;
                    }
                }
            }
        }

        current_min = N + 1;
        best_partition = null;
        backtrack(0, new ArrayList<>());
        
        if (best_partition == null) {
            StringBuilder sb = new StringBuilder();
            for(int i=0; i<N; i++) {
                sb.append(S.charAt(i));
                if(i < N-1) sb.append(" ");
            }
            return sb.toString();
        }
        
        return String.join(" ", best_partition);
    }

    private void backtrack(int start, List<String> current) {
        if (start == N) {
            int count = current.size();
            if (count < current_min) {
                current_min = count;
                best_partition = new ArrayList<>(current);
            }
            return;
        }

        if (current.size() >= current_min) return;

        int max_end = Math.min(start + L, N);
        for (int end = start; end < max_end; end++) {
            if (is_pal[start][end]) {
                current.add(S.substring(start, end + 1));
                backtrack(end + 1, current);
                current.remove(current.size() - 1);
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNext()) return;
        String s = sc.next();
        if(!sc.hasNextInt()) return;
        int L = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.minPalindromePartitions(s, L));
        sc.close();
    }
}
