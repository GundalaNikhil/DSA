import java.util.*;

class Solution {
    static class Node {
        String id;
        long value;
        public Node(String id, long value) {
            this.id = id;
            this.value = value;
        }
    }
    
    // Custom Min Heap
    List<Node> heap = new ArrayList<>();
    Map<String, Integer> pos = new HashMap<>();
    
    private void swap(int i, int j) {
        Node n1 = heap.get(i);
        Node n2 = heap.get(j);
        
        heap.set(i, n2);
        heap.set(j, n1);
        
        pos.put(n1.id, j);
        pos.put(n2.id, i);
    }
    
    private boolean less(int i, int j) {
        Node n1 = heap.get(i);
        Node n2 = heap.get(j);
        if (n1.value != n2.value) {
            return n1.value < n2.value;
        }
        return n1.id.compareTo(n2.id) < 0;
    }
    
    private void bubbleUp(int k) {
        while (k > 0) {
            int p = (k - 1) / 2;
            if (less(k, p)) {
                swap(k, p);
                k = p;
            } else {
                break;
            }
        }
    }
    
    private void bubbleDown(int k) {
        int half = heap.size() / 2;
        while (k < half) {
            int child = 2 * k + 1;
            int right = child + 1;
            if (right < heap.size() && less(right, child)) {
                child = right;
            }
            if (less(child, k)) {
                swap(k, child);
                k = child;
            } else {
                break;
            }
        }
    }
    
    public List<String> processOperations(List<String[]> operations) {
        List<String> results = new ArrayList<>();
        heap.clear();
        pos.clear();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("INSERT")) {
                String id = op[1];
                long val = Long.parseLong(op[2]);
                Node node = new Node(id, val);
                heap.add(node);
                pos.put(id, heap.size() - 1);
                bubbleUp(heap.size() - 1);
            } else if (type.equals("DECREASE")) {
                String id = op[1];
                long delta = Long.parseLong(op[2]);
                if (pos.containsKey(id)) {
                    int idx = pos.get(id);
                    heap.get(idx).value -= delta;
                    bubbleUp(idx);
                }
            } else if (type.equals("EXTRACT")) {
                if (heap.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    Node min = heap.get(0);
                    results.add(min.value + " " + min.id);
                    
                    int lastIdx = heap.size() - 1;
                    Node last = heap.remove(lastIdx);
                    pos.remove(min.id);
                    
                    if (lastIdx > 0) {
                        heap.set(0, last);
                        pos.put(last.id, 0);
                        bubbleDown(0);
                    }
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
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("INSERT")) {
                    String id = sc.next();
                    String value = sc.next();
                    operations.add(new String[]{op, id, value});
                } else if (op.equals("DECREASE")) {
                    String id = sc.next();
                    String delta = sc.next();
                    operations.add(new String[]{op, id, delta});
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
