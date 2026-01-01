const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const nums = [];
    for(let i=0; i<n; i++) nums.push(parseInt(tokens[ptr++]));
    
    const ops = tokens[ptr++];
    const target = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.findFlipIndex(nums, ops, target));
});

class Solution {
    findFlipIndex(nums, ops, target) {
        const n_ops = ops.length;
        for (let flip_idx = 0; flip_idx < n_ops; flip_idx++) {
            let current_sum = BigInt(nums[0]);
            for (let i = 0; i < n_ops; i++) {
                let op;
                if (i === flip_idx) {
                    op = (ops[i] === '+') ? '-' : '+';
                } else {
                    op = ops[i];
                }

                if (op === '+') {
                    current_sum += BigInt(nums[i + 1]);
                } else {
                    current_sum -= BigInt(nums[i + 1]);
                }
            }
            if (current_sum === BigInt(target)) {
                return flip_idx;
            }
        }
        return -1;
    }
}
