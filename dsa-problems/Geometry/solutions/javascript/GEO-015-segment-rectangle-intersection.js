const readline = require("readline");

class Solution {
  intersects(xL, yB, xR, yT, x1, y1, x2, y2) {
    xL = BigInt(xL); yB = BigInt(yB); xR = BigInt(xR); yT = BigInt(yT);
    x1 = BigInt(x1); y1 = BigInt(y1); x2 = BigInt(x2); y2 = BigInt(y2);

    const orient = (ax, ay, bx, by, cx, cy) => {
      const v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
      if (v > 0n) return 1;
      if (v < 0n) return -1;
      return 0;
    };

    const onSeg = (ax, ay, bx, by, cx, cy) => {
      return orient(ax, ay, bx, by, cx, cy) === 0 &&
             (ax < bx ? ax : bx) <= cx && cx <= (ax > bx ? ax : bx) &&
             (ay < by ? ay : by) <= cy && cy <= (ay > by ? ay : by);
    };

    const segInter = (ax, ay, bx, by, cx, cy, dx, dy) => {
      const o1 = orient(ax, ay, bx, by, cx, cy);
      const o2 = orient(ax, ay, bx, by, dx, dy);
      const o3 = orient(cx, cy, dx, dy, ax, ay);
      const o4 = orient(cx, cy, dx, dy, bx, by);

      if (o1 === 0 && onSeg(ax, ay, bx, by, cx, cy)) return true;
      if (o2 === 0 && onSeg(ax, ay, bx, by, dx, dy)) return true;
      if (o3 === 0 && onSeg(cx, cy, dx, dy, ax, ay)) return true;
      if (o4 === 0 && onSeg(cx, cy, dx, dy, bx, by)) return true;

      return o1 !== o2 && o3 !== o4;
    };

    const inside1 = (xL <= x1 && x1 <= xR && yB <= y1 && y1 <= yT);
    const inside2 = (xL <= x2 && x2 <= xR && yB <= y2 && y2 <= yT);
    if (inside1 || inside2) return true;

    const edges = [
      [xL, yB, xR, yB],
      [xR, yB, xR, yT],
      [xR, yT, xL, yT],
      [xL, yT, xL, yB]
    ];

    for (const e of edges) {
      if (segInter(x1, y1, x2, y2, e[0], e[1], e[2], e[3])) return true;
    }

    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const xL = data[ptr++];
  const yB = data[ptr++];
  const xR = data[ptr++];
  const yT = data[ptr++];
  const x1 = data[ptr++];
  const y1 = data[ptr++];
  const x2 = data[ptr++];
  const y2 = data[ptr++];
  
  const solution = new Solution();
  console.log(solution.intersects(xL, yB, xR, yT, x1, y1, x2, y2));
});
