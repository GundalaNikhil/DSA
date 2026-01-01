const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const L = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.minPalindromePartitions(s, L));
});

class Solution {
    minPalindromePartitions(s, L) {
        const n = s.length;
        const is_pal = Array.from({length: n}, () => Array(n).fill(false));
        
        for (let len = 1; len <= n; len++) {
            for (let i = 0; i <= n - len; i++) {
                let j = i + len - 1;
                if (s[i] === s[j]) {
                    if (len <= 2 || is_pal[i + 1][j - 1]) {
                        is_pal[i][j] = true;
                    }
                }
            }
        }
        
        this.current_min = n + 1;
        this.best_partition = null;
        
        const backtrack = (start, current) => {
            if (start === n) {
                const count = current.length;
                if (count < this.current_min) {
                    this.current_min = count;
                    this.best_partition = [...current];
                }
                return;
            }
            
            if (current.length >= this.current_min) return;
            
            const max_end = Math.min(start + L, n);
            for (let end = start; end < max_end; end++) {
                if (is_pal[start][end]) {
                    current.push(s.substring(start, end + 1));
                    backtrack(end + 1, current);
                    current.pop();
                }
            }
        };
        
        backtrack(0, []);
        
        if (!this.best_partition) {
            return s.split('').join(' ');
        }
        
        return this.best_partition.join(' ');
    }
}
