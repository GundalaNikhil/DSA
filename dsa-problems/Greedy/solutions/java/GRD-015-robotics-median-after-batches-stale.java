import java.util.*;

class Solution {
    public List<String> medianAfterBatches(int k, int t, List<List<Integer>> batches) {
        PriorityQueue<Integer> lower = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> upper = new PriorityQueue<>();
        Map<Integer, Integer> freq = new HashMap<>();
        Map<Integer, int[]> location = new HashMap<>();
        
        int validLower = 0;
        int validUpper = 0;
        List<String> results = new ArrayList<>();
        
        for (List<Integer> batch : batches) {
            for (int x : batch) {
                freq.put(x, freq.getOrDefault(x, 0) + 1);
                int f = freq.get(x);
                
                if (f > t + 1) continue;
                
                if (f == t + 1) {
                    int[] loc = location.get(x);
                    if (loc != null) {
                        validLower -= loc[0];
                        validUpper -= loc[1];
                    }
                    continue;
                }
                
                // Add new valid number
                // We need to peek valid top to decide
                // But peeking might show stale.
                // It's safe to compare against raw top, then rebalance later.
                if (lower.isEmpty() || x <= lower.peek()) {
                    lower.offer(x);
                    location.computeIfAbsent(x, z -> new int[2])[0]++;
                    validLower++;
                } else {
                    upper.offer(x);
                    location.computeIfAbsent(x, z -> new int[2])[1]++;
                    validUpper++;
                }
            }
            
            // Balance
            // Goal: validLower == validUpper OR validLower == validUpper + 1
            
            while (true) {
                // Prune stale tops
                while (!lower.isEmpty() && freq.get(lower.peek()) > t) lower.poll();
                while (!upper.isEmpty() && freq.get(upper.peek()) > t) upper.poll();
                
                if (validLower > validUpper + 1) {
                    int move = lower.poll();
                    location.get(move)[0]--;
                    location.get(move)[1]++;
                    upper.offer(move);
                    validLower--;
                    validUpper++;
                } else if (validUpper > validLower) {
                    int move = upper.poll();
                    location.get(move)[1]--;
                    location.get(move)[0]++;
                    lower.offer(move);
                    validUpper--;
                    validLower++;
                } else {
                    break;
                }
            }
            
            // Compute Median
            if (validLower + validUpper == 0) {
                results.add("NA");
            } else {
                long med;
                if ((validLower + validUpper) % 2 == 1) {
                    med = lower.peek();
                } else {
                    long v1 = lower.peek();
                    long v2 = upper.peek();
                    med = (long)Math.floor((v1 + v2) / 2.0);
                }
                results.add(String.valueOf(med));
            }
        }
        return results;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        int t = sc.nextInt();

        List<List<Integer>> batches = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int m = sc.nextInt();
            List<Integer> batch = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                batch.add(sc.nextInt());
            }
            batches.add(batch);
        }

        Solution solution = new Solution();
        List<String> result = solution.medianAfterBatches(k, t, batches);

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
