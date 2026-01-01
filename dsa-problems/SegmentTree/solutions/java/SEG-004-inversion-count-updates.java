import java.util.*;

class Solution {
    public List<Long> process(int[] arr, List<int[]> updates) {
        int n = arr.length;
        int blockSize = (int) Math.sqrt(n * Math.log(n + 1) / Math.log(2)) + 1;
        if (blockSize < 50) blockSize = 50; // Heuristic lower bound
        
        int numBlocks = (n + blockSize - 1) / blockSize;
        List<List<Integer>> blocks = new ArrayList<>();
        for (int i = 0; i < numBlocks; i++) blocks.add(new ArrayList<>());
        
        for (int i = 0; i < n; i++) {
            blocks.get(i / blockSize).add(arr[i]);
        }
        
        for (List<Integer> b : blocks) Collections.sort(b);
        
        // Initial inversion count using Merge Sort or BIT
        long currentInversions = countInversions(arr);
        List<Long> results = new ArrayList<>();
        
        for (int[] up : updates) {
            int idx = up[0];
            int val = up[1];
            int oldVal = arr[idx];
            
            if (val == oldVal) {
                results.add(currentInversions);
                continue;
            }
            
            int bIdx = idx / blockSize;
            
            // Remove contribution of oldVal
            currentInversions -= countGreaterLeft(blocks, arr, idx, oldVal, blockSize);
            currentInversions -= countSmallerRight(blocks, arr, idx, oldVal, blockSize);
            
            // Update structures
            arr[idx] = val;
            List<Integer> block = blocks.get(bIdx);
            // Remove oldVal using binary search to find index
            int pos = Collections.binarySearch(block, oldVal);
            // binarySearch might return any index if duplicates, but we just need to remove one instance.
            // However, we must ensure we remove the correct instance? Values are identical, so any instance works.
            // But Collections.binarySearch returns arbitrary index.
            if (pos < 0) pos = -pos - 1; // Should be found though
            // If duplicates exist, binarySearch returns one of them.
            // We need to iterate to find one if binarySearch isn't guaranteed (it is for found elements).
            // We can just remove at pos.
            block.remove(pos);
            
            // Insert val
            int insertPos = Collections.binarySearch(block, val);
            if (insertPos < 0) insertPos = -insertPos - 1;
            block.add(insertPos, val);
            
            // Add contribution of val
            currentInversions += countGreaterLeft(blocks, arr, idx, val, blockSize);
            currentInversions += countSmallerRight(blocks, arr, idx, val, blockSize);
            
            results.add(currentInversions);
        }
        return results;
    }
    
    private long countGreaterLeft(List<List<Integer>> blocks, int[] arr, int idx, int val, int blockSize) {
        long count = 0;
        int bIdx = idx / blockSize;
        
        // Full blocks to the left
        for (int i = 0; i < bIdx; i++) {
            List<Integer> b = blocks.get(i);
            // Count elements > val
            int pos = upperBound(b, val);
            count += (b.size() - pos);
        }
        
        // Elements in same block to the left
        int start = bIdx * blockSize;
        for (int i = start; i < idx; i++) {
            if (arr[i] > val) count++;
        }
        return count;
    }
    
    private long countSmallerRight(List<List<Integer>> blocks, int[] arr, int idx, int val, int blockSize) {
        long count = 0;
        int bIdx = idx / blockSize;
        int numBlocks = blocks.size();
        
        // Elements in same block to the right
        int end = Math.min((bIdx + 1) * blockSize, arr.length);
        for (int i = idx + 1; i < end; i++) {
            if (arr[i] < val) count++;
        }
        
        // Full blocks to the right
        for (int i = bIdx + 1; i < numBlocks; i++) {
            List<Integer> b = blocks.get(i);
            // Count elements < val
            int pos = lowerBound(b, val);
            count += pos;
        }
        return count;
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
    
    // Standard Merge Sort Inversion Count
    private long countInversions(int[] arr) {
        return mergeSort(arr.clone(), 0, arr.length - 1);
    }
    
    private long mergeSort(int[] arr, int l, int r) {
        if (l >= r) return 0;
        int mid = (l + r) / 2;
        long count = mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r);
        
        int[] temp = new int[r - l + 1];
        int i = l, j = mid + 1, k = 0;
        while (i <= mid && j <= r) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                count += (mid - i + 1);
            }
        }
        while (i <= mid) temp[k++] = arr[i++];
        while (j <= r) temp[k++] = arr[j++];
        System.arraycopy(temp, 0, arr, l, temp.length);
        return count;
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
            List<int[]> updates = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next(); // SET
                updates.add(new int[]{sc.nextInt(), sc.nextInt()});
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, updates);
            for (long res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
