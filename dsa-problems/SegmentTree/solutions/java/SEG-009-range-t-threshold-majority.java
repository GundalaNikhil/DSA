import java.util.*;

class Solution {
    private List<Integer>[] positions;
    private int[] arr;
    
    // Misra-Gries summary size
    private static final int K = 40; 
    
    static class Summary {
        // value -> count
        // We use a simple list of pairs for small K
        List<int[]> candidates = new ArrayList<>();
        
        void add(int val, int count) {
            for (int[] c : candidates) {
                if (c[0] == val) {
                    c[1] += count;
                    return;
                }
            }
            candidates.add(new int[]{val, count});
            if (candidates.size() > K) {
                // Prune
                // Find min count
                int minCnt = Integer.MAX_VALUE;
                for (int[] c : candidates) minCnt = Math.min(minCnt, c[1]);
                
                List<int[]> next = new ArrayList<>();
                for (int[] c : candidates) {
                    c[1] -= minCnt;
                    if (c[1] > 0) next.add(c);
                }
                candidates = next;
            }
        }
        
        void merge(Summary other) {
            for (int[] c : other.candidates) {
                add(c[0], c[1]);
            }
        }
    }
    
    private Random random = new Random();
    private Summary[] tree;
    private int n;

    public int[] process(int[] arr, int[][] queries) {
        this.arr = arr;
        this.n = arr.length;
        
        // Coordinate Compression / Positions Map
        Map<Integer, Integer> valToId = new HashMap<>();
        List<Integer> idToVal = new ArrayList<>();
        int idCounter = 0;
        
        for (int x : arr) {
            if (!valToId.containsKey(x)) {
                valToId.put(x, idCounter++);
                idToVal.add(x);
            }
        }
        
        positions = new List[idCounter];
        for (int i = 0; i < idCounter; i++) positions[i] = new ArrayList<>();
        
        int[] mappedArr = new int[n];
        for (int i = 0; i < n; i++) {
            mappedArr[i] = valToId.get(arr[i]);
            positions[mappedArr[i]].add(i);
        }
        
        // Build Segment Tree
        tree = new Summary[4 * n];
        build(mappedArr, 0, 0, n - 1);
        
        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int t = queries[i][2];
            
            Summary s = query(0, 0, n - 1, l, r);
            Set<Integer> candidates = new HashSet<>();
            for (int[] c : s.candidates) candidates.add(c[0]);
            
            // Random sampling
            for (int k = 0; k < 40; k++) {
                int randIdx = l + random.nextInt(r - l + 1);
                candidates.add(mappedArr[randIdx]);
            }
            
            int bestVal = -1;
            int maxFreq = -1;
            
            for (int valId : candidates) {
                int freq = getFreq(valId, l, r);
                if (freq >= t) {
                    int realVal = idToVal.get(valId);
                    if (freq > maxFreq) {
                        maxFreq = freq;
                        bestVal = realVal;
                    } else if (freq == maxFreq) {
                        if (bestVal == -1 || realVal < bestVal) {
                            bestVal = realVal;
                        }
                    }
                }
            }
            results[i] = bestVal;
        }
        return results;
    }
    
    private int getFreq(int valId, int l, int r) {
        List<Integer> pos = positions[valId];
        int leftIdx = Collections.binarySearch(pos, l);
        if (leftIdx < 0) leftIdx = -leftIdx - 1;
        int rightIdx = Collections.binarySearch(pos, r);
        if (rightIdx < 0) rightIdx = -rightIdx - 2;
        
        if (leftIdx > rightIdx) return 0;
        return rightIdx - leftIdx + 1;
    }

    private void build(int[] a, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Summary();
            tree[node].add(a[start], 1);
        } else {
            int mid = (start + end) / 2;
            build(a, 2 * node + 1, start, mid);
            build(a, 2 * node + 2, mid + 1, end);
            tree[node] = new Summary();
            tree[node].merge(tree[2 * node + 1]);
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    private Summary query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Summary();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Summary s1 = query(2 * node + 1, start, mid, l, r);
        Summary s2 = query(2 * node + 2, mid + 1, end, l, r);
        
        Summary res = new Summary();
        res.merge(s1);
        res.merge(s2);
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[][] queries = new int[q][3];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // MAJ
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
                queries[i][2] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, queries);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
