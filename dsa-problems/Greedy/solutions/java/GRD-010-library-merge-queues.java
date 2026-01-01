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
        int[] indices = new int[queues.size()];

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

            if (result.size() > 0 && best.val == lastVal && count == 2) {
                if (pq.isEmpty()) {
                    break; // Deadlock
                }

                List<Node> temp = new ArrayList<>();
                temp.add(best);
                boolean found = false;

                while (!pq.isEmpty()) {
                    Node next = pq.poll();
                    if (next.val != lastVal) {
                        // Found valid
                        result.add(next.val);
                        lastVal = next.val;
                        count = 1;

                        indices[next.queueIndex]++;
                        if (indices[next.queueIndex] < queues.get(next.queueIndex).size()) {
                            pq.offer(new Node(queues.get(next.queueIndex).get(indices[next.queueIndex]), next.queueIndex));
                        }
                        found = true;
                        break;
                    } else {
                        temp.add(next);
                    }
                }

                // Push back temp
                for (Node item : temp) {
                    pq.offer(item);
                }

                if (!found) break; // Deadlock

            } else {
                // Valid
                result.add(best.val);
                if (best.val == lastVal) {
                    count++;
                } else {
                    lastVal = best.val;
                    count = 1;
                }

                indices[best.queueIndex]++;
                if (indices[best.queueIndex] < queues.get(best.queueIndex).size()) {
                    pq.offer(new Node(queues.get(best.queueIndex).get(indices[best.queueIndex]), best.queueIndex));
                }
            }
        }

        return result;
    }
}

class Main {
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
