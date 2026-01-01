import java.util.*;

class Solution {
    List<List<Integer>> result;
    
    public List<List<Integer>> placeLights(int n, int k, int d) {
        result = new ArrayList<>();
        backtrack(0, 0, n, k, d, new ArrayList<>());
        return result;
    }

    private void backtrack(int start_pos, int lights_placed, int n, int k, int d, List<Integer> current) {
        if (lights_placed == k) {
            result.add(new ArrayList<>(current));
            return;
        }

        int remaining_lights = k - lights_placed;
        int remaining_positions = n - start_pos;
        if (remaining_positions < remaining_lights) return;

        for (int pos = start_pos; pos < n; pos++) {
            if (current.isEmpty() || pos - current.get(current.size() - 1) >= d) {
                current.add(pos);
                backtrack(pos + 1, lights_placed + 1, n, k, d, current);
                current.remove(current.size() - 1);
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int d = sc.nextInt();
        
        Solution sol = new Solution();
        List<List<Integer>> res = sol.placeLights(n, k, d);
        if(res.isEmpty()) {
            System.out.println("NONE");
        } else {
            for(List<Integer> row : res) {
                for(int i=0; i<row.size(); i++) {
                    System.out.print(row.get(i) + (i==row.size()-1?"":" "));
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
