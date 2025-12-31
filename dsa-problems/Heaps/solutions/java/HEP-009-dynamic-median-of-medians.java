import java.util.*;

class Solution {
    static class Group {
        PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> right = new PriorityQueue<>();
        
        void add(int val) {
            if (left.isEmpty() || val <= left.peek()) {
                left.offer(val);
            } else {
                right.offer(val);
            }
            rebalance();
        }
        
        void rebalance() {
            while (left.size() > right.size() + 1) {
                right.offer(left.poll());
            }
            while (right.size() > left.size()) {
                left.offer(right.poll());
            }
        }
        
        int getMedian() {
            if (left.isEmpty()) return 0; // Should not happen for non-empty
            return left.peek();
        }
        
        int size() {
            return left.size() + right.size();
        }
    }
    
    // Global heaps
    PriorityQueue<Integer> gLeft = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> gRight = new PriorityQueue<>();
    Map<Integer, Integer> gDeleted = new HashMap<>();
    int gLeftSize = 0;
    int gRightSize = 0;
    
    Map<String, Group> groups = new HashMap<>();
    
    private void addToGlobal(int val) {
        cleanGlobal();
        if (gLeft.isEmpty() || val <= gLeft.peek()) {
            gLeft.offer(val);
            gLeftSize++;
        } else {
            gRight.offer(val);
            gRightSize++;
        }
        rebalanceGlobal();
    }
    
    private void removeFromGlobal(int val) {
        gDeleted.put(val, gDeleted.getOrDefault(val, 0) + 1);
        cleanGlobal();
        // We don't know if val was in Left or Right exactly without checking bounds
        // But we can infer: if val <= gLeft.peek(), it was in Left.
        // However, with lazy deletion, peek can be stale. Clean first.
        if (!gLeft.isEmpty() && val <= gLeft.peek()) {
            gLeftSize--;
        } else {
            gRightSize--;
        }
        rebalanceGlobal();
    }
    
    private void cleanGlobal() {
        while (!gLeft.isEmpty() && gDeleted.getOrDefault(gLeft.peek(), 0) > 0) {
            int val = gLeft.poll();
            gDeleted.put(val, gDeleted.get(val) - 1);
        }
        while (!gRight.isEmpty() && gDeleted.getOrDefault(gRight.peek(), 0) > 0) {
            int val = gRight.poll();
            gDeleted.put(val, gDeleted.get(val) - 1);
        }
    }
    
    private void rebalanceGlobal() {
        cleanGlobal();
        while (gLeftSize > gRightSize + 1) {
            gRight.offer(gLeft.poll());
            gLeftSize--;
            gRightSize++;
            cleanGlobal();
        }
        while (gRightSize > gLeftSize) { // Median is in Left (or Left has 1 more)
            gLeft.offer(gRight.poll());
            gLeftSize++;
            gRightSize--;
            cleanGlobal();
        }
    }
    
    public List<String> processOperations(List<String[]> operations) {
        List<String> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("NEW")) {
                String id = op[1];
                Group g = new Group();
                for (int i = 2; i < op.length; i++) {
                    g.add(Integer.parseInt(op[i]));
                }
                groups.put(id, g);
                addToGlobal(g.getMedian());
                
            } else if (type.equals("ADD")) {
                String id = op[1];
                int x = Integer.parseInt(op[2]);
                Group g = groups.get(id);
                if (g != null) {
                    int oldMed = g.getMedian();
                    removeFromGlobal(oldMed);
                    g.add(x);
                    addToGlobal(g.getMedian());
                }
                
            } else if (type.equals("MERGE")) {
                String id1 = op[1];
                String id2 = op[2];
                Group g1 = groups.get(id1);
                Group g2 = groups.get(id2);
                
                if (g1 != null && g2 != null) {
                    removeFromGlobal(g1.getMedian());
                    removeFromGlobal(g2.getMedian());
                    
                    // Small to large merging
                    if (g1.size() < g2.size()) {
                        // Swap contents: move g1 into g2, then make g1 point to g2's content
                        for (int val : g1.left) g2.add(val);
                        for (int val : g1.right) g2.add(val);
                        groups.put(id1, g2);
                    } else {
                        for (int val : g2.left) g1.add(val);
                        for (int val : g2.right) g1.add(val);
                        // g1 already correct
                    }
                    groups.remove(id2); // id2 is gone
                    addToGlobal(groups.get(id1).getMedian());
                }
                
            } else if (type.equals("QUERY")) {
                cleanGlobal();
                if (gLeftSize == 0) results.add("EMPTY");
                else results.add(String.valueOf(gLeft.peek()));
            }
        }
        return results;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("NEW")) {
                    String id = sc.next();
                    int m = sc.nextInt();
                    String[] line = new String[2 + m];
                    line[0] = op;
                    line[1] = id;
                    for (int j = 0; j < m; j++) line[2 + j] = sc.next();
                    operations.add(line);
                } else if (op.equals("ADD")) {
                    String id = sc.next();
                    String x = sc.next();
                    operations.add(new String[]{op, id, x});
                } else if (op.equals("MERGE")) {
                    String id1 = sc.next();
                    String id2 = sc.next();
                    operations.add(new String[]{op, id1, id2});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
