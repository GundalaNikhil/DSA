import java.util.*;

class Solution {
    int N;
    int total_unblocked;
    boolean[][] blocked;
    boolean[][] visited;
    int[] dr = {-2, -2, -1, -1, 1, 1, 2, 2};
    int[] dc = {-1, 1, -2, 2, -2, 2, -1, 1};

    public boolean knightTour(int n, boolean[][] blk) {
        N = n;
        blocked = blk;
        total_unblocked = 0;
        for(int i=0; i<n; i++) 
            for(int j=0; j<n; j++) 
                if(!blocked[i][j]) total_unblocked++;
        
        if(total_unblocked == 0) return true;
        if(blocked[0][0]) return false;
        if(total_unblocked == 1) return true;

        visited = new boolean[n][n];
        visited[0][0] = true;
        return dfs(0, 0, 1);
    }

    int countOnward(int r, int c) {
        int cnt = 0;
        for(int i=0; i<8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                cnt++;
            }
        }
        return cnt;
    }

    boolean dfs(int r, int c, int count) {
        if (count == total_unblocked) return true;

        List<int[]> moves = new ArrayList<>(); // {priority, dr_index}
        for(int i=0; i<8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                moves.add(new int[]{countOnward(nr, nc), i});
            }
        }
        
        if(moves.isEmpty()) return false;
        
        moves.sort((a, b) -> Integer.compare(a[0], b[0]));

        for(int[] p : moves) {
            int i = p[1];
            int nr = r + dr[i];
            int nc = c + dc[i];
            
            visited[nr][nc] = true;
            if(dfs(nr, nc, count + 1)) return true;
            visited[nr][nc] = false;
        }
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int b = sc.nextInt();
        
        boolean[][] blocked = new boolean[n][n];
        for(int i=0; i<b; i++) {
            if(sc.hasNextInt()) {
                int r = sc.nextInt();
                int c = sc.nextInt();
                if(r >= 0 && r < n && c >= 0 && c < n) blocked[r][c] = true;
            }
        }
        
        Solution sol = new Solution();
        if(sol.knightTour(n, blocked)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
