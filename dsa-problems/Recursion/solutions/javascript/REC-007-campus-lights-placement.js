const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const k = parseInt(tokens[ptr++]);
    const d = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    const res = sol.placeLights(n, k, d);
    
    if (res.length === 0) {
        console.log("NONE");
    } else {
        res.forEach(row => console.log(row.join(' ')));
    }
});

class Solution {
    placeLights(n, k, d) {
        const result = [];
        
        const backtrack = (start_pos, lights_placed, current) => {
            if (lights_placed === k) {
                result.push([...current]);
                return;
            }
            
            const remaining_lights = k - lights_placed;
            const remaining_positions = n - start_pos;
            if (remaining_positions < remaining_lights) return;
            
            for (let pos = start_pos; pos < n; pos++) {
                if (current.length === 0 || pos - current[current.length - 1] >= d) {
                    current.push(pos);
                    backtrack(pos + 1, lights_placed + 1, current);
                    current.pop();
                }
            }
        };
        
        backtrack(0, 0, []);
        return result;
    }
}
