import java.util.*;

class Solution {
    private int n;
    private int maxVal;
    // We use a Map for the inner BITs to save space, or coordinate compress.
    // Coordinate compression is better.
    
    public List<Integer> process(int[] arr, List<String[]> ops) {
        n = arr.length;
        
        // Coordinate Compression
        Set<Integer> values = new HashSet<>();
        for (int x : arr) values.add(x);
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                values.add(Integer.parseInt(op[2]));
            } else {
                values.add(Integer.parseInt(op[3])); // x
                values.add(Integer.parseInt(op[4])); // y
            }
        }
        List<Integer> sortedVals = new ArrayList<>(values);
        Collections.sort(sortedVals);
        Map<Integer, Integer> valMap = new HashMap<>();
        for (int i = 0; i < sortedVals.size(); i++) {
            valMap.put(sortedVals.get(i), i + 1); // 1-based for BIT
        }
        maxVal = sortedVals.size();
        
        // Initialize BIT of BITs
        // Outer BIT size N, Inner BIT size maxVal
        // To save space, we can use dynamic allocation or just arrays if N*maxVal fits?
        // N=200k, maxVal=400k. 200k * 400k is too big.
        // We need dynamic nodes or Map<Integer, Integer> for inner BITs.
        // Or simpler: Use Square Root Decomposition for implementation simplicity and memory safety.
        // Given constraints and typical interview setting, SQRT is often accepted.
        // However, let's try to implement a memory-efficient BIT of BITs using HashMap for inner nodes.
        
        // For dynamic, "BIT of dynamic Segment Trees" is standard.
        // Let's use SQRT Decomposition for code clarity and safety against OOM.
        
        return sqrtDecomposition(arr, ops);
    }
    
    private List<Integer> sqrtDecomposition(int[] arr, List<String[]> ops) {
        int blockSize = (int) Math.sqrt(n * Math.log(n + 1) / Math.log(2)) + 1;
        List<List<Integer>> blocks = new ArrayList<>();
        int numBlocks = (n + blockSize - 1) / blockSize;
        
        for (int i = 0; i < numBlocks; i++) blocks.add(new ArrayList<>());
        for (int i = 0; i < n; i++) blocks.get(i / blockSize).add(arr[i]);
        for (List<Integer> b : blocks) Collections.sort(b);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                int val = Integer.parseInt(op[2]);
                int oldVal = arr[idx];
                arr[idx] = val;
                
                List<Integer> block = blocks.get(idx / blockSize);
                // Remove oldVal
                int pos = Collections.binarySearch(block, oldVal);
                if (pos < 0) pos = -pos - 1; // Should exist
                // Handle duplicates: binarySearch finds arbitrary. We just remove one.
                // But we must ensure we remove *a* instance.
                // If binarySearch returns index, it is present.
                block.remove(pos);
                
                // Add val
                int ins = Collections.binarySearch(block, val);
                if (ins < 0) ins = -ins - 1;
                block.add(ins, val);
                
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                int x = Integer.parseInt(op[3]);
                int y = Integer.parseInt(op[4]);
                
                int count = 0;
                int startBlock = l / blockSize;
                int endBlock = r / blockSize;
                
                if (startBlock == endBlock) {
                    for (int i = l; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                } else {
                    for (int i = l; i < (startBlock + 1) * blockSize; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                    for (int i = startBlock + 1; i < endBlock; i++) {
                        List<Integer> b = blocks.get(i);
                        // Count elements in [x, y]
                        // upper_bound(y) - lower_bound(x)
                        int upper = upperBound(b, y);
                        int lower = lowerBound(b, x);
                        count += (upper - lower);
                    }
                    for (int i = endBlock * blockSize; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                }
                results.add(count);
            }
        }
        return results;
    }
    
    private int lowerBound(List<Integer> list, int val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) >= val) r = mid;
            else l = mid + 1;
        }
        return l;
    }
    
    private int upperBound(List<Integer> list, int val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) > val) r = mid;
            else l = mid + 1;
        }
        return l;
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
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("SET")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Integer> results = sol.process(arr, ops);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
