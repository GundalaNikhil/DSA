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
            if (left.isEmpty()) return 0;
            return left.peek();
        }
        
        int size() {
            return left.size() + right.size();
        }
    }
    
    // Global heaps with tracking
    PriorityQueue<Integer> gLeft = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> gRight = new PriorityQueue<>();
    Map<Integer, Integer> gDeletedLeft = new HashMap<>();
    Map<Integer, Integer> gDeletedRight = new HashMap<>();
    Map<Integer, Integer> gInLeft = new HashMap<>();
    Map<Integer, Integer> gInRight = new HashMap<>();
    int gLeftSize = 0;
    int gRightSize = 0;
    
    Map<String, Group> groups = new HashMap<>();
    
    private void cleanGlobal() {
        while (!gLeft.isEmpty()) {
            int val = gLeft.peek();
            if (gDeletedLeft.getOrDefault(val, 0) > 0) {
                gDeletedLeft.put(val, gDeletedLeft.get(val) - 1);
                gLeft.poll();
            } else {
                break;
            }
        }
        while (!gRight.isEmpty()) {
            int val = gRight.peek();
            if (gDeletedRight.getOrDefault(val, 0) > 0) {
                gDeletedRight.put(val, gDeletedRight.get(val) - 1);
                gRight.poll();
            } else {
                break;
            }
        }
    }
    
    private void addToGlobal(int val) {
        cleanGlobal();
        if (gLeft.isEmpty() || val <= gLeft.peek()) {
            gLeft.offer(val);
            gInLeft.put(val, gInLeft.getOrDefault(val, 0) + 1);
            gLeftSize++;
        } else {
            gRight.offer(val);
            gInRight.put(val, gInRight.getOrDefault(val, 0) + 1);
            gRightSize++;
        }
        rebalanceGlobal();
    }
    
    private void removeFromGlobal(int val) {
        if (gInLeft.getOrDefault(val, 0) > 0) {
            gInLeft.put(val, gInLeft.get(val) - 1);
            gDeletedLeft.put(val, gDeletedLeft.getOrDefault(val, 0) + 1);
            gLeftSize--;
        } else {
            gInRight.put(val, gInRight.getOrDefault(val, 0) - 1);
            gDeletedRight.put(val, gDeletedRight.getOrDefault(val, 0) + 1);
            gRightSize--;
        }
        rebalanceGlobal();
    }
    
    private void rebalanceGlobal() {
        while (gLeftSize > gRightSize + 1) {
            cleanGlobal();
            if (gLeft.isEmpty()) break; // Should not happen if sizes consistent
            int val = gLeft.poll();
            gInLeft.put(val, gInLeft.getOrDefault(val, 0) - 1);
            
            gRight.offer(val);
            gInRight.put(val, gInRight.getOrDefault(val, 0) + 1);
            gLeftSize--;
            gRightSize++;
            cleanGlobal();
        }
        while (gRightSize > gLeftSize) {
            cleanGlobal();
            if (gRight.isEmpty()) break;
            int val = gRight.poll();
            gInRight.put(val, gInRight.getOrDefault(val, 0) - 1);
            
            gLeft.offer(val);
            gInLeft.put(val, gInLeft.getOrDefault(val, 0) + 1);
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
                if (g.size() > 0) addToGlobal(g.getMedian());
                
            } else if (type.equals("ADD")) {
                String id = op[1];
                int x = Integer.parseInt(op[2]);
                Group g = groups.get(id);
                if (g != null) {
                    if (g.size() > 0) removeFromGlobal(g.getMedian());
                    g.add(x);
                    if (g.size() > 0) addToGlobal(g.getMedian());
                }
                
            } else if (type.equals("MERGE")) {
                String id1 = op[1];
                String id2 = op[2];
                Group g1 = groups.get(id1);
                Group g2 = groups.get(id2);
                
                if (g1 != null && g2 != null) {
                    if (g1.size() > 0) removeFromGlobal(g1.getMedian());
                    if (g2.size() > 0) removeFromGlobal(g2.getMedian());
                    
                    if (g1.size() < g2.size()) {
                        for (int val : g1.left) g2.add(val);
                        for (int val : g1.right) g2.add(val);
                        groups.put(id1, g2);
                    } else {
                        for (int val : g2.left) g1.add(val);
                        for (int val : g2.right) g1.add(val);
                    }
                    groups.remove(id2);
                    Group merged = groups.get(id1);
                    if (merged.size() > 0) addToGlobal(merged.getMedian());
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

class Main {
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
