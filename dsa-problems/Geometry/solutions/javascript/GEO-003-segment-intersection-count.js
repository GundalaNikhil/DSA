function orient(ax, ay, bx, by, cx, cy) {
  const v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
  return v === 0 ? 0 : v > 0 ? 1 : -1;
}

function onSeg(ax, ay, bx, by, cx, cy) {
  return orient(ax, ay, bx, by, cx, cy) === 0 &&
    Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
    Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
}

function inter(a, b) {
  const [ax, ay, bx, by] = a;
  const [cx, cy, dx, dy] = b;
  const o1 = orient(ax, ay, bx, by, cx, cy);
  const o2 = orient(ax, ay, bx, by, dx, dy);
  const o3 = orient(cx, cy, dx, dy, ax, ay);
  const o4 = orient(cx, cy, dx, dy, bx, by);
  if (o1 === 0 && onSeg(ax, ay, bx, by, cx, cy)) return true;
  if (o2 === 0 && onSeg(ax, ay, bx, by, dx, dy)) return true;
  if (o3 === 0 && onSeg(cx, cy, dx, dy, ax, ay)) return true;
  if (o4 === 0 && onSeg(cx, cy, dx, dy, bx, by)) return true;
  return o1 * o2 < 0 && o3 * o4 < 0;
}

function countIntersections(x1, y1, x2, y2) {
  const m = x1.length;
  const segs = [];
  const events = [];
  for (let i = 0; i < m; i++) {
    let ax = x1[i], ay = y1[i], bx = x2[i], by = y2[i];
    if (ax > bx || (ax === bx && ay > by)) [ax, ay, bx, by] = [bx, by, ax, ay];
    segs.push([ax, ay, bx, by]);
    events.push([ax, 0, ay, i]);
    events.push([bx, 1, by, i]);
  }
  events.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[3] - b[3]);

  const yAt = (s, x) => {
    const [ax, ay, bx, by] = s;
    if (ax === bx) return Math.min(ay, by);
    return ay + (by - ay) * (x - ax) / (bx - ax);
  };

  let ans = 0;
  const status = [];
  for (const [x, typ, y, id] of events) {
    if (typ === 0) {
      const ycur = yAt(segs[id], x);
      let pos = status.findIndex(pair => yAt(segs[pair[1]], x) > ycur || (yAt(segs[pair[1]], x) === ycur && pair[1] > id));
      if (pos === -1) pos = status.length;
      if (pos > 0 && inter(segs[id], segs[status[pos-1][1]])) ans++;
      if (pos < status.length && inter(segs[id], segs[status[pos][1]])) ans++;
      status.splice(pos, 0, [ycur, id]);
    } else {
      const ycur = yAt(segs[id], x);
      const pos = status.findIndex(pair => pair[1] === id);
      if (pos !== -1) {
        const left = pos > 0 ? status[pos-1][1] : null;
        const right = pos+1 < status.length ? status[pos+1][1] : null;
        if (left !== null && right !== null && inter(segs[left], segs[right])) ans++;
        status.splice(pos, 1);
      }
    }
  }
  return ans;
}
