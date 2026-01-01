import java.util.*;

class Solution {
    private long B, M;
    private int L;
    private Map<Long, String> seen;
    
    public String[] findCollision(long B, long M, int L) {
        this.B = B;
        this.M = M;
        this.L = L;
        this.seen = new HashMap<>();
        
        return dfs(new StringBuilder());
    }
    
    private String[] dfs(StringBuilder sb) {
        if (sb.length() == L) {
            String s = sb.toString();
            long h = computeHash(s);
            if (seen.containsKey(h)) {
                return new String[]{seen.get(h), s};
            }
            seen.put(h, s);
            return null;
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            sb.append(c);
            String[] res = dfs(sb);
            if (res != null) return res;
            sb.setLength(sb.length() - 1);
            
            // For M=10^9, expected map size is approximately sqrt(M) ≈ 32k.
            // With L≤8, we have 26^8 possible strings, far exceeding M.
            // By the pigeonhole principle, collisions must exist for these inputs.
        }
        return null;
    }
    
    private long computeHash(String s) {
        long h = 0;
        for (char c : s.toCharArray()) {
            h = (h * B + c) % M;
        }
        return h;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long B = sc.nextLong();
            long M = sc.nextLong();
            int L = sc.nextInt();
            
            Solution solution = new Solution();
            String[] result = solution.findCollision(B, M, L);
            
            if (result != null) {
                System.out.println(result[0]);
                System.out.println(result[1]);
            }
        }
        sc.close();
    }
}
