const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        pts.sort((a, b) => {
            if (a.x !== b.x) return a.x < b.x ? -1 : 1;
            if (a.y !== b.y) return a.y < b.y ? -1 : 1;
            return 0;
        });
        pts = pts.filter((p, i) => i === 0 || p.x !== pts[i-1].x || p.y !== pts[i-1].y);
        
        if (pts.length <= 1) return 0n;
        if (pts.length === 2) return (pts[0].x-pts[1].x)**2n + (pts[0].y-pts[1].y)**2n;
        
        const cross = (o, a, b) => (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
        let lower = [];
        for (let p of pts) {
            while (lower.length >= 2 && cross(lower[lower.length-2], lower[lower.length-1], p) <= 0n) lower.pop();
            lower.push(p);
        }
        let upper = [];
        for (let i = pts.length - 1; i >= 0; i--) {
            let p = pts[i];
            while (upper.length >= 2 && cross(upper[upper.length-2], upper[upper.length-1], p) <= 0n) upper.pop();
            upper.push(p);
        }
        lower.pop(); upper.pop();
        let hull = lower.concat(upper);
        
        if (hull.length <= 1) return 0n;
        if (hull.length === 2) return (hull[0].x-hull[1].x)**2n + (hull[0].y-hull[1].y)**2n;
        
        let maxD2 = 0n;
        let k = 1;
        let n = hull.length;
        
        const distSq = (a, b) => (a.x-b.x)**2n + (a.y-b.y)**2n;
        const absVal = (n) => n < 0n ? -n : n;

        for (let i = 0; i < n; i++) {
            while (true) {
                let nextK = (k + 1) % n;
                let p_i = hull[i];
                let p_next = hull[(i+1)%n];
                
                let distK = absVal(cross(p_i, p_next, hull[k]));
                let distNextK = absVal(cross(p_i, p_next, hull[nextK]));
                
                if (distNextK > distK) {
                    k = nextK;
                } else {
                    break;
                }
            }
            
            let d1 = distSq(hull[i], hull[k]);
            let d2 = distSq(hull[(i+1)%n], hull[k]);
            if (d1 > maxD2) maxD2 = d1;
            if (d2 > maxD2) maxD2 = d2;
        }
        return maxD2.toString();
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
