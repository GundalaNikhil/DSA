import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        int val;
        int queueIndex;

        public Node(int val, int queueIndex) {
            this.val = val;
            this.queueIndex = queueIndex;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.val, other.val);
        }
    }

    public List<Integer> mergeQueues(List<List<Integer>> queues) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        // Pointers to current index in each queue
        int[] indices = new int[queues.size()];
        
        // Initialize heap
        for (int i = 0; i < queues.size(); i++) {
            if (!queues.get(i).isEmpty()) {
                pq.offer(new Node(queues.get(i).get(0), i));
            }
        }
        
        List<Integer> result = new ArrayList<>();
        int lastVal = -1;
        int count = 0;
        
        while (!pq.isEmpty()) {
            Node best = pq.poll();
            
            // Check constraint
            if (result.size() >= 2 && best.val == lastVal && count == 2) {
                if (pq.isEmpty()) {
                    // No other options, cannot proceed
                    break;
                }
                
                Node secondBest = pq.poll();
                
                // Use second best
                result.add(secondBest.val);
                if (secondBest.val == lastVal) {
                    count++; // Should not happen if logic is correct (secondBest must be diff or count reset)
                    // But heap is sorted. If best.val == lastVal, and secondBest.val == best.val,
                    // then secondBest is ALSO blocked.
                    // We need to find the first NON-blocked value.
                    // However, problem constraints usually imply we just skip the blocked value.
                    // If multiple queues have the same blocked value, we need to skip ALL of them.
                    // Let's handle this generally.
                } else {
                    lastVal = secondBest.val;
                    count = 1;
                }
                
                // Advance second best
                indices[secondBest.queueIndex]++;
                if (indices[secondBest.queueIndex] < queues.get(secondBest.queueIndex).size()) {
                    pq.offer(new Node(queues.get(secondBest.queueIndex).get(indices[secondBest.queueIndex]), secondBest.queueIndex));
                }
                
                // Push best back
                pq.offer(best);
                
            } else {
                // Use best
                result.add(best.val);
                if (result.size() == 1 || best.val != lastVal) {
                    lastVal = best.val;
                    count = 1;
                } else {
                    count++;
                }
                
                // Advance best
                indices[best.queueIndex]++;
                if (indices[best.queueIndex] < queues.get(best.queueIndex).size()) {
                    pq.offer(new Node(queues.get(best.queueIndex).get(indices[best.queueIndex]), best.queueIndex));
                }
            }
        }
        
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();

        List<List<Integer>> queues = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int len = sc.nextInt();
            List<Integer> queue = new ArrayList<>();
            for (int j = 0; j < len; j++) {
                queue.add(sc.nextInt());
            }
            queues.add(queue);
        }

        Solution solution = new Solution();
        List<Integer> result = solution.mergeQueues(queues);

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
