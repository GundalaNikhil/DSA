const readline = require('readline');

class Solution {
    solve(xs, ys, theta) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        // Remove duplicates with Correct Sort
        pts.sort((a, b) => {
            if (a.x !== b.x) return a.x < b.x ? -1 : 1;
            if (a.y !== b.y) return a.y < b.y ? -1 : 1;
            return 0;
        });
        pts = pts.filter((p, i) => i === 0 || p.x !== pts[i-1].x || p.y !== pts[i-1].y);

        if (pts.length <= 1) return pts;

        const cross = (o, a, b) => (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);

        let lower = [];
        for (let p of pts) {
            while (lower.length >= 2 && cross(lower[lower.length-2], lower[lower.length-1], p) <= 0n) {
                lower.pop();
            }
            lower.push(p);
        }
        let upper = [];
        for (let i = pts.length - 1; i >= 0; i--) {
            let p = pts[i];
            while (upper.length >= 2 && cross(upper[upper.length-2], upper[upper.length-1], p) <= 0n) {
                upper.pop();
            }
            upper.push(p);
        }
        
        lower.pop();
        upper.pop();
        let hull = lower.concat(upper);

        if (hull.length <= 2) return hull;

        const h = hull.length;
        const cosT = Math.cos(theta * Math.PI / 180.0);
        let keep = [];

        for (let i = 0; i < h; i++) {
            let prev = hull[(i - 1 + h) % h];
            let curr = hull[i];
            let nxt = hull[(i + 1) % h];

            let ux = Number(prev.x - curr.x);
            let uy = Number(prev.y - curr.y);
            let vx = Number(nxt.x - curr.x);
            let vy = Number(nxt.y - curr.y);

            let lenU = Math.hypot(ux, uy);
            let lenV = Math.hypot(vx, vy);

            if (lenU === 0 || lenV === 0) {
                keep.push(curr);
                continue;
            }

            let dot = ux * vx + uy * vy;
            let cosA = dot / (lenU * lenV);

            if (cosA <= cosT + 1e-9) {
                keep.push(curr);
            }
        }
        return keep;
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
    let xs = [], ys = [];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }
    let theta = parseInt(nextInt());

    const sol = new Solution();
    const res = sol.solve(xs, ys, theta);
    
    if (res.length === 0) console.log(0);
    else {
        console.log(res.length);
        for(let p of res) console.log(`${p.x} ${p.y}`);
    }
});
