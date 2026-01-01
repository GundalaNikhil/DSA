const fs = require('fs');

class BIT {
    constructor(n) {
        this.n = n;
        this.minVal = new Float64Array(n + 1).fill(4e18);
        this.id = new Int32Array(n + 1).fill(-1);
    }
    update(i, val, pId) {
        for (; i > 0; i -= i & -i) {
            if (val < this.minVal[i]) {
                this.minVal[i] = val;
                this.id[i] = pId;
            }
        }
    }
    query(i) {
        let resVal = 4e18;
        let resId = -1;
        for (; i <= this.n; i += i & -i) {
            if (this.minVal[i] < resVal) {
                resVal = this.minVal[i];
                resId = this.id[i];
            }
        }
        return resId;
    }
}

class DSU {
    constructor(n) {
        this.parent = new Int32Array(n);
        for (let i = 0; i < n; i++) this.parent[i] = i;
    }
    find(i) {
        if (this.parent[i] === i) return i;
        return this.parent[i] = this.find(this.parent[i]);
    }
    union(i, j) {
        let rootI = this.find(i);
        let rootJ = this.find(j);
        if (rootI !== rootJ) {
            this.parent[rootI] = rootJ;
            return true;
        }
        return false;
    }
}

function solve() {
    const input = fs.readFileSync(0, 'utf8').split(/\s+/);
    let ptr = 0;
    const n = parseInt(input[ptr++]);
    if (isNaN(n)) return;
    if (n <= 1) {
        process.stdout.write("0\n");
        return;
    }

    let pts = [];
    for (let i = 0; i < n; i++) {
        pts.push({ x: parseInt(input[ptr++]), y: parseInt(input[ptr++]), id: i });
    }

    let edges = [];
    for (let s1 = 0; s1 < 2; s1++) {
        for (let s2 = 0; s2 < 2; s2++) {
            for (let sw = 0; sw < 2; sw++) {
                pts.sort((a, b) => a.x !== b.x ? b.x - a.x : b.y - a.y);
                
                let ys = pts.map(p => p.y - p.x);
                let sortedYs = Array.from(new Set(ys)).sort((a, b) => a - b);
                
                let bit = new BIT(sortedYs.length);
                for (let i = 0; i < n; i++) {
                    let pos = sortedYs.indexOf(ys[i]) + 1;
                    let idx = bit.query(pos);
                    if (idx !== -1) {
                        let d = Math.abs(pts[i].x - pts[idx].x) + Math.abs(pts[i].y - pts[idx].y);
                        edges.push({ u: pts[i].id, v: pts[idx].id, w: d });
                    }
                    bit.update(pos, pts[i].x + pts[i].y, i);
                }

                for (let p of pts) { let tmp = p.x; p.x = p.y; p.y = tmp; }
            }
            for (let p of pts) p.y = -p.y;
        }
        for (let p of pts) p.x = -p.x;
    }

    edges.sort((a, b) => a.w - b.w);
    let dsu = new DSU(n);
    let mst = 0;
    let count = 0;
    for (let e of edges) {
        if (dsu.union(e.u, e.v)) {
            mst += e.w;
            if (++count === n - 1) break;
        }
    }
    process.stdout.write(mst.toString() + "\n");
}

solve();
