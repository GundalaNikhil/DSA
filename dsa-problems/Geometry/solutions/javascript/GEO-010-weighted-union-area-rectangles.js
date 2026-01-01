const fs = require('fs');

function solve() {
    const input = fs.readFileSync(0, 'utf8').split(/\s+/);
    let ptr = 0;
    const n = parseInt(input[ptr++]);
    const targetW = parseInt(input[ptr++]);
    if (isNaN(n)) return;

    let rects = [];
    let xSet = new Set(), ySet = new Set();
    for (let i = 0; i < n; i++) {
        let x1 = parseInt(input[ptr++]);
        let y1 = parseInt(input[ptr++]);
        let x2 = parseInt(input[ptr++]);
        let y2 = parseInt(input[ptr++]);
        let w = parseInt(input[ptr++]);
        rects.push({ x1, y1, x2, y2, w });
        xSet.add(x1); xSet.add(x2);
        ySet.add(y1); ySet.add(y2);
    }

    let ux = Array.from(xSet).sort((a, b) => a - b);
    let uy = Array.from(ySet).sort((a, b) => a - b);

    let totalArea = BigInt(0);
    for (let i = 0; i < ux.length - 1; i++) {
        let dx = BigInt(ux[i + 1] - ux[i]);
        if (dx <= 0n) continue;

        let yWeights = new BigInt64Array(uy.length - 1);
        for (let r of rects) {
            if (r.x1 <= ux[i] && r.x2 >= ux[i + 1]) {
                for (let j = 0; j < uy.length - 1; j++) {
                    if (r.y1 <= uy[j] && r.y2 >= uy[j + 1]) {
                        yWeights[j] += BigInt(r.w);
                    }
                }
            }
        }

        let dyCovered = 0n;
        for (let j = 0; j < uy.length - 1; j++) {
            if (yWeights[j] >= BigInt(targetW)) {
                dyCovered += BigInt(uy[j + 1] - uy[j]);
            }
        }
        totalArea += dx * dyCovered;
    }

    process.stdout.write(totalArea.toString() + "\n");
}

solve();
