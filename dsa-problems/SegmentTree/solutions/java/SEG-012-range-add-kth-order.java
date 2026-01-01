import java.util.*;

class Solution {
    static class Block {
        long[] sorted;
        long lazy;
        
        Block(int size) {
            sorted = new long[size];
            lazy = 0;
        }
    }
    
    private long[] arr;
    private Block[] blocks;
    private int blockSize;
    private int n;

    public List<Long> process(long[] inputArr, List<String[]> ops) {
        n = inputArr.length;
        arr = inputArr.clone();
        blockSize = (int) Math.sqrt(n * Math.log(n + 1) / Math.log(2)) + 1;
        if (blockSize < 100) blockSize = 100; // Heuristic
        
        int numBlocks = (n + blockSize - 1) / blockSize;
        blocks = new Block[numBlocks];
        
        for (int i = 0; i < numBlocks; i++) {
            int start = i * blockSize;
            int end = Math.min(n, start + blockSize);
            blocks[i] = new Block(end - start);
            for (int j = start; j < end; j++) {
                blocks[i].sorted[j - start] = arr[j];
            }
            Arrays.sort(blocks[i].sorted);
        }
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("ADD")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long x = Long.parseLong(op[3]);
                update(l, r, x);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                int k = Integer.parseInt(op[3]);
                results.add(query(l, r, k));
            }
        }
        return results;
    }
    
    private void update(int l, int r, long x) {
        int startBlock = l / blockSize;
        int endBlock = r / blockSize;
        
        if (startBlock == endBlock) {
            partialUpdate(startBlock, l, r, x);
        } else {
            partialUpdate(startBlock, l, (startBlock + 1) * blockSize - 1, x);
            for (int i = startBlock + 1; i < endBlock; i++) {
                blocks[i].lazy += x;
            }
            partialUpdate(endBlock, endBlock * blockSize, r, x);
        }
    }
    
    private void partialUpdate(int bIdx, int l, int r, long x) {
        Block b = blocks[bIdx];
        int start = bIdx * blockSize;
        int end = Math.min(n, start + blockSize);
        
        // Push lazy to arr for this block
        if (b.lazy != 0) {
            for (int i = start; i < end; i++) arr[i] += b.lazy;
            b.lazy = 0;
        }
        
        // Update arr
        for (int i = l; i <= r; i++) arr[i] += x;
        
        // Rebuild sorted
        for (int i = start; i < end; i++) {
            b.sorted[i - start] = arr[i];
        }
        Arrays.sort(b.sorted);
    }
    
    private long query(int l, int r, int k) {
        // Binary search for answer
        // Range estimation: min to max possible
        // Just use a safe range
        long low = -200000000000000L; // -2e14
        long high = 200000000000000L; // 2e14
        long ans = high;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (countLessEqual(l, r, mid) >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
    
    private int countLessEqual(int l, int r, long val) {
        int count = 0;
        int startBlock = l / blockSize;
        int endBlock = r / blockSize;
        
        if (startBlock == endBlock) {
            long lazy = blocks[startBlock].lazy;
            for (int i = l; i <= r; i++) {
                if (arr[i] + lazy <= val) count++;
            }
        } else {
            long lazyStart = blocks[startBlock].lazy;
            for (int i = l; i < (startBlock + 1) * blockSize; i++) {
                if (arr[i] + lazyStart <= val) count++;
            }
            
            for (int i = startBlock + 1; i < endBlock; i++) {
                Block b = blocks[i];
                // Count elements <= val - b.lazy in sorted
                long target = val - b.lazy;
                count += upperBound(b.sorted, target);
            }
            
            long lazyEnd = blocks[endBlock].lazy;
            for (int i = endBlock * blockSize; i <= r; i++) {
                if (arr[i] + lazyEnd <= val) count++;
            }
        }
        return count;
    }
    
    private int upperBound(long[] arr, long val) {
        int l = 0, r = arr.length;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] > val) r = mid;
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
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("ADD")) {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
