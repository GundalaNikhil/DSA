const readline = require('readline');

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
    let x1=[], y1=[], x2=[], y2=[];
    for(let i=0; i<m; i++) {
        x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(x1, y1, x2, y2));
});
