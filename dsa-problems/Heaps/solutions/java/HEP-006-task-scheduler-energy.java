import java.util.*;

class Solution {
    static class Task {
        int d, g;
        public Task(int d, int g) {
            this.d = d;
            this.g = g;
        }
    }
    
    public int maxTasks(int E, int[] duration, int[] gain) {
        List<Task> positive = new ArrayList<>();
        List<Task> negative = new ArrayList<>();
        
        for (int i = 0; i < duration.length; i++) {
            if (gain[i] >= duration[i]) {
                positive.add(new Task(duration[i], gain[i]));
            } else {
                negative.add(new Task(duration[i], gain[i]));
            }
        }
        
        // 1. Process Positive: Sort by duration ascending
        Collections.sort(positive, (a, b) -> Integer.compare(a.d, b.d));
        
        int count = 0;
        long currentE = E;
        
        for (Task t : positive) {
            if (currentE >= t.d) {
                currentE += (t.g - t.d);
                count++;
            } else {
                // Cannot process this task. Since sorted by duration, can't process any further?
                break;
            }
        }
        
        long peakE = currentE;

        // 2. Process Negative: Sort by gain descending
        Collections.sort(negative, (a, b) -> Integer.compare(b.g, a.g));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        long currentLossSum = 0;
        
        for (Task t : negative) {
            int loss = t.d - t.g;
            currentLossSum += loss;
            pq.offer(loss);
            if (currentLossSum + t.g > peakE) {
                currentLossSum -= pq.poll();
            }
        }
        
        return count + pq.size();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int E = sc.nextInt();
            int[] duration = new int[n];
            int[] gain = new int[n];
            for (int i = 0; i < n; i++) {
                duration[i] = sc.nextInt();
                gain[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maxTasks(E, duration, gain));
        }
        sc.close();
    }
}
