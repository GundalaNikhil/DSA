const readline = require('readline');

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
    let W = nextInt();
    let x1=[], y1=[], x2=[], y2=[], w=[];
    for(let i=0; i<m; i++) {
        x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt()); w.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(x1, y1, x2, y2, w, W).toString());
});
