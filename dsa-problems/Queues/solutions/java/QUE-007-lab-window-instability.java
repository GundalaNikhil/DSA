import java.util.*;

class Solution {
    public long[] windowInstability(int[] values, int k) {
        int n = values.length;
        long[] result = new long[n - k + 1];
        
        return solveWithDualPQ(values, k);
    }

    private long[] solveWithDualPQ(int[] values, int k) {
        int n = values.length;
        long[] result = new long[n - k + 1];
        Deque<Integer> minD = new ArrayDeque<>();
        Deque<Integer> maxD = new ArrayDeque<>();
        MedianFinder mf = new MedianFinder();

        for (int i = 0; i < n; i++) {
            // Min/Max
            while (!minD.isEmpty() && minD.peekFirst() <= i - k) minD.pollFirst();
            while (!minD.isEmpty() && values[minD.peekLast()] >= values[i]) minD.pollLast();
            minD.offerLast(i);

            while (!maxD.isEmpty() && maxD.peekFirst() <= i - k) maxD.pollFirst();
            while (!maxD.isEmpty() && values[maxD.peekLast()] <= values[i]) maxD.pollLast();
            maxD.offerLast(i);

            // Median
            mf.add(values[i]);
            if (i >= k) mf.remove(values[i - k]);

            if (i >= k - 1) {
                int minVal = values[minD.peekFirst()];
                int maxVal = values[maxD.peekFirst()];
                int median = mf.getMedian();
                if (median == 0) result[i - k + 1] = 0;
                else {
                    long diff = (long)maxVal - minVal;
                    long instability = diff / median;
                    if (diff % median != 0 && ((diff ^ median) < 0)) {
                        instability--;
                    }
                    result[i - k + 1] = instability;
                }
            }
        }
        return result;
    }

    static class MedianFinder {
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> large = new PriorityQueue<>();
        // To handle lazy removal correctly, we track balance explicitly
        // Balance = small.size() - large.size() (considering only valid elements)
        // But since we can't know if a specific instance in heap is valid, we just track counts.
        // Let's use two TreeMaps (Multiset).
        
        // Re-implementation with TreeMap for correctness and simplicity
        TreeMap<Integer, Integer> smallMap = new TreeMap<>();
        TreeMap<Integer, Integer> largeMap = new TreeMap<>();
        int smallSize = 0;
        int largeSize = 0;

        void add(int val) {
            // Add to small first
            addMap(smallMap, val);
            smallSize++;
            
            // Move max of small to large
            int maxSmall = smallMap.lastKey();
            removeMap(smallMap, maxSmall);
            smallSize--;
            
            addMap(largeMap, maxSmall);
            largeSize++;
            
            // Rebalance: small should be >= large
            if (smallSize < largeSize) {
                int minLarge = largeMap.firstKey();
                removeMap(largeMap, minLarge);
                largeSize--;
                
                addMap(smallMap, minLarge);
                smallSize++;
            }
        }

        void remove(int val) {
            // Try to remove from small first
            if (smallMap.containsKey(val)) {
                // Check if it really belongs to small range
                // It must be <= small.lastKey()
                // Since small contains smaller elements, if val <= small.lastKey(), it's in small.
                // If val is in smallMap, we can just remove it?
                // Yes, because all elements in smallMap are <= all elements in largeMap.
                // So if val is in smallMap, it MUST be in the small partition.
                removeMap(smallMap, val);
                smallSize--;
            } else {
                removeMap(largeMap, val);
                largeSize--;
            }
            
            // Rebalance
            if (smallSize < largeSize) {
                int minLarge = largeMap.firstKey();
                removeMap(largeMap, minLarge);
                largeSize--;
                addMap(smallMap, minLarge);
                smallSize++;
            } else if (smallSize > largeSize + 1) {
                int maxSmall = smallMap.lastKey();
                removeMap(smallMap, maxSmall);
                smallSize--;
                addMap(largeMap, maxSmall);
                largeSize++;
            }
        }

        int getMedian() {
            return smallMap.lastKey();
        }

        void addMap(TreeMap<Integer, Integer> map, int val) {
            map.put(val, map.getOrDefault(val, 0) + 1);
        }

        void removeMap(TreeMap<Integer, Integer> map, int val) {
            int count = map.get(val);
            if (count == 1) map.remove(val);
            else map.put(val, count - 1);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
            Solution solution = new Solution();
            long[] result = solution.windowInstability(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
