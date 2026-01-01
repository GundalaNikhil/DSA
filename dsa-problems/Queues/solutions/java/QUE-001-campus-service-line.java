import java.util.*;

class Solution {
    public List<String> processCommands(List<String[]> commands) {
        List<String> result = new ArrayList<>();
        Queue<String> queue = new LinkedList<>();

        for (String[] cmd : commands) {
            String op = cmd[0];
            if (op.equals("ENQUEUE")) {
                queue.offer(cmd[1]);
            } else if (op.equals("DEQUEUE")) {
                if (queue.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    result.add(queue.poll());
                }
            } else if (op.equals("FRONT")) {
                if (queue.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    result.add(queue.peek());
                }
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            List<String[]> commands = new ArrayList<>();
    
            for (int i = 0; i < m; i++) {
                String op = sc.next();
                if (op.equals("ENQUEUE")) {
                    String x = sc.next();
                    commands.add(new String[]{op, x});
                } else {
                    commands.add(new String[]{op});
                }
            }
    
            Solution solution = new Solution();
            List<String> result = solution.processCommands(commands);
            for (String line : result) {
                System.out.println(line);
            }
        }
        sc.close();
    }
}
