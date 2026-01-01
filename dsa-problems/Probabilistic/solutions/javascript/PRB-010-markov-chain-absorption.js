const readline = require("readline");

function invert(A) {
  const n = A.length;
  const B = Array(n).fill(0).map(() => Array(2 * n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) B[i][j] = A[i][j];
    B[i][n + i] = 1;
  }
  for (let i = 0; i < n; i++) {
    let pivot = i;
    for (let j = i + 1; j < n; j++) {
      if (Math.abs(B[j][i]) > Math.abs(B[pivot][i])) pivot = j;
    }
    const temp = B[i]; B[i] = B[pivot]; B[pivot] = temp;
    const div = B[i][i];
    for (let j = i; j < 2 * n; j++) B[i][j] /= div;
    for (let k = 0; k < n; k++) {
      if (k !== i) {
        const factor = B[k][i];
        for (let j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
      }
    }
  }
  const res = Array(n).fill(0).map(() => Array(n).fill(0));
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
    const probs = absorbing.map(idx => (idx === s ? 1.0 : 0.0));
    return { expectedSteps: 0.0, probs };
  }

  const tSize = transient.length;
  const aSize = absorbing.length;
  const Q = Array(tSize).fill(0).map(() => Array(tSize).fill(0));
  const R = Array(tSize).fill(0).map(() => Array(aSize).fill(0));

  for (let i = 0; i < tSize; i++) {
    const u = transient[i];
    for (let j = 0; j < tSize; j++) Q[i][j] = P[u][transient[j]];
    for (let j = 0; j < aSize; j++) R[i][j] = P[u][absorbing[j]];
  }

  const I_minus_Q = Array(tSize).fill(0).map((_, i) =>
    Array(tSize).fill(0).map((_, j) => (i === j ? 1.0 : 0.0) - Q[i][j])
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
  return { expectedSteps, probs };
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const P = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) row.push(parseFloat(data[idx++]));
    P.push(row);
  }

  const numQueries = parseInt(data[idx++], 10);
  const queryStates = [];
  for (let i = 0; i < numQueries; i++) queryStates.push(parseInt(data[idx++], 10));

  const numAbsorbing = parseInt(data[idx++], 10);
  const absorbingIndices = [];
  for (let i = 0; i < numAbsorbing; i++) absorbingIndices.push(parseInt(data[idx++], 10));

  const funcAbsorbing = [];
  for (let i = 0; i < n; i++) {
    if (Math.abs(P[i][i] - 1.0) < 1e-9) funcAbsorbing.push(i);
  }

  const finalProbs = [];
  const finalSteps = [];

  for (const s of queryStates) {
    const res = absorptionStats(P, s);
    finalSteps.push(res.expectedSteps.toFixed(6));
    
    for (const aIdx of absorbingIndices) {
      const pos = funcAbsorbing.indexOf(aIdx);
      if (pos !== -1) {
        finalProbs.push(res.probs[pos].toFixed(6));
      }
    }
  }

  console.log(finalProbs.join(" "));
  console.log(finalSteps.join(" "));
});
