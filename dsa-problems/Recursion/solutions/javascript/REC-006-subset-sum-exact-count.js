const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    
    if(ptr >= tokens.length) return;
    const n = parseInt(tokens[ptr++]);
    const k = parseInt(tokens[ptr++]);
    const target = parseInt(tokens[ptr++]);
    
    const arr = [];
    for(let i=0; i<n; i++) {
        if(ptr < tokens.length) arr.push(parseInt(tokens[ptr++]));
    }
    
    const sol = new Solution();
    const res = sol.findSubset(arr, k, target);
    
    if(res.length === 0) {
        console.log("NONE");
    } else {
        console.log(res.join(' '));
    }
});

class Solution {
    findSubset(arr, k, target) {
        const current = [];
        if (this.backtrack(0, 0, 0, arr, k, target, current)) {
            return current;
        }
        return [];
    }

    backtrack(index, count, currentSum, arr, k, target, current) {
        if (count === k) {
            return currentSum === target;
        }
        if (index === arr.length) {
            return false;
        }
        
        // Pruning
        if (arr.length - index < k - count) {
            return false;
        }

        // Option 1: Include
        current.push(arr[index]);
        if (this.backtrack(index + 1, count + 1, currentSum + arr[index], arr, k, target, current)) {
            return true;
        }
        current.pop();

        // Option 2: Exclude
        if (this.backtrack(index + 1, count, currentSum, arr, k, target, current)) {
            return true;
        }

        return false;
    }
}
