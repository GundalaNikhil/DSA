const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const r = parseInt(tokens[ptr++]);
    const c = parseInt(tokens[ptr++]);
    const T = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.countPaths(r, c, T).toString());
});

class Solution {
    countPaths(r, c, T) {
        this.R = r;
        this.C = c;
        this.T = T;
        this.memo = new Map();
        return this.dfs(0, 0, -1, 0);
    }

    dfs(r, c, lastDir, turns) {
        if (r === this.R - 1 && c === this.C - 1) return 1;
        if (turns > this.T) return 0;
        
        const key = `${r},${c},${lastDir},${turns}`;
        if (this.memo.has(key)) return this.memo.get(key);

        let count = 0;

        // Dir 0: Right (c+1)
        if (c + 1 < this.C) {
            let newTurns = turns;
            if (lastDir !== -1 && lastDir !== 0) newTurns++;
            count += this.dfs(r, c + 1, 0, newTurns);
        }

        // Dir 1: Down (r+1)
        if (r + 1 < this.R) {
            let newTurns = turns;
            if (lastDir !== -1 && lastDir !== 1) newTurns++;
            count += this.dfs(r + 1, c, 1, newTurns);
        }

        this.memo.set(key, count);
        return count;
    }
}
