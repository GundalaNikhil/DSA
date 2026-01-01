const fs = require('fs');

function orient(ax, ay, bx, by, cx, cy) {
    let v = (BigInt(bx) - BigInt(ax)) * (BigInt(cy) - BigInt(ay)) - (BigInt(by) - BigInt(ay)) * (BigInt(cx) - BigInt(ax));
    if (v === 0n) return 0;
    return v > 0n ? 1 : -1;
}

function onSeg(ax, ay, bx, by, cx, cy) {
    return Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
           Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
}

function intersects(s1, s2) {
    let o1 = orient(s1[0], s1[1], s1[2], s1[3], s2[0], s2[1]);
    let o2 = orient(s1[0], s1[1], s1[2], s1[3], s2[2], s2[3]);
    let o3 = orient(s2[0], s2[1], s2[2], s2[3], s1[0], s1[1]);
    let o4 = orient(s2[0], s2[1], s2[2], s2[3], s1[2], s1[3]);

    if (((o1 > 0 && o2 < 0) || (o1 < 0 && o2 > 0)) &&
        ((o3 > 0 && o4 < 0) || (o3 < 0 && o4 > 0))) return true;

    if (o1 === 0 && onSeg(s1[0], s1[1], s1[2], s1[3], s2[0], s2[1])) return true;
    if (o2 === 0 && onSeg(s1[0], s1[1], s1[2], s1[3], s2[2], s2[3])) return true;
    if (o3 === 0 && onSeg(s2[0], s2[1], s2[2], s2[3], s1[0], s1[1])) return true;
    if (o4 === 0 && onSeg(s2[0], s2[1], s2[2], s2[3], s1[2], s1[3])) return true;

    return false;
}

function solve() {
    const input = fs.readFileSync(0, 'utf8').split(/\s+/);
    let ptr = 0;
    const n = parseInt(input[ptr++]);
    if (isNaN(n)) return;

    let segs = [];
    for (let i = 0; i < n; i++) {
        segs.push([parseInt(input[ptr++]), parseInt(input[ptr++]), parseInt(input[ptr++]), parseInt(input[ptr++])]);
    }

    let count = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (intersects(segs[i], segs[j])) count++;
        }
    }
    process.stdout.write(count.toString() + "\n");
}

solve();
