import java.util.*;

class Solution {
    public List<String> processOperations(int k, List<String[]> operations) {
        List<String> result = new ArrayList<>();
        int[] buffer = new int[k];
        int head = 0;
        int tail = 0;
        int count = 0;

        for (String[] op : operations) {
            String cmd = op[0];
            if (cmd.equals("ENQ")) {
                if (count == k) {
                    result.add("false");
                } else {
                    buffer[tail] = Integer.parseInt(op[1]);
                    tail = (tail + 1) % k;
                    count++;
                    result.add("true");
                }
            } else if (cmd.equals("ENQ_OVR")) {
                int val = Integer.parseInt(op[1]);
                if (count == k) {
                    head = (head + 1) % k; // Drop oldest
                    buffer[tail] = val;
                    tail = (tail + 1) % k;
                    result.add("overwritten");
                } else {
                    buffer[tail] = val;
                    tail = (tail + 1) % k;
                    count++;
                    result.add("true"); // Or just success, problem says "true" for normal ENQ, let's assume consistent
                }
            } else if (cmd.equals("DEQ")) {
                if (count == 0) {
                    result.add("EMPTY");
                } else {
                    result.add(String.valueOf(buffer[head]));
                    head = (head + 1) % k;
                    count--;
                }
            } else if (cmd.equals("FRONT")) {
                if (count == 0) result.add("EMPTY");
                else result.add(String.valueOf(buffer[head]));
            } else if (cmd.equals("REAR")) {
                if (count == 0) result.add("EMPTY");
                else {
                    int idx = (tail - 1 + k) % k;
                    result.add(String.valueOf(buffer[idx]));
                }
            } else if (cmd.equals("ISEMPTY")) {
                result.add(count == 0 ? "true" : "false");
            } else if (cmd.equals("ISFULL")) {
                result.add(count == k ? "true" : "false");
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            int m = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
    
            for (int i = 0; i < m; i++) {
                String op = sc.next();
                if (op.equals("ENQ") || op.equals("ENQ_OVR")) {
                    String x = sc.next();
                    operations.add(new String[]{op, x});
                } else {
                    operations.add(new String[]{op});
                }
            }
    
            Solution solution = new Solution();
            List<String> result = solution.processOperations(k, operations);
            for (String line : result) {
                System.out.println(line);
            }
        }
        sc.close();
    }
}
