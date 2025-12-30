import java.util.*;

class Solution {
    static class Item {
        int value;
        double score;
        Item(int v, double s) { this.value = v; this.score = s; }
    }

    public List<Integer> topKWithDecay(int[][] events, int now, int D, int k) {
        Map<Integer, Double> map = new HashMap<>();
        
        for (int[] event : events) {
            int v = event[0];
            int t = event[1];
            double term = Math.exp(-(double)(now - t) / D);
            map.put(v, map.getOrDefault(v, 0.0) + term);
        }

        List<Item> items = new ArrayList<>();
        for (Map.Entry<Integer, Double> entry : map.entrySet()) {
            items.add(new Item(entry.getKey(), entry.getValue()));
        }

        // Sort: Descending Score, Ascending Value
        items.sort((a, b) -> {
            if (Double.compare(b.score, a.score) != 0) {
                return Double.compare(b.score, a.score);
            }
            return Integer.compare(a.value, b.value);
        });

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k && i < items.size(); i++) {
            result.add(items.get(i).value);
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[][] events = new int[n][2];
        for (int i = 0; i < n; i++) {
            events[i][0] = sc.nextInt();
            events[i][1] = sc.nextInt();
        }
        int now = sc.nextInt();
        int D = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> result = solution.topKWithDecay(events, now, D, k);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append(i == result.size() - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
