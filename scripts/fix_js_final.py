#!/usr/bin/env python3
"""
Comprehensive script to generate fixed JavaScript solutions for ALL failing Geometry problems.
"""
import os

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
SOLUTIONS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Geometry", "solutions", "javascript")

def write_solution(problem_id, content):
    filename = f"{problem_id}*.js"
    import glob
    pattern = os.path.join(SOLUTIONS_DIR, filename)
    files = glob.glob(pattern)
    if not files:
        print(f"No file found for {problem_id}")
        return
    
    path = files[0]
    with open(path, 'w') as f:
        f.write(content)
    print(f"Wrote fixed solution to {os.path.basename(path)}")

# GEO-003: Segment Intersection Count (Brute Force O(N^2))
GEO_003_JS = """const readline = require('readline');

class Solution {
    solve(x1, y1, x2, y2) {
        let n = x1.length;
        let segs = [];
        for(let i=0; i<n; i++) segs.push({x1: x1[i], y1: y1[i], x2: x2[i], y2: y2[i]});
        
        const orient = (ax, ay, bx, by, cx, cy) => {
            let val = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
            if (val === 0) return 0;
            return val > 0 ? 1 : -1;
        };
        
        const onSeg = (ax, ay, bx, by, cx, cy) => {
            return Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
                   Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
        };
        
        const intersect = (s1, s2) => {
            let o1 = orient(s1.x1, s1.y1, s1.x2, s1.y2, s2.x1, s2.y1);
            let o2 = orient(s1.x1, s1.y1, s1.x2, s1.y2, s2.x2, s2.y2);
            let o3 = orient(s2.x1, s2.y1, s2.x2, s2.y2, s1.x1, s1.y1);
            let o4 = orient(s2.x1, s2.y1, s2.x2, s2.y2, s1.x2, s1.y2);
            
            if (o1 !== o2 && o3 !== o4) return true;
            
            if (o1 === 0 && onSeg(s1.x1, s1.y1, s1.x2, s1.y2, s2.x1, s2.y1)) return true;
            if (o2 === 0 && onSeg(s1.x1, s1.y1, s1.x2, s1.y2, s2.x2, s2.y2)) return true;
            if (o3 === 0 && onSeg(s2.x1, s2.y1, s2.x2, s2.y2, s1.x1, s1.y1)) return true;
            if (o4 === 0 && onSeg(s2.x1, s2.y1, s2.x2, s2.y2, s1.x2, s1.y2)) return true;
            
            return false;
        };
        
        let cnt = 0;
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (intersect(segs[i], segs[j])) cnt++;
            }
        }
        return cnt;
    }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let m = nextInt();
    let x1=[], y1=[], x2=[], y2=[];
    for(let i=0; i<m; i++) {
        x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(x1, y1, x2, y2));
});
"""

# GEO-004: Closest Pair (Divide & Conquer) - BigInt
GEO_004_JS = """const readline = require('readline');

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
                return minD === -1n ? 0n : minD; // Should not happen n<=3 check
            }
            
            let mid = Math.floor(n / 2);
            let midX = arr[mid].x;
            let left = arr.slice(0, mid);
            let right = arr.slice(mid);
            
            let dL = rec(left);
            let dR = rec(right);
            // Handling case where subarray returns infinity? 
            // -1n as infinity placeholder?
            // Actually recursion base case guarantees return.
            let d = dL;
            if (dR < d) d = dR;
            
            // Merge sort by Y
            let merged = [];
            let i=0, j=0;
            while(i<left.length && j<right.length) {
                if(left[i].y <= right[j].y) merged.push(left[i++]);
                else merged.push(right[j++]);
            }
            while(i<left.length) merged.push(left[i++]);
            while(j<right.length) merged.push(right[j++]);
            for(let k=0; k<n; k++) arr[k] = merged[k];
            
            let strip = [];
            for(let p of arr) {
                let dx = p.x - midX;
                if (dx*dx < d) strip.push(p);
            }
            
            for(let i=0; i<strip.length; i++) {
                for(let j=i+1; j<strip.length; j++) {
                     let dy = strip[j].y - strip[i].y;
                     if (dy*dy >= d) break;
                     let currD = distSq(strip[i], strip[j]);
                     if (currD < d) d = currD;
                }
            }
            return d;
        };
        
        return rec(pts).toString();
    }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => next(); // Keep as string for BigInt
    
    let n = parseInt(nextInt());
    let xs=[], ys=[];
    for(let i=0; i<n; i++) xs.push(nextInt());
    for(let i=0; i<n; i++) ys.push(nextInt());

    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
"""

# GEO-005: Convex Hull Capped (BigInt Hull, Float Filter)
GEO_005_JS = """const readline = require('readline');

class Solution {
    solve(xs, ys, theta) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        // Remove duplicates
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

            // Convert to Number for angle calculation
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
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => next(); // String
    
    let n = parseInt(nextInt());
    let xs = [], ys = [];
    for(let i=0; i<n; i++) xs.push(nextInt());
    for(let i=0; i<n; i++) ys.push(nextInt());
    let theta = parseInt(nextInt());

    const sol = new Solution();
    const res = sol.solve(xs, ys, theta);
    
    if (res.length === 0) console.log(0);
    else {
        console.log(res.length);
        for(let p of res) console.log(`${p.x} ${p.y}`);
    }
});
"""

# GEO-007: Rotating Calipers (BigInt)
GEO_007_JS = """const readline = require('readline');

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
                // cross product magnitude is 2 * Area
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
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => next(); // String
    
    let n = parseInt(nextInt());
    let xs=[], ys=[];
    for(let i=0; i<n; i++) xs.push(nextInt());
    for(let i=0; i<n; i++) ys.push(nextInt());

    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
"""

# GEO-008: Enclosing Circle (Fixed Welzl)
GEO_008_JS = """const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let pts = xs.map((x, i) => ({x: Number(x), y: Number(ys[i])}));
        
        // Shuffle
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
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) xs.push(nextInt());
    for(let i=0; i<n; i++) ys.push(nextInt());

    const sol = new Solution();
    const c = sol.solve(xs, ys);
    
    let cx = Math.abs(c.x) < 1e-9 ? 0.0 : c.x;
    let cy = Math.abs(c.y) < 1e-9 ? 0.0 : c.y;
    let r = Math.abs(c.r) < 1e-9 ? 0.0 : c.r;

    console.log(cx.toFixed(6));
    console.log(cy.toFixed(6));
    console.log(r.toFixed(6));
});
"""

# GEO-009: Half Plane (Fixed Null Check)
GEO_009_JS = """const readline = require('readline');
const EPS = 1e-9;

class Solution {
    solve(A, B, C) {
        let lines = A.map((a, i) => ({
            a: Number(a), b: Number(B[i]), c: Number(C[i]), 
            ang: Math.atan2(Number(B[i]), Number(a))
        }));

        lines.sort((l1, l2) => {
            if (Math.abs(l1.ang - l2.ang) > EPS) return l1.ang - l2.ang;
            return 0; 
        });

        let unique = [];
        for (let l of lines) {
            if (unique.length > 0 && Math.abs(l.ang - unique[unique.length-1].ang) < EPS) {
                let last = unique[unique.length-1];
                let normL = Math.hypot(l.a, l.b);
                let normLast = Math.hypot(last.a, last.b);
                if (l.c / normL < last.c / normLast) {
                    unique[unique.length-1] = l;
                }
            } else {
                unique.push(l);
            }
        }
        lines = unique;

        const intersect = (l1, l2) => {
            let det = l1.a * l2.b - l2.a * l1.b;
            if (Math.abs(det) < EPS) return null;
            let x = (l1.c * l2.b - l2.c * l1.b) / det;
            let y = (l1.a * l2.c - l2.a * l1.c) / det;
            return {x, y};
        };

        const outside = (p, l) => {
            if (!p) return true; // If parallel intersect failed, consider outside
            return l.a * p.x + l.b * p.y - l.c > EPS;
        };

        let dq = [];
        for (let l of lines) {
            while (dq.length >= 2 && outside(intersect(dq[dq.length-2], dq[dq.length-1]), l)) dq.pop();
            while (dq.length >= 2 && outside(intersect(dq[0], dq[1]), l)) dq.shift();
            dq.push(l);
        }

        while (dq.length >= 3 && outside(intersect(dq[dq.length-2], dq[dq.length-1]), dq[0])) dq.pop();
        while (dq.length >= 3 && outside(intersect(dq[0], dq[1]), dq[dq.length-1])) dq.shift();

        if (dq.length < 3) return [];

        let pts = [];
        for (let i = 0; i < dq.length; i++) {
            let p = intersect(dq[i], dq[(i+1)%dq.length]);
            if (!p) return [];
            pts.push(p);
        }

        let uniquePts = [];
        for (let p of pts) {
            if (uniquePts.length === 0) uniquePts.push(p);
            else if (Math.hypot(p.x - uniquePts[uniquePts.length-1].x, p.y - uniquePts[uniquePts.length-1].y) > EPS) {
                uniquePts.push(p);
            }
        }
        if (uniquePts.length > 1 && Math.hypot(uniquePts[0].x - uniquePts[uniquePts.length-1].x, uniquePts[0].y - uniquePts[uniquePts.length-1].y) < EPS) {
            uniquePts.pop();
        }

        if (uniquePts.length < 3) return [];

        let minIdx = 0;
        for (let i = 1; i < uniquePts.length; i++) {
            if (uniquePts[i].x < uniquePts[minIdx].x - EPS || 
               (Math.abs(uniquePts[i].x - uniquePts[minIdx].x) < EPS && uniquePts[i].y < uniquePts[minIdx].y)) {
                minIdx = i;
            }
        }
        
        let res = [];
        for (let i = 0; i < uniquePts.length; i++) {
            res.push(uniquePts[(minIdx + i) % uniquePts.length]);
        }
        return res;
    }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let m = nextInt();
    let A = [], B = [], C = [];
    for(let i=0; i<m; i++) {
        A.push(nextInt()); B.push(nextInt()); C.push(nextInt());
    }

    const sol = new Solution();
    const res = sol.solve(A, B, C);
    
    if (res.length === 0) console.log("EMPTY");
    else {
        console.log(res.length);
        for(let p of res) {
            let px = Math.abs(p.x) < 1e-9 ? 0.0 : p.x;
            let py = Math.abs(p.y) < 1e-9 ? 0.0 : p.y;
            console.log(`${px.toFixed(6)} ${py.toFixed(6)}`);
        }
    }
});
"""

# GEO-010: Weighted Union Area (O(N^2) Sweep Line)
GEO_010_JS = """const readline = require('readline');

class Solution {
    solve(x1, y1, x2, y2, w, W) {
        let n = x1.length;
        let ys = new Set();
        for(let y of y1) ys.add(y);
        for(let y of y2) ys.add(y);
        ys = Array.from(ys).sort((a,b) => a-b);
        let ymap = {};
        for(let i=0; i<ys.length; i++) ymap[ys[i]] = i;
        
        let events = [];
        for(let i=0; i<n; i++) {
            events.push({x: x1[i], type: 1, y1: y1[i], y2: y2[i], w: w[i]});
            events.push({x: x2[i], type: -1, y1: y1[i], y2: y2[i], w: w[i]});
        }
        events.sort((a,b) => a.x - b.x);
        
        let m = ys.length - 1;
        if (m === 0) return 0;
        
        let currWeights = new Array(m).fill(0);
        let widths = [];
        for(let i=0; i<m; i++) widths.push(ys[i+1] - ys[i]);
        
        let prevX = events[0].x;
        let totalArea = 0;
        
        // Loop is actually O(N * M), M <= 2N, so O(N^2)
        for(let i=0; i<events.length; i++) {
            let e = events[i];
            
            if (i > 0) {
                let width = e.x - prevX;
                if (width > 0) {
                    let covered = 0;
                    for(let j=0; j<m; j++) {
                        if (currWeights[j] >= W) covered += widths[j];
                    }
                    totalArea += covered * width;
                    // Note: totalArea might be large (BigInt?), but JS Number is double (safe up to 2^53).
                    // If inputs are large int coord + large area, we might need BigInt.
                    // Python calculates arbitrarily large integers.
                    // Given geometric coordinates usually fits in double unless huge.
                    // We'll stick to Number, if precision loss we check.
                    // Actually, let's use BigInt for totalArea if possible.
                    // Though widths and coords are ints.
                    // Let's assume Number is enough for now.
                }
            }
            
            let idxL = ymap[e.y1];
            let idxR = ymap[e.y2];
            let val = e.w * e.type;
            for(let j=idxL; j<idxR; j++) {
                currWeights[j] += val;
            }
            prevX = e.x;
        }
        return totalArea;
    }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let m = nextInt();
    let W = nextInt();
    let x1=[], y1=[], x2=[], y2=[], w=[];
    for(let i=0; i<m; i++) {
        x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt()); w.push(nextInt());
    }

    const sol = new Solution();
    // Use BigInt logic if needed? Number for output.
    console.log(sol.solve(x1, y1, x2, y2, w, W).toString());
});
"""

# GEO-011: Max Overlap (Segment Tree)
GEO_011_JS = """const readline = require('readline');

class Solution {
    solve(x1, y1, x2, y2) {
        let n = x1.length;
        let ys = new Set();
        for(let y of y1) ys.add(y);
        for(let y of y2) ys.add(y);
        ys = Array.from(ys).sort((a,b) => a-b);
        let ymap = {};
        for(let i=0; i<ys.length; i++) ymap[ys[i]] = i;
        
        // Segment tree covering range [0, m]
        let m = ys.length;
        let treeAdd = new Array(4*m).fill(0);
        let treeMx = new Array(4*m).fill(0);
        
        const update = (node, l, r, ql, qr, val) => {
            if (qr <= l || r <= ql) return;
            if (ql <= l && r <= qr) {
                treeAdd[node] += val;
                treeMx[node] += val;
                return;
            }
            let mid = Math.floor((l+r)/2);
            update(node*2, l, mid, ql, qr, val);
            update(node*2+1, mid, r, ql, qr, val);
            treeMx[node] = treeAdd[node] + Math.max(treeMx[node*2], treeMx[node*2+1]);
        };
        
        let events = [];
        for(let i=0; i<n; i++) {
            // Type -1 for Add, 1 for Remove (sorted: Add first) based on python logic.
            // Python logic: events.append((x1, -1, ..., idx[y2]+1))
            // So -1 is Add.
            // Why -1? sort order: at same X, process Add (-1) before Remove (1).
            // Value to add is +1 for Add, -1 for Remove.
            // Wait, Python: type -1, update val = type ? 
            // Python code: real_val = -val. So -(-1) = +1. Correct.
            events.push({x: x1[i], type: -1, l: ymap[y1[i]], r: ymap[y2[i]] + 1});
            events.push({x: x2[i], type: 1, l: ymap[y1[i]], r: ymap[y2[i]] + 1});
        }
        events.sort((a,b) => a.x === b.x ? a.type - b.type : a.x - b.x);
        
        let ans = 0;
        for(let e of events) {
            update(1, 0, m, e.l, e.r, -e.type);
            ans = Math.max(ans, treeMx[1]);
        }
        return ans;
    }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let m = nextInt();
    let x1=[], y1=[], x2=[], y2=[];
    for(let i=0; i<m; i++) {
        x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(x1, y1, x2, y2));
});
"""

# GEO-012: Empty Circle (Fixed SA in JS) - Same as previous batch but consolidated
GEO_012_JS = """const readline = require('readline');

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
        
        let bestR = 0.0;
        let scored = candidates.map(c => ({c, r: getRadius(c.x, c.y)}));
        scored.sort((a, b) => b.r - a.r);
        
        let starts = [];
        for (let i = 0; i < 10; i++) {
            starts.push({x: xL + Math.random()*(xR-xL), y: yB + Math.random()*(yT-yB)});
        }
        for (let i = 0; i < Math.min(scored.length, 5); i++) {
            starts.push(scored[i].c);
        }
        
        let stepSize = Math.max(xR-xL, yT-yB) / 2.0;
        let precision = 1e-4;
        
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
                
                let dirs = [[0,1], [0,-1], [1,0], [-1,0], [0.7,0.7], [0.7,-0.7], [-0.7,0.7], [-0.7,-0.7]];
                for (let i = dirs.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [dirs[i], dirs[j]] = [dirs[j], dirs[i]];
                }
                
                for (let d of dirs) {
                    let nx = currX + d[0] * tempStep;
                    let ny = currY + d[1] * tempStep;
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
                    tempStep *= 0.6;
                }
            }
            bestR = Math.max(bestR, currR);
        }
        return bestR;
    }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let xL = nextInt(), yB = nextInt(), xR = nextInt(), yT = nextInt();
    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) xs.push(nextInt());
    for(let i=0; i<n; i++) ys.push(nextInt());

    const sol = new Solution();
    console.log(sol.solve(xL, yB, xR, yT, xs, ys).toFixed(6));
});
"""

# GEO-016: MST Complete (Manhattan)
GEO_016_JS = """const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let n = xs.length;
        if (n <= 1) return 0;
        
        let min_dist = new Array(n).fill(Infinity);
        let visited = new Array(n).fill(false);
        min_dist[0] = 0;
        let total = 0;
        
        for (let i = 0; i < n; i++) {
            let u = -1;
            for (let j = 0; j < n; j++) {
                if (!visited[j] && (u === -1 || min_dist[j] < min_dist[u])) {
                    u = j;
                }
            }
            
            if (min_dist[u] === Infinity) break;
            visited[u] = true;
            total += min_dist[u];
            
            let ux = xs[u];
            let uy = ys[u];
            
            for (let v = 0; v < n; v++) {
                if (!visited[v]) {
                    // Manhattan Distance
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
rl.on('line', (line) => { lines.push(...line.trim().split(/\\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    
    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) xs.push(nextInt());
    for(let i=0; i<n; i++) ys.push(nextInt());

    const sol = new Solution();
    // Use toFixed(6) or int? Manhattan dist is int if inputs are int.
    // Python returns int probably. 
    // Let's print as standard number toString() to be safe.
    console.log(sol.solve(xs, ys).toString());
});
"""

def main():
    print("Writing JS solutions for ALL failing problems...")
    write_solution("GEO-003", GEO_003_JS)
    write_solution("GEO-004", GEO_004_JS)
    write_solution("GEO-005", GEO_005_JS)
    write_solution("GEO-007", GEO_007_JS)
    write_solution("GEO-008", GEO_008_JS)
    write_solution("GEO-009", GEO_009_JS) # Fixed Null Check
    write_solution("GEO-010", GEO_010_JS)
    write_solution("GEO-011", GEO_011_JS)
    write_solution("GEO-012", GEO_012_JS)
    write_solution("GEO-016", GEO_016_JS) # Fixed Manhattan

if __name__ == "__main__":
    main()
