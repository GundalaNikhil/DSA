const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    
    if(ptr >= tokens.length) return;
    const n = parseInt(tokens[ptr++]);
    const target = parseInt(tokens[ptr++]);
    
    const values = [];
    for(let i=0; i<n; i++) {
        if(ptr < tokens.length) values.push(parseInt(tokens[ptr++]));
    }
    
    const sol = new Solution();
    console.log(sol.countCombinations(values, target));
});

class Solution {
    countCombinations(values, target) {
        return this.backtrack(0, 0, values, target);
    }

    backtrack(index, currentSum, values, target) {
        if (currentSum === target) {
            return 1;
        }
        if (currentSum > target || index === values.length) {
            return 0;
        }

        let count = 0;
        const value = values[index];

        // Option 1: Don't take any of the current value
        count += this.backtrack(index + 1, currentSum, values, target);

        // Option 2: Take 1 or more of this value
        let count_used = 1;
        while (currentSum + value * count_used <= target) {
            count += this.backtrack(index + 1, currentSum + value * count_used, values, target);
            count_used++;
        }
        return count;
    }
}
