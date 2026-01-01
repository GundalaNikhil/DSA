import java.util.*;

class Solution {
    static class DualHeap {
        int k;
        PriorityQueue<Integer> small; // Max heap (simulated)
        PriorityQueue<Integer> large; // Min heap
        int smallCount; // Logical count
        int largeCount; // Logical count
        Map<Integer, Integer> lazy;
        Map<Integer, Integer> inSmall;
        Map<Integer, Integer> inLarge;

        public DualHeap(int k) {
            this.k = k;
            this.small = new PriorityQueue<>(Collections.reverseOrder());
            this.large = new PriorityQueue<>();
            this.smallCount = 0;
            this.largeCount = 0;
            this.lazy = new HashMap<>();
            this.inSmall = new HashMap<>();
            this.inLarge = new HashMap<>();
        }

        private void prune(PriorityQueue<Integer> heap) {
            while (!heap.isEmpty()) {
                int val = heap.peek();
                if (lazy.getOrDefault(val, 0) > 0) {
                    lazy.put(val, lazy.get(val) - 1);
                    heap.poll();
                } else {
                    break;
                }
            }
        }

        public void add(int x) {
            if (smallCount < k) {
                small.offer(x);
                smallCount++;
                inSmall.put(x, inSmall.getOrDefault(x, 0) + 1);
            } else {
                prune(small);
                if (small.isEmpty()) { // Should be rare given smallCount >= k check
                     small.offer(x);
                     smallCount++;
                     inSmall.put(x, inSmall.getOrDefault(x, 0) + 1);
                } else {
                    int smallMax = small.peek();
                    if (x <= smallMax) {
                        small.poll();
                        inSmall.put(smallMax, inSmall.get(smallMax) - 1);
                        
                        small.offer(x);
                        inSmall.put(x, inSmall.getOrDefault(x, 0) + 1);
                        
                        large.offer(smallMax);
                        inLarge.put(smallMax, inLarge.getOrDefault(smallMax, 0) + 1);
                        largeCount++;
                    } else {
                        large.offer(x);
                        inLarge.put(x, inLarge.getOrDefault(x, 0) + 1);
                        largeCount++;
                    }
                }
            }
            balance();
        }

        public void remove(int x) {
            lazy.put(x, lazy.getOrDefault(x, 0) + 1);
            if (inSmall.getOrDefault(x, 0) > 0) {
                inSmall.put(x, inSmall.get(x) - 1);
                smallCount--;
            } else {
                inLarge.put(x, inLarge.getOrDefault(x, 0) - 1); // Note: might be 0 if bug, but logic should hold
                largeCount--;
            }
            balance();
        }

        private void balance() {
            prune(small);
            prune(large);

            while (smallCount < k && !large.isEmpty()) {
                prune(large);
                if (large.isEmpty()) break;
                
                int val = large.poll();
                inLarge.put(val, inLarge.get(val) - 1);
                
                small.offer(val);
                inSmall.put(val, inSmall.getOrDefault(val, 0) + 1);
                smallCount++;
                largeCount--;
                prune(small); 
            }
            
            while (smallCount > k) {
                prune(small);
                 if (small.isEmpty()) break;
                 
                int val = small.poll();
                inSmall.put(val, inSmall.get(val) - 1);
                
                large.offer(val);
                inLarge.put(val, inLarge.getOrDefault(val, 0) + 1);
                smallCount--;
                largeCount++;
                prune(large);
            }
        }

        public Integer getKthSmallest() {
            prune(small);
            if (small.isEmpty()) return null;
            return small.peek();
        }
    }

    public List<Integer> kthSmallestInWindows(int[] arr, int w, int k) {
        int n = arr.length;
        if (w > n) return Collections.emptyList();

        DualHeap dh = new DualHeap(k);
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < w; i++) {
            dh.add(arr[i]);
        }
        result.add(dh.getKthSmallest());

        for (int i = w; i < n; i++) {
            dh.remove(arr[i - w]);
            dh.add(arr[i]);
            result.add(dh.getKthSmallest());
        }

        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            List<Integer> result = solution.kthSmallestInWindows(arr, w, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.size(); i++) {
                if (i > 0) sb.append(" ");
                sb.append(result.get(i));
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
