import java.util.*;

class Solution {
    private long[] bit;
    private int n;
    private long mod;

    public List<Long> process(int[] arr, long mod, List<String[]> ops) {
        this.n = arr.length;
        this.mod = mod;
        this.bit = new long[n + 1];
        
        // Build BIT
        for (int i = 0; i < n; i++) {
            add(i + 1, arr[i]);
        }

        // Current state of array to track values for updates
        long[] currentArr = new long[n];
        for(int i=0; i<n; i++) currentArr[i] = arr[i];

        // History stack: stores {index, oldValue}
        Stack<long[]> history = new Stack<>();
        List<Long> results = new ArrayList<>();

        for (String[] op : ops) {
            String type = op[0];
            if (type.equals("UPDATE")) {
                int idx = Integer.parseInt(op[1]); // 0-based from input?
                // Problem statement usually implies 0-based or 1-based. 
                // Example: UPDATE 2 10. Array 1 2 3 4 5.
                // If 0-based, index 2 is 3. 
                // Let's assume 0-based based on "QUERY 0 4".
                long val = Long.parseLong(op[2]);
                
                long oldVal = currentArr[idx];
                history.push(new long[]{idx, oldVal});
                
                long diff = (val - oldVal) % mod;
                if (diff < 0) diff += mod;
                
                add(idx + 1, diff);
                currentArr[idx] = val;

            } else if (type.equals("QUERY")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long res = (query(r + 1) - query(l)) % mod;
                if (res < 0) res += mod;
                results.add(res);

            } else if (type.equals("UNDO")) {
                int k = Integer.parseInt(op[1]);
                while (k > 0 && !history.isEmpty()) {
                    long[] last = history.pop();
                    int idx = (int) last[0];
                    long oldVal = last[1];
                    
                    long currentVal = currentArr[idx];
                    long diff = (oldVal - currentVal) % mod;
                    if (diff < 0) diff += mod;
                    
                    add(idx + 1, diff);
                    currentArr[idx] = oldVal;
                    k--;
                }
            }
        }
        return results;
    }

    private void add(int idx, long val) {
        for (; idx <= n; idx += idx & -idx) {
            bit[idx] = (bit[idx] + val) % mod;
            if (bit[idx] < 0) bit[idx] += mod;
        }
    }

    private long query(int idx) {
        long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum = (sum + bit[idx]) % mod;
        }
        return sum;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long mod = sc.nextLong();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("UNDO")) {
                    ops.add(new String[]{type, sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, mod, ops);
            for (long res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
