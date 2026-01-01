const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const m = parseInt(tokens[ptr++]);
    
    const edges = [];
    for(let i=0; i<m; i++) {
        edges.push([parseInt(tokens[ptr++]), parseInt(tokens[ptr++])]);
    }
    
    const sol = new Solution();
    const res = sol.findOrder(n, edges);
    if (res.length === 0) {
        console.log("IMPOSSIBLE");
    } else {
        console.log(res.join(" "));
    }
});

class Solution {
    findOrder(n, edges) {
        const adj = Array.from({length: n}, () => []);
        const inDegree = Array(n).fill(0);
        
        for(let [u, v] of edges) {
            adj[u].push(v);
            inDegree[v]++;
        }
        
        const q = []; // Simple array as Queue
        for(let i=0; i<n; i++) {
            if(inDegree[i] === 0) q.push(i);
        }
        
        const result = [];
        let head = 0; // Pointer for queue for O(1) dequeue effect
        
        while(head < q.length) {
            const u = q[head++];
            result.push(u);
            
            for(let v of adj[u]) {
                inDegree[v]--;
                if(inDegree[v] === 0) q.push(v);
            }
        }
        
        if (result.length === n) return result;
        return [];
    }
}
