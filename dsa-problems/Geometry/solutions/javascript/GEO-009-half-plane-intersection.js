const readline = require('readline');
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
            if (!p) return true; 
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
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
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
