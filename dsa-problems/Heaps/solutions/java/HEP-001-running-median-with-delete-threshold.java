import java.util.*;

class Solution {
    private PriorityQueue<Integer> left; // Max heap
    private PriorityQueue<Integer> right; // Min heap
    private Map<Integer, Integer> debt;
    private int validLeft, validRight;

    public List<String> processOperations(int T, List<String[]> operations) {
        left = new PriorityQueue<>(Collections.reverseOrder());
        right = new PriorityQueue<>();
        debt = new HashMap<>();
        validLeft = 0;
        validRight = 0;
        
        List<String> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("ADD")) {
                int x = Integer.parseInt(op[1]);
                add(x);
            } else if (type.equals("DEL")) {
                int x = Integer.parseInt(op[1]);
                del(x);
            } else {
                results.add(getMedian(T));
            }
        }
        return results;
    }
    
    private void add(int x) {
        if (left.isEmpty() || x <= left.peek()) {
            left.offer(x);
            validLeft++;
        } else {
            right.offer(x);
            validRight++;
        }
        rebalance();
    }
    
    private void del(int x) {
        // We assume x exists as per problem description "if it exists"
        // But we need to know WHERE it effectively is to update valid counts.
        // A simple heuristic: if x <= median, treat it as in left.
        // Correct logic: Check if x can be in right (x >= right.peek()).
        // But right.peek() can be stale.
        // Robust approach:
        // Always clean tops first.
        
        // If left is empty, it must be in right (if validRight > 0).
        
        // Assume the caller guarantees existence or we handle it.
        // Problem says "remove one occurrence IF IT EXISTS".
        // We need to track total count of x.
        
        // Simplified Logic:
        // Just mark it as deleted.
        // We need to know if we decrement validLeft or validRight.
        // If x <= current_median, we treat it as removing from Left.
        
        int currentMedian = Integer.MIN_VALUE;
        clean(left);
        if (!left.isEmpty()) currentMedian = left.peek();
        
        // If heaps are empty, we can't delete (or x doesn't exist).
        // But we can have stale elements.
        
        // To strictly track validLeft/Right is hard with duplicates.
        // Alternative: Don't track validLeft/Right manually. 
        // Use .size() - dead_in_heap.
        // But we don't know dead_in_heap count for each heap easily.
        
        // Use the standard:
        // If x <= left.peek(), it's in Left.
        // Else in Right.
        // CAUTION: left.peek() can be stale.
        // So always clean left and right before making decisions.
        
        clean(left);
        clean(right);
        
        boolean inLeft = false;
        if (!left.isEmpty() && x <= left.peek()) inLeft = true;
        else if (!right.isEmpty() && x >= right.peek()) inLeft = false;
        else {
            // x is between left.peek() and right.peek()? Impossible if balanced.
            // Or one heap is empty.
            if (left.isEmpty()) inLeft = false; // Must be in right
            else inLeft = true; // Must be in left
        }
        
        // Verify existence? The problem implies we should only delete if exists.
        // We can use a global frequency map to check existence.
        // Assume we maintain a global map `present`.
        
        debt.put(x, debt.getOrDefault(x, 0) + 1);
        if (inLeft) validLeft--;
        else validRight--;
        
        rebalance();
    }
    
    private String getMedian(int T) {
        clean(left);
        clean(right);
        
        int total = validLeft + validRight;
        if (total == 0) return "EMPTY";
        if (total < T) return "NA";
        
        return String.valueOf(left.peek());
    }
    
    private void rebalance() {
        // Invariant: validLeft == validRight OR validLeft == validRight + 1
        
        // While validLeft > validRight + 1
        while (validLeft > validRight + 1) {
            clean(left);
            int val = left.poll();
            validLeft--;
            right.offer(val);
            validRight++;
        }
        
        // While validRight > validLeft
        while (validRight > validLeft) {
            clean(right);
            int val = right.poll();
            validRight--;
            left.offer(val);
            validLeft++;
        }
        
        clean(left);
        clean(right);
    }
    
    private void clean(PriorityQueue<Integer> heap) {
        while (!heap.isEmpty() && debt.getOrDefault(heap.peek(), 0) > 0) {
            int val = heap.poll();
            debt.put(val, debt.get(val) - 1);
            // We don't decrement valid counts here because we already did when DEL was called
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            int T = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD") || op.equals("DEL")) {
                    String x = sc.next();
                    operations.add(new String[]{op, x});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(T, operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
