import java.util.*;

class Solution {
    private PriorityQueue<Integer> left; // Max heap
    private PriorityQueue<Integer> right; // Min heap
    private Map<Integer, Integer> leftDebt;
    private Map<Integer, Integer> rightDebt;
    private Map<Integer, Integer> globalCounts;
    private int validLeft, validRight;

    public List<String> processOperations(int T, List<String[]> operations) {
        left = new PriorityQueue<>(Collections.reverseOrder());
        right = new PriorityQueue<>();
        leftDebt = new HashMap<>();
        rightDebt = new HashMap<>();
        globalCounts = new HashMap<>();
        validLeft = 0;
        validRight = 0;
        
        List<String> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("ADD")) {
                int x = Integer.parseInt(op[1]);
                globalCounts.put(x, globalCounts.getOrDefault(x, 0) + 1);
                add(x);
            } else if (type.equals("DEL")) {
                int x = Integer.parseInt(op[1]);
                if (globalCounts.getOrDefault(x, 0) > 0) {
                    globalCounts.put(x, globalCounts.get(x) - 1);
                    del(x);
                }
            } else {
                results.add(getMedian(T));
            }
        }
        return results;
    }
    
    private void add(int x) {
        cleanLeft();
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
        cleanLeft();
        cleanRight();
        
        boolean inLeft = false;
        if (!left.isEmpty() && x <= left.peek()) inLeft = true;
        else inLeft = false;
        
        if (inLeft) {
            leftDebt.put(x, leftDebt.getOrDefault(x, 0) + 1);
            validLeft--;
        } else {
            rightDebt.put(x, rightDebt.getOrDefault(x, 0) + 1);
            validRight--;
        }
        
        rebalance();
    }
    
    private String getMedian(int T) {
        cleanLeft();
        
        int total = validLeft + validRight;
        if (total == 0) return "EMPTY";
        if (total < T) return "NA";
        
        // Safety check for empty queue though logic implies it shouldn't be empty if total > 0
        if (left.isEmpty()) return "EMPTY"; 
        return String.valueOf(left.peek());
    }
    
    private void rebalance() {
        // Invariant: validLeft == validRight OR validLeft == validRight + 1
        
        cleanLeft();
        cleanRight();
        
        while (validLeft > validRight + 1) {
            cleanLeft(); // ensure top is valid
            if (left.isEmpty()) break; 
            int val = left.poll();
            validLeft--;
            right.offer(val);
            validRight++;
            cleanLeft();
        }
        
        cleanRight();
        while (validRight > validLeft) {
            cleanRight(); // ensure top is valid
            if (right.isEmpty()) break;
            int val = right.poll();
            validRight--;
            left.offer(val);
            validLeft++;
            cleanRight();
        }
    }
    
    private void cleanLeft() {
        while (!left.isEmpty() && leftDebt.getOrDefault(left.peek(), 0) > 0) {
            int val = left.poll();
            leftDebt.put(val, leftDebt.get(val) - 1);
        }
    }

    private void cleanRight() {
        while (!right.isEmpty() && rightDebt.getOrDefault(right.peek(), 0) > 0) {
            int val = right.poll();
            rightDebt.put(val, rightDebt.get(val) - 1);
        }
    }
}

class Main {
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
