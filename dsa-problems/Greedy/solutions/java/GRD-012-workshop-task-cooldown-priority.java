import java.util.*;

class Solution {
    static class Task implements Comparable<Task> {
        char name;
        int count;
        int priority;
        int readyTime;

        public Task(char name, int count, int priority) {
            this.name = name;
            this.count = count;
            this.priority = priority;
            this.readyTime = 0;
        }

        @Override
        public int compareTo(Task other) {
            if (this.priority != other.priority) {
                return Integer.compare(other.priority, this.priority); // High priority first
            }
            return Integer.compare(other.count, this.count); // High count first
        }
    }

    public int minSlots(List<Task> inputTasks, int k) {
        PriorityQueue<Task> readyQueue = new PriorityQueue<>();
        List<Task> cooldownList = new ArrayList<>();
        
        for (Task t : inputTasks) {
            readyQueue.offer(t);
        }
        
        int time = 0;
        int tasksRemaining = 0;
        for (Task t : inputTasks) tasksRemaining += t.count;
        
        while (tasksRemaining > 0) {
            time++;
            
            // 1. Move ready tasks from cooldown to readyQueue
            // We need to use an iterator to remove safely
            Iterator<Task> it = cooldownList.iterator();
            while (it.hasNext()) {
                Task t = it.next();
                if (t.readyTime <= time) {
                    readyQueue.offer(t);
                    it.remove();
                }
            }
            
            if (readyQueue.isEmpty()) {
                // IDLE
                continue;
            }
            
            // 2. Pick best task
            Task current = readyQueue.poll();
            current.count--;
            tasksRemaining--;
            
            // 3. Apply Interrupts to Cooldown List
            for (Task t : cooldownList) {
                if (t.priority < current.priority) {
                    t.readyTime = Math.max(t.readyTime, time + k + 1);
                }
            }
            
            // 4. Add current back to cooldown if needed
            if (current.count > 0) {
                current.readyTime = time + k + 1;
                cooldownList.add(current);
            }
        }
        
        return time;
    }
}

class Task {
    char name;
    int count;
    int priority;
    
    Task(char name, int count, int priority) {
        this.name = name;
        this.count = count;
        this.priority = priority;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();

        List<Solution.Task> tasks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char name = sc.next().charAt(0);
            int count = sc.nextInt();
            int priority = sc.nextInt();
            tasks.add(new Solution.Task(name, count, priority));
        }

        Solution solution = new Solution();
        System.out.println(solution.minSlots(tasks, k));
        sc.close();
    }
}
