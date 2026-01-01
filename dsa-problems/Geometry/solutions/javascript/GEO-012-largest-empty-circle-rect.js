const fs = require('fs');

function getRadius(x, y, xL, yB, xR, yT, n, xs, ys, rs) {
    let r = Math.min(x - xL, xR - x, y - yB, yT - y);
    if (r <= 0) return 0;
    for (let i = 0; i < n; i++) {
        let d = Math.sqrt((x - xs[i])**2 + (y - ys[i])**2);
        r = Math.min(r, d - rs[i]);
        if (r <= 0) return 0;
    }
    return r;
}

function solve() {
    const data = fs.readFileSync(0, 'utf8').split(/\s+/);
    let idx = 0;
    const xL = parseInt(data[idx++]), yB = parseInt(data[idx++]), xR = parseInt(data[idx++]), yT = parseInt(data[idx++]);
    const n = parseInt(data[idx++]);
    if (isNaN(xL)) return;
    
    const xs = [], ys = [], rs = [];
    for (let i = 0; i < n; i++) {
        xs.push(parseInt(data[idx++]));
        ys.push(parseInt(data[idx++]));
        rs.push(parseInt(data[idx++]));
    }
    
    let candidates = [];
    const gridRes = 120;
    for (let i = 0; i <= gridRes; i++) {
        const cx = xL + (xR - xL) * (i / gridRes);
        for (let j = 0; j <= gridRes; j++) {
            const cy = yB + (yT - yB) * (j / gridRes);
            const r = getRadius(cx, cy, xL, yB, xR, yT, n, xs, ys, rs);
            if (r > 0) candidates.push({ x: cx, y: cy, r });
        }
    }
    
    for (let i = 0; i < n; i++) {
        candidates.push({ x: xs[i], y: yB, r: getRadius(xs[i], yB, xL, yB, xR, yT, n, xs, ys, rs) });
        candidates.push({ x: xs[i], y: yT, r: getRadius(xs[i], yT, xL, yB, xR, yT, n, xs, ys, rs) });
        candidates.push({ x: xL, y: ys[i], r: getRadius(xL, ys[i], xL, yB, xR, yT, n, xs, ys, rs) });
        candidates.push({ x: xR, y: ys[i], r: getRadius(xR, ys[i], xL, yB, xR, yT, n, xs, ys, rs) });
        for (let j = i + 1; j < n; j++) {
            const mx = (xs[i] + xs[j]) / 2, my = (ys[i] + ys[j]) / 2;
            candidates.push({ x: mx, y: my, r: getRadius(mx, my, xL, yB, xR, yT, n, xs, ys, rs) });
        }
    }
    
    let bestR = 0;
    if (candidates.length === 0) {
        bestR = Math.max(bestR, getRadius((xL + xR) / 2, (yB + yT) / 2, xL, yB, xR, yT, n, xs, ys, rs));
    } else {
        candidates.sort((a, b) => b.r - a.r);
        let count = 0;
        const seen = new Set();
        for (let cand of candidates) {
            if (count >= 60) break;
            const key = `${Math.round(cand.x * 10)}_${Math.round(cand.y * 10)}`;
            if (seen.has(key)) continue;
            seen.add(key);
            count++;
            
            let currX = cand.x, currY = cand.y, currR = cand.r;
            let step = Math.max(xR - xL, yT - yB) / gridRes;
            while (step > 1e-13) {
                let improved = false;
                const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [0.7, 0.7], [0.7, -0.7], [-0.7, 0.7], [-0.7, -0.7], [0.3, 0.9], [0.9, 0.3]];
                for (let [dx, dy] of dirs) {
                    const nx = currX + dx * step, ny = currY + dy * step;
                    if (nx >= xL && nx <= xR && ny >= yB && ny <= yT) {
                        const nr = getRadius(nx, ny, xL, yB, xR, yT, n, xs, ys, rs);
                        if (nr > currR) {
                            currR = nr; currX = nx; currY = ny;
                            improved = true;
                        }
                    }
                }
                if (!improved) step *= 0.5;
            }
            bestR = Math.max(bestR, currR);
        }
    }
    process.stdout.write(Math.max(0, bestR).toFixed(6) + "\n");
}

solve();
