const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        // Sort by X
        pts.sort((a, b) => {
            if (a.x < b.x) return -1;
            if (a.x > b.x) return 1;
            return 0;
        });
        
        let unique = new Set(pts.map(p => `${p.x},${p.y}`));
        if (unique.size !== pts.length) return "0";
        
        const distSq = (a, b) => (a.x-b.x)**2n + (a.y-b.y)**2n;
        const minBig = (a, b) => (a === -1n) ? b : ((b === -1n) ? a : (a < b ? a : b));
        
        const rec = (arr) => {
            let n = arr.length;
            if (n <= 3) {
                let minD = -1n;
                for(let i=0; i<n; i++) {
                    for(let j=i+1; j<n; j++) {
                        let d = distSq(arr[i], arr[j]);
                        if (minD === -1n || d < minD) minD = d;
                    }
                }
                arr.sort((a, b) => {
                    if (a.y < b.y) return -1;
                    if (a.y > b.y) return 1;
                    return 0;
                });
                return minD === -1n ? 0n : minD; 
            }
            
            let mid = Math.floor(n / 2);
            let midX = arr[mid].x;
            let left = arr.slice(0, mid);
            let right = arr.slice(mid);
            
            let dL = rec(left);
            let dR = rec(right);
            
            let d = minBig(dL, dR);
            if (d === -1n) d = 0n;
            
            arr.sort((a, b) => {
                if (a.y < b.y) return -1;
                if (a.y > b.y) return 1;
                return 0;
            });
            
            let strip = [];
            for(let p of arr) {
                let dx = p.x - midX;
                if (d === -1n || dx*dx < d) strip.push(p);
            }
            
            for(let i=0; i<strip.length; i++) {
                for(let j=i+1; j<strip.length; j++) {
                     let dy = strip[j].y - strip[i].y;
                     if (d !== -1n && dy*dy >= d) break;
                     let currD = distSq(strip[i], strip[j]);
                     if (d === -1n || currD < d) d = currD;
                }
            }
            return d === -1n ? 0n : d;
        };
        
        return rec(pts).toString();
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
    const nextInt = () => next(); 

    let n = parseInt(nextInt());
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
