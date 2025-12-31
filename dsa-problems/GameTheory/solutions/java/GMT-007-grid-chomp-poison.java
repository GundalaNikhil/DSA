import java.util.*;

class Solution {
    Map<List<Integer>, Boolean> memo = new HashMap<>();
    int[][] poisons;
    int K;

    public String chompGame(int R, int C, int[][] poisons) {
        this.poisons = poisons;
        this.K = poisons.length;
        List<Integer> initialState = new ArrayList<>();
        for (int i = 0; i < C; i++) initialState.add(R);
        
        return canWin(initialState) ? "First" : "Second";
    }

    private boolean canWin(List<Integer> state) {
        if (memo.containsKey(state)) return memo.get(state);

        boolean canReachLosing = false;
        int C = state.size();

        // Try all possible moves (r, c)
        // A move is valid if r < state[c] (cell exists)
        // AND it doesn't eat any poison
        for (int c = 0; c < C; c++) {
            for (int r = 0; r < state.get(c); r++) {
                if (isValid(r, c)) {
                    List<Integer> nextState = new ArrayList<>(state);
                    // Update heights for columns >= c
                    for (int i = c; i < C; i++) {
                        nextState.set(i, Math.min(nextState.get(i), r));
                    }
                    
                    // Optimization: If state didn't change, it's not a move (eating nothing)
                    // But here r < state[c], so we always remove at least (r, c).
                    
                    if (!canWin(nextState)) {
                        canReachLosing = true;
                        break;
                    }
                }
            }
            if (canReachLosing) break;
        }

        memo.put(state, canReachLosing);
        return canReachLosing;
    }

    private boolean isValid(int r, int c) {
        for (int[] p : poisons) {
            if (p[0] >= r && p[1] >= c) return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int R = sc.nextInt();
            int C = sc.nextInt();
            int K = sc.nextInt();
            int[][] poisons = new int[K][2];
            for (int i = 0; i < K; i++) {
                poisons[i][0] = sc.nextInt();
                poisons[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.chompGame(R, C, poisons));
        }
        sc.close();
    }
}
