const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let n = xs.length;
        if (n <= 1) return 0;
        
        let min_dist = new Array(n).fill(Infinity);
        let visited = new Int8Array(n).fill(0);
        min_dist[0] = 0;
        let total = 0;
        
        for (let i = 0; i < n; i++) {
            let u = -1;
            let minVal = Infinity;
            for (let j = 0; j < n; j++) {
                if (visited[j] === 0 && min_dist[j] < minVal) {
                    minVal = min_dist[j];
                    u = j;
                }
            }
            
            if (u === -1 || minVal === Infinity) break;
            visited[u] = 1;
            total += minVal;
            
            let ux = xs[u];
            let uy = ys[u];
            
            for (let v = 0; v < n; v++) {
                if (visited[v] === 0) {
                    let d = Math.abs(ux - xs[v]) + Math.abs(uy - ys[v]);
                    if (d < min_dist[v]) min_dist[v] = d;
                }
            }
        }
        return total;
    }
}
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());

    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xs, ys).toString());
});
