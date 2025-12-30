class Solution {
  process(arr, mod, ops) {
    const n = arr.length;
    const bit = new Array(n + 1).fill(0n);
    const bigMod = BigInt(mod);

    const add = (idx, val) => {
      idx++; // 1-based
      while (idx <= n) {
        bit[idx] = (bit[idx] + val) % bigMod;
        if (bit[idx] < 0n) bit[idx] += bigMod;
        idx += idx & -idx;
      }
    };

    const query = (idx) => {
      idx++;
      let sum = 0n;
      while (idx > 0) {
        sum = (sum + bit[idx]) % bigMod;
        idx -= idx & -idx;
      }
      return sum;
    };

    // Build BIT
    for (let i = 0; i < n; i++) {
      add(i, BigInt(arr[i]));
    }

    const currentArr = arr.map(BigInt);
    const history = []; // Stack
    const results = [];

    for (const op of ops) {
      const type = op[0];
      if (type === "UPDATE") {
        const idx = parseInt(op[1], 10);
        const val = BigInt(op[2]);

        const oldVal = currentArr[idx];
        history.push({ idx, oldVal });

        let diff = (val - oldVal) % bigMod;
        if (diff < 0n) diff += bigMod;

        add(idx, diff);
        currentArr[idx] = val;

      } else if (type === "QUERY") {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);

        let res = (query(r) - query(l - 1)) % bigMod;
        if (res < 0n) res += bigMod;
        results.push(Number(res)); // Convert back to number for output

      } else if (type === "UNDO") {
        let k = parseInt(op[1], 10);
        while (k > 0 && history.length > 0) {
          const { idx, oldVal } = history.pop();
          const currentVal = currentArr[idx];

          let diff = (oldVal - currentVal) % bigMod;
          if (diff < 0n) diff += bigMod;

          add(idx, diff);
          currentArr[idx] = oldVal;
          k--;
        }
      }
    }
    return results;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const mod = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "UNDO") {
      ops.push([type, data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, mod, ops);
  console.log(out.join("\n"));
});
