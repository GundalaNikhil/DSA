import java.util.*;

class Solution {
    static class State {
        double count;
        int last_update;
        int version;
    }

    static class Entry {
        double count;
        String key;
        int version;

        Entry(double count, String key, int version) {
            this.count = count;
            this.key = key;
            this.version = version;
        }
    }

    public List<String> processOperations(int d, int k, List<String[]> operations) {
        Map<String, State> map = new HashMap<>();
        // PriorityQueue: Max heap by count, then lexicographically smallest key
        PriorityQueue<Entry> pq = new PriorityQueue<>((a, b) -> {
            if (Math.abs(a.count - b.count) > 1e-9) {
                return Double.compare(b.count, a.count); // Descending count
            }
            return a.key.compareTo(b.key); // Ascending key
        });
        
        List<String> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("ADD")) {
                String key = op[1];
                int t = Integer.parseInt(op[2]);
                
                double current_count = 0.0;
                State state = map.get(key);
                if (state != null) {
                    if (t >= state.last_update) {
                        int steps = (t - state.last_update) / d;
                        if (steps > 0) {
                            state.count *= Math.pow(0.5, steps);
                        }
                    }
                    current_count = state.count;
                }
                
                double new_count = current_count + 1.0;
                int new_ver = (state != null ? state.version + 1 : 1);
                
                State newState = new State();
                newState.count = new_count;
                newState.last_update = t;
                newState.version = new_ver;
                map.put(key, newState);
                
                pq.add(new Entry(new_count, key, new_ver));
                
            } else {
                int t = Integer.parseInt(op[1]);
                List<String> top_k = new ArrayList<>();
                List<Entry> temp_back = new ArrayList<>();
                
                while (top_k.size() < k && !pq.isEmpty()) {
                    Entry e = pq.poll();
                    State s = map.get(e.key);
                    
                    if (s == null || s.version != e.version) {
                        continue;
                    }
                    
                    int steps = 0;
                    if (t >= s.last_update) {
                        steps = (t - s.last_update) / d;
                    }
                    
                    if (steps > 0) {
                        s.count *= Math.pow(0.5, steps);
                        s.last_update += steps * d;
                        s.version++;
                        
                        pq.add(new Entry(s.count, e.key, s.version));
                    } else {
                        top_k.add(e.key);
                        temp_back.add(e);
                    }
                }
                
                if (top_k.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    results.add(String.join(" ", top_k));
                }
                
                for (Entry e : temp_back) {
                    pq.add(e);
                }
            }
        }
        return results;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            int d = sc.nextInt();
            int k = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD")) {
                    String key = sc.next();
                    String t = sc.next();
                    operations.add(new String[]{op, key, t});
                } else {
                    String t = sc.next();
                    operations.add(new String[]{op, t});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(d, k, operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
