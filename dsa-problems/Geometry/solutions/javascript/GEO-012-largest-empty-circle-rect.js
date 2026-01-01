const readline = require('readline');

class Solution {
    solve(xL, yB, xR, yT, xs, ys) {
        let pts = xs.map((x, i) => ({x: Number(x), y: Number(ys[i])}));
        
        const distSq = (x1, y1, x2, y2) => (x1-x2)**2 + (y1-y2)**2;
        
        const getRadius = (x, y) => {
            if (x < xL || x > xR || y < yB || y > yT) return 0.0;
            let r = Math.min(x - xL, xR - x, y - yB, yT - y);
            if (r <= 1e-12) return 0.0;
            
            for (let p of pts) {
                let d2 = distSq(x, y, p.x, p.y);
                if (d2 < r * r) return Math.sqrt(d2);
            }
            return r;
        };

        let candidates = [];
        candidates.push({x: (xL+xR)/2, y: (yB+yT)/2});
        
        for (let p of pts) {
            candidates.push({x: p.x, y: (p.y+yB)/2});
            candidates.push({x: p.x, y: (p.y+yT)/2});
            candidates.push({x: (p.x+xL)/2, y: p.y});
            candidates.push({x: (p.x+xR)/2, y: p.y});
        }
        
        if (pts.length <= 100) {
            for (let i = 0; i < pts.length; i++) {
                for (let j = i + 1; j < pts.length; j++) {
                    candidates.push({x: (pts[i].x+pts[j].x)/2, y: (pts[i].y+pts[j].y)/2});
                }
            }
        }
        
        // Grid Search (Robustness)
        const GRID = 12;
        for (let i = 0; i <= GRID; i++) {
            for (let j = 0; j <= GRID; j++) {
                 let gx = xL + (xR - xL) * i / GRID;
                 let gy = yB + (yT - yB) * j / GRID;
                 candidates.push({x: gx, y: gy});
            }
        }
        
        let scored = candidates.map(c => ({c, r: getRadius(c.x, c.y)}));
        scored.sort((a, b) => b.r - a.r);
        
        let starts = [];
        // Top 40 to be safe
        for (let i = 0; i < Math.min(scored.length, 40); i++) {
            starts.push(scored[i].c);
        }
        
        let bestR = scored.length > 0 ? scored[0].r : 0.0;
        
        let stepSize = Math.max(xR-xL, yT-yB) / 2.0;
        let precision = 1e-7; // Very High precision
        
        let seed = 1337;
        const rand = () => {
            seed = (seed * 1664525 + 1013904223) % 4294967296;
            return seed / 4294967296;
        };
        
        for (let start of starts) {
            let currX = start.x;
            let currY = start.y;
            let currR = getRadius(currX, currY);
            let tempStep = stepSize;
            
            while (tempStep > precision) {
                let improved = false;
                let bestNeighR = currR;
                let bestNeighX = currX;
                let bestNeighY = currY;
                
                // Random Rotation Directions
                let angle = rand() * 2 * Math.PI;
                for (let k = 0; k < 8; k++) {
                    let a = angle + k * (Math.PI / 4.0);
                    let dx = Math.cos(a);
                    let dy = Math.sin(a);
                    
                    let nx = currX + dx * tempStep;
                    let ny = currY + dy * tempStep;
                    nx = Math.max(xL, Math.min(xR, nx));
                    ny = Math.max(yB, Math.min(yT, ny));
                    
                    let nr = getRadius(nx, ny);
                    if (nr > bestNeighR) {
                        bestNeighR = nr;
                        bestNeighX = nx;
                        bestNeighY = ny;
                        improved = true;
                    }
                }
                
                if (improved) {
                    currX = bestNeighX;
                    currY = bestNeighY;
                    currR = bestNeighR;
                } else {
                    tempStep *= 0.85; // Slow decay
                }
            }
            bestR = Math.max(bestR, currR);
        }
        return bestR;
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

    let xL = nextInt(), yB = nextInt(), xR = nextInt(), yT = nextInt();
    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xL, yB, xR, yT, xs, ys).toFixed(6));
});
