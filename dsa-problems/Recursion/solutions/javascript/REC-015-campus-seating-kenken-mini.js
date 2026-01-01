const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    const res = sol.solveLatinSquare(n);
    
    res.forEach(row => console.log(row.join(' ')));
});

class Solution {
    solveLatinSquare(n) {
        const grid = Array.from({length: n}, () => Array(n).fill(0));
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                grid[i][j] = ((i + j) % n) + 1;
            }
        }
        return grid;
    }
}
