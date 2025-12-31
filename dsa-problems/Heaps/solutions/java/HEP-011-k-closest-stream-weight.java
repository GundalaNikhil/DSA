import java.util.*;

class Solution {
    static class Point implements Comparable<Point> {
        long num, den;
        int id;
        
        public Point(long num, long den, int id) {
            this.num = num;
            this.den = den;
            this.id = id;
        }
        
        // Compare for Max-Heap (Reverse of "Better")
        // We want "Worst" at top.
        // Worst = Larger Distance, or Same Distance + Larger ID.
        @Override
        public int compareTo(Point other) {
            // this vs other
            // distA = num/den, distB = other.num/other.den
            // Compare num*other.den vs other.num*den
            long val1 = this.num * other.den;
            long val2 = other.num * this.den;
            
            if (val1 != val2) {
                return Long.compare(val1, val2);
            }
            return Integer.compare(this.id, other.id);
        }
    }
    
    public List<String> processOperations(int k, List<String[]> operations) {
        PriorityQueue<Point> pq = new PriorityQueue<>(Collections.reverseOrder());
        List<String> results = new ArrayList<>();
        int currentId = 1;
        
        for (String[] op : operations) {
            if (op[0].equals("ADD")) {
                long x = Long.parseLong(op[1]);
                long y = Long.parseLong(op[2]);
                long w = Long.parseLong(op[3]);
                
                Point p = new Point(x * x + y * y, w, currentId++);
                
                if (pq.size() < k) {
                    pq.offer(p);
                } else {
                    Point top = pq.peek();
                    // If p is "better" (smaller) than top, replace.
                    // p < top means p.compareTo(top) < 0
                    if (p.compareTo(top) < 0) {
                        pq.poll();
                        pq.offer(p);
                    }
                }
            } else {
                if (pq.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    List<Point> list = new ArrayList<>(pq);
                    Collections.sort(list); // Sorts ascending (Smallest first)
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < list.size(); i++) {
                        sb.append(list.get(i).id);
                        if (i < list.size() - 1) sb.append(" ");
                    }
                    results.add(sb.toString());
                }
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
            int k = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD")) {
                    String x = sc.next();
                    String y = sc.next();
                    String w = sc.next();
                    operations.add(new String[]{op, x, y, w});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(k, operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
