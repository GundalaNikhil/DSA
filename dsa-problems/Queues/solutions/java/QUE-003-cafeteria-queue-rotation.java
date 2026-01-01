import java.util.*;

class Solution {
    public String processQueueOperations(List<String[]> operations) {
        Queue<Integer> q = new LinkedList<>();
        long total = 0;

        for (String[] opData : operations) {
            String cmd = opData[0];

            if (cmd.equals("ENQUEUE")) {
                q.offer(Integer.parseInt(opData[1]));
            } else if (cmd.equals("DEQUEUE")) {
                if (!q.isEmpty()) {
                    q.poll();
                }
            } else if (cmd.equals("FRONT")) {
                // Just read
            } else if (cmd.equals("REAR")) {
                // Just read
            } else if (cmd.equals("SIZE")) {
                total += q.size();
            } else if (cmd.equals("ISEMPTY")) {
                // Just read
            }
        }

        return String.valueOf(total);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            List<String[]> operations = new ArrayList<>();

            for (int i = 0; i < m; i++) {
                String op = sc.next();
                if (op.equals("ENQUEUE")) {
                    String val = sc.next();
                    operations.add(new String[]{op, val});
                } else {
                    operations.add(new String[]{op});
                }
            }

            Solution solution = new Solution();
            String result = solution.processQueueOperations(operations);
            System.out.println(result);
        }
        sc.close();
    }
}
