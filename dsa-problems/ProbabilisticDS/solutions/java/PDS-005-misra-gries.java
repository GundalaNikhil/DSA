import java.util.*;

class Solution {
    public List<Integer> misraGries(int[] stream, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        
        for (int x : stream) {
            if (counts.containsKey(x)) {
                counts.put(x, counts.get(x) + 1);
            } else if (counts.size() < k - 1) {
                counts.put(x, 1);
            } else {
                // Decrement all
                List<Integer> toRemove = new ArrayList<>();
                for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
                    int val = entry.getValue() - 1;
                    if (val == 0) {
                        toRemove.add(entry.getKey());
                    } else {
                        entry.setValue(val);
                    }
                }
                for (int key : toRemove) {
                    counts.remove(key);
                }
            }
        }
        
        List<Integer> res = new ArrayList<>(counts.keySet());
        Collections.sort(res);
        return res;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] stream = new int[n];
            for (int i = 0; i < n; i++) {
                stream[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            List<Integer> res = solution.misraGries(stream, k);
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i));
                if (i + 1 < res.size()) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
