const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const b = parseInt(tokens[ptr++]);
    
    // JS 2D array
    const blocked = Array.from({length: n}, () => Array(n).fill(false));
    for(let i=0; i<b; i++) {
        if(ptr < tokens.length) {
            const r = parseInt(tokens[ptr++]);
            const c = parseInt(tokens[ptr++]);
            if(r >= 0 && r < n && c >= 0 && c < n) blocked[r][c] = true;
        }
    }
    
    const sol = new Solution();
    if(sol.knightTour(n, blocked)) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});

class Solution {
    knightTour(n, blocked) {
        this.N = n;
        this.blocked = blocked;
        this.total_unblocked = 0;
        for(let r=0; r<n; r++)
            for(let c=0; c<n; c++)
                if(!blocked[r][c]) this.total_unblocked++;
        
        if(this.total_unblocked === 0) return true;
        if(blocked[0][0]) return false;
        if(this.total_unblocked === 1) return true;
        
        this.visited = Array.from({length: n}, () => Array(n).fill(false));
        this.vis(0, 0, true);
        
        this.dr = [-2, -2, -1, -1, 1, 1, 2, 2];
        this.dc = [-1, 1, -2, 2, -2, 2, -1, 1];
        
        return this.dfs(0, 0, 1);
    }
    
    vis(r, c, val) {
        this.visited[r][c] = val;
    }
    
    isVis(r, c) {
        return this.visited[r][c];
    }
    
    countOnward(r, c) {
        let cnt = 0;
        for(let i=0; i<8; i++) {
            let nr = r + this.dr[i];
            let nc = c + this.dc[i];
            if(nr >= 0 && nr < this.N && nc >= 0 && nc < this.N && !this.blocked[nr][nc] && !this.isVis(nr, nc)) {
                cnt++;
            }
        }
        return cnt;
    }
    
    dfs(r, c, count) {
        if (count === this.total_unblocked) return true;
        
        const moves = [];
        for(let i=0; i<8; i++) {
            let nr = r + this.dr[i];
            let nc = c + this.dc[i];
            if(nr >= 0 && nr < this.N && nc >= 0 && nc < this.N && !this.blocked[nr][nc] && !this.isVis(nr, nc)) {
                moves.push({p: this.countOnward(nr, nc), idx: i});
            }
        }
        
        if(moves.length === 0) return false;
        
        moves.sort((a, b) => a.p - b.p);
        
        for(let m of moves) {
            let i = m.idx;
            let nr = r + this.dr[i];
            let nc = c + this.dc[i];
            
            this.vis(nr, nc, true);
            if(this.dfs(nr, nc, count + 1)) return true;
            this.vis(nr, nc, false);
        }
        return false;
    }
}
