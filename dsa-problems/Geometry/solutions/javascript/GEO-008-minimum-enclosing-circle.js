const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let pts = xs.map((x, i) => ({x: Number(x), y: Number(ys[i])}));
        
        for (let i = pts.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [pts[i], pts[j]] = [pts[j], pts[i]];
        }

        const dist = (p1, p2) => Math.hypot(p1.x - p2.x, p1.y - p2.y);
        
        const circleTwo = (p1, p2) => {
            let cx = (p1.x + p2.x) / 2.0;
            let cy = (p1.y + p2.y) / 2.0;
            return {x: cx, y: cy, r: dist(p1, p2) / 2.0};
        };

        const circleThree = (a, b, c) => {
            let d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
            if (Math.abs(d) < 1e-9) return {x: 0, y: 0, r: 0};
            let ux = ((a.x*a.x + a.y*a.y)*(b.y-c.y) + (b.x*b.x + b.y*b.y)*(c.y-a.y) + (c.x*c.x + c.y*c.y)*(a.y-b.y)) / d;
            let uy = ((a.x*a.x + a.y*a.y)*(c.x-b.x) + (b.x*b.x + b.y*b.y)*(a.x-c.x) + (c.x*c.x + c.y*c.y)*(b.x-a.x)) / d;
            return {x: ux, y: uy, r: dist({x: ux, y: uy}, a)};
        };

        const inside = (p, c) => dist(p, c) <= c.r + 1e-9;

        let c = {x: pts[0].x, y: pts[0].y, r: 0};
        for (let i = 1; i < pts.length; i++) {
            if (inside(pts[i], c)) continue;
            c = {x: pts[i].x, y: pts[i].y, r: 0};
            for (let j = 0; j < i; j++) {
                if (inside(pts[j], c)) continue;
                c = circleTwo(pts[i], pts[j]);
                for (let k = 0; k < j; k++) {
                    if (inside(pts[k], c)) continue;
                    c = circleThree(pts[i], pts[j], pts[k]);
                }
            }
        }
        return c;
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
    const c = sol.solve(xs, ys);
    
    let cx = Math.abs(c.x) < 1e-9 ? 0.0 : c.x;
    let cy = Math.abs(c.y) < 1e-9 ? 0.0 : c.y;
    let r = Math.abs(c.r) < 1e-9 ? 0.0 : c.r;

    console.log(cx.toFixed(6));
    console.log(cy.toFixed(6));
    console.log(r.toFixed(6));
});
