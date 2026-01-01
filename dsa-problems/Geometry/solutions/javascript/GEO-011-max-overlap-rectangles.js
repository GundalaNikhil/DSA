const readline = require('readline');

class Solution {
    solve(x1, y1, x2, y2) {
        let n = x1.length;
        let ys = new Set();
        for(let y of y1) ys.add(y);
        for(let y of y2) ys.add(y);
        ys = Array.from(ys).sort((a,b) => a-b);
        let ymap = {};
        for(let i=0; i<ys.length; i++) ymap[ys[i]] = i;
        
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
