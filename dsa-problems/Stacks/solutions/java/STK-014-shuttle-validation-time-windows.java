import java.util.*;
import java.io.*;

class Solution {
    public boolean validate(List<Integer> push, List<Integer> pushT, 
                            List<Integer> pop, List<Integer> popT,
                            Map<Integer, Integer> windows, Set<Integer> priority) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> timeStack = new Stack<>();
        Stack<Integer> minPriorityStack = new Stack<>();
        
        int j = 0;
        int n = push.size();
        
        for (int i = 0; i < n; i++) {
            int val = push.get(i);
            int t = pushT.get(i);
            
            stack.push(val);
            timeStack.push(t);
            
            int currentMin = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
            if (priority.contains(val)) {
                currentMin = Math.min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!stack.isEmpty() && j < n && stack.peek().equals(pop.get(j))) {
                int poppedVal = stack.pop();
                int pushedTime = timeStack.pop();
                minPriorityStack.pop();
                
                int poppedTime = popT.get(j);
                
                // Check Time Window
                if (windows.containsKey(poppedVal)) {
                    if (poppedTime - pushedTime > windows.get(poppedVal)) {
                        return false;
                    }
                }
                
                // Check Priority
                if (!priority.contains(poppedVal)) {
                    int minP = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return stack.isEmpty();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        // Helper to read tokens robustly
        // State machine parsing based on counts
        
        String line = br.readLine();
        while (line != null && line.trim().isEmpty()) line = br.readLine();
        if (line == null) return;
        
        int numPush = Integer.parseInt(line.trim());
        List<Integer> push = new ArrayList<>();
        List<Integer> pushT = new ArrayList<>();
        
        for (int i = 0; i < numPush; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            push.add(Integer.parseInt(parts[0]));
            pushT.add(Integer.parseInt(parts[1]));
        }
        
        int numPop = Integer.parseInt(br.readLine().trim());
        List<Integer> pop = new ArrayList<>();
        List<Integer> popT = new ArrayList<>();
        
        for (int i = 0; i < numPop; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            pop.add(Integer.parseInt(parts[0]));
            popT.add(Integer.parseInt(parts[1]));
        }
        
        int numWindows = Integer.parseInt(br.readLine().trim());
        Map<Integer, Integer> windows = new HashMap<>();
        
        for (int i = 0; i < numWindows; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            windows.put(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
        }
        
        int numPriority = Integer.parseInt(br.readLine().trim());
        Set<Integer> priority = new HashSet<>();
        
        for (int i = 0; i < numPriority; i++) {
            String l = br.readLine();
            if (l != null && !l.trim().isEmpty()) {
                priority.add(Integer.parseInt(l.trim()));
            }
        }
        
        Solution sol = new Solution();
        boolean res = sol.validate(push, pushT, pop, popT, windows, priority);
        System.out.println(res ? "YES" : "NO");
    }
}
