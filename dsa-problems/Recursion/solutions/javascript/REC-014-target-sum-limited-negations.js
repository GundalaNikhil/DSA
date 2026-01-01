const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const k = parseInt(tokens[ptr++]);
    const target = parseInt(tokens[ptr++]);
    
    const nums = [];
    for(let i=0; i<n; i++) nums.push(parseInt(tokens[ptr++]));
    
    const sol = new Solution();
    if(sol.countAssignments(nums, k, target)) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});

class Solution {
    countAssignments(nums, k, target) {
        this.nums = nums;
        this.k = k;
        this.target = target;
        this.n = nums.length;
        this.memo = new Map();
        return this.backtrack(0, 0, 0);
    }
    
    backtrack(index, current_sum, negations) {
        if (index === this.n) return current_sum === this.target;
        
        const key = `${index},${current_sum},${negations}`;
        if (this.memo.has(key)) return this.memo.get(key);
        
        if (this.backtrack(index + 1, current_sum + this.nums[index], negations)) {
            this.memo.set(key, true);
            return true;
        }
        
        if (negations < this.k) {
            if (this.backtrack(index + 1, current_sum - this.nums[index], negations + 1)) {
                this.memo.set(key, true);
                return true;
            }
        }
        
        this.memo.set(key, false);
        return false;
    }
}
