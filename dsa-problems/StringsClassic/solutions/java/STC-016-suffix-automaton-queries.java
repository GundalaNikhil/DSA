import java.util.*;

class Solution {
    static class State {
        int len, link;
        Map<Character, Integer> next = new HashMap<>();
        long cnt = 0;
        boolean isClone = false;
    }

    State[] st;
    int sz, last;

    public long[] countOccurrences(String s, String[] queries) {
        int n = s.length();
        st = new State[n * 2 + 5]; // Max states 2*n
        for(int i=0; i<st.length; i++) st[i] = new State();
        
        st[0].len = 0;
        st[0].link = -1;
        sz = 1;
        last = 0;
        
        // 1. Build SAM
        for (char c : s.toCharArray()) {
            extend(c);
        }
        
        // 2. Sort by length descending
        List<Integer> nodes = new ArrayList<>();
        for (int i = 1; i < sz; i++) nodes.add(i);
        nodes.sort((a, b) -> st[b].len - st[a].len);
        
        // 3. Propagate counts
        for (int u : nodes) {
            if (st[u].link != -1) {
                st[st[u].link].cnt += st[u].cnt;
            }
        }
        
        // 4. Answer queries
        long[] ans = new long[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int curr = 0;
            boolean ok = true;
            for (char c : queries[i].toCharArray()) {
                if (!st[curr].next.containsKey(c)) {
                    ok = false;
                    break;
                }
                curr = st[curr].next.get(c);
            }
            if (ok) ans[i] = st[curr].cnt;
            else ans[i] = 0;
        }
        
        return ans;
    }
    
    void extend(char c) {
        int cur = sz++;
        st[cur].len = st[last].len + 1;
        st[cur].cnt = 1; // Original state
        st[cur].isClone = false;
        
        int p = last;
        while (p != -1 && !st[p].next.containsKey(c)) {
            st[p].next.put(c, cur);
            p = st[p].link;
        }
        
        if (p == -1) {
            st[cur].link = 0;
        } else {
            int q = st[p].next.get(c);
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = sz++;
                st[clone].len = st[p].len + 1;
                st[clone].next = new HashMap<>(st[q].next);
                st[clone].link = st[q].link;
                st[clone].cnt = 0; // Clone starts with 0
                st[clone].isClone = true;
                
                while (p != -1 && st[p].next.get(c) == q) {
                    st[p].next.put(c, clone);
                    p = st[p].link;
                }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        int q = sc.nextInt();
        String[] queries = new String[q];
        for (int i = 0; i < q; i++) {
            queries[i] = sc.next();
        }

        Solution solution = new Solution();
        long[] ans = solution.countOccurrences(s, queries);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.length; i++) {
            sb.append(ans[i]);
            if (i + 1 < ans.length) sb.append('\n');
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
