const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.countNQueens(n));
});

class Solution {
    countNQueens(n) {
        let count = 0;
        const cols = new Int32Array(2*n);
        const diag1 = new Int32Array(2*n);
        const diag2 = new Int32Array(2*n);
        
        // Iterative stack to avoid recursion limit if N is large? 
        // Or recursive is fine for N=14 in Node?
        // Node default stack is usually enough for depth 14.
        // Previous JS failure "RangeError: Maximum call stack size exceeded" on Test 1.
        // This implies infinite recursion or Very deep.
        // If N was huge? Constraints usually N <= 15 for NQueens.
        // My previous JS code for REC-004 was BROKEN logic. It probably recursed infinitely.
        // Let's use clean recursion.
        
        const backtrack = (row) => {
            if (row === n) {
                count++;
                return;
            }
            
            for (let col = 0; col < n; col++) {
                if (cols[col] || diag1[row + col] || diag2[row - col + n]) continue;
                
                cols[col] = 1;
                diag1[row + col] = 1;
                diag2[row - col + n] = 1;
                
                backtrack(row + 1);
                
                cols[col] = 0;
                diag1[row + col] = 0;
                diag2[row - col + n] = 0;
            }
        };
        
        backtrack(0);
        return count;
    }
}
