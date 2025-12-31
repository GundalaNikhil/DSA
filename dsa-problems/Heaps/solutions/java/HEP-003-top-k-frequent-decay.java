import java.util.*;

class Solution {
    static class State {
        double count;
        int bucket;
        double score;
        int version;
    }

    static class Entry {
        String key;
        double score;
        int version;

        Entry(String key, double score, int version) {
            this.key = key;
            this.score = score;
            this.version = version;
        }
    }

    public List<String> processOperations(int d, int k, List<String[]> operations) {
        Map<String, State> map = new HashMap<>();
        PriorityQueue<Entry> pq = new PriorityQueue<>((a, b) -> {
            if (a.score == b.score) return a.key.compareTo(b.key);
            return Double.compare(b.score, a.score);
        });
        List<String> results = new ArrayList<>();
        final double LN2 = Math.log(2.0);
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("ADD")) {
                String key = op[1];
                int t = Integer.parseInt(op[2]);

                int bucket = t / d;
                State state = map.get(key);
                if (state == null) {
                    state = new State();
                    state.count = 0.0;
                    state.bucket = bucket;
                    state.version = 0;
                } else if (bucket > state.bucket) {
                    int diff = bucket - state.bucket;
                    state.count *= Math.pow(0.5, diff);
                }

                state.count += 1.0;
                state.bucket = bucket;
                state.score = Math.log(state.count) + state.bucket * LN2;
                state.version++;
                map.put(key, state);
                pq.add(new Entry(key, state.score, state.version));
            } else {
                List<Entry> used = new ArrayList<>();
                List<String> out = new ArrayList<>();

                while (out.size() < k && !pq.isEmpty()) {
                    Entry e = pq.poll();
                    State state = map.get(e.key);
                    if (state == null || state.version != e.version) {
                        continue;
                    }
                    out.add(e.key);
                    used.add(e);
                }

                for (Entry e : used) pq.add(e);
                if (out.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    results.add(String.join(" ", out));
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
