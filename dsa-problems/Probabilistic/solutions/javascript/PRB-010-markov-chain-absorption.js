const readline = require("readline");

function invert(A) {
  const n = A.length;
  const B = Array(n)
    .fill(0)
    .map(() => Array(2 * n).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) B[i][j] = A[i][j];
    B[i][n + i] = 1;
  }

  for (let i = 0; i < n; i++) {
    let pivot = i;
    for (let j = i + 1; j < n; j++) {
      if (Math.abs(B[j][i]) > Math.abs(B[pivot][i])) pivot = j;
    }
    [B[i], B[pivot]] = [B[pivot], B[i]];

    const div = B[i][i];
    for (let j = i; j < 2 * n; j++) B[i][j] /= div;

    for (let k = 0; k < n; k++) {
      if (k !== i) {
        const factor = B[k][i];
        for (let j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
      }
    }
  }

  const res = Array(n)
    .fill(0)
    .map(() => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) res[i][j] = B[i][n + j];
  }
  return res;
}

function absorptionStats(P, s) {
  const n = P.length;
  const absorbing = [];
  const transient = [];

  for (let i = 0; i < n; i++) {
    if (Math.abs(P[i][i] - 1.0) < 1e-9) absorbing.push(i);
    else transient.push(i);
  }

  if (absorbing.includes(s)) {
    const res = [0.0];
    for (const idx of absorbing) res.push(idx === s ? 1.0 : 0.0);
    return res;
  }

  const tSize = transient.length;
  const aSize = absorbing.length;

  const Q = Array(tSize)
    .fill(0)
    .map(() => Array(tSize).fill(0));
  const R = Array(tSize)
    .fill(0)
    .map(() => Array(aSize).fill(0));

  for (let i = 0; i < tSize; i++) {
    const u = transient[i];
    for (let j = 0; j < tSize; j++) {
      const v = transient[j];
      Q[i][j] = P[u][v];
    }
    for (let j = 0; j < aSize; j++) {
      const v = absorbing[j];
      R[i][j] = P[u][v];
    }
  }

  const I_minus_Q = Array(tSize)
    .fill(0)
    .map((_, i) =>
      Array(tSize)
        .fill(0)
        .map((_, j) => (i === j ? 1.0 : 0.0) - Q[i][j])
    );

  const N = invert(I_minus_Q);

  const sIdx = transient.indexOf(s);

  let expectedSteps = 0;
  for (let j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

  const probs = Array(aSize).fill(0);
  for (let j = 0; j < aSize; j++) {
    for (let k = 0; k < tSize; k++) {
      probs[j] += N[sIdx][k] * R[k][j];
    }
  }

  return [expectedSteps, ...probs];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  let idx = 0;
  const first = lines[idx++].split(/\s+/).map(Number);
  const n = first[0];
  const s = first[1];
  const P = [];
  for (let i = 0; i < n; i++) {
    P.push(lines[idx++].split(/\s+/).map(Number));
  }
  const res = absorptionStats(P, s);
  if (res.length > 0) {
    console.log(res[0].toFixed(6));
    if (res.length > 1) {
      console.log(
        res
          .slice(1)
          .map((x) => x.toFixed(6))
          .join(" ")
      );
    } else {
      console.log("");
    }
  }
});
