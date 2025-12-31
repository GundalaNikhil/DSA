const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null];
    this.count = 0;
  }
}

class Solution {
  insert(root, num) {
    let curr = root;
    for (let i = 29; i >= 0; i--) {
      const bit = (num >> i) & 1;
      if (!curr.children[bit]) {
        curr.children[bit] = new TrieNode();
      }
      curr = curr.children[bit];
      curr.count++;
    }
  }

  countLessEqual(root, num, K) {
    if (K < 0) return 0;
    let curr = root;
    let count = 0;
    for (let i = 29; i >= 0; i--) {
      if (!curr) break;
      const bitNum = (num >> i) & 1;
      const bitK = (K >> i) & 1;

      if (bitK === 1) {
        if (curr.children[bitNum]) {
          count += curr.children[bitNum].count;
        }
        curr = curr.children[1 - bitNum];
      } else {
        curr = curr.children[bitNum];
      }
    }
    if (curr) count += curr.count;
    return count;
  }

  solve(nums, L, U) {
    const root = new TrieNode();
    let total = 0;
    const limitL = L - 1;

    for (const x of nums) {
      const cU = this.countLessEqual(root, x, U);
      const cL = this.countLessEqual(root, x, limitL);
      total += cU - cL;
      this.insert(root, x);
    }
    return total;
  }

  countPairwiseXorBandParity(a, L, U) {
    const evens = [];
    const odds = [];
    for (let i = 0; i < a.length; i++) {
      if (i % 2 === 0) evens.push(a[i]);
      else odds.push(a[i]);
    }
    return BigInt(this.solve(evens, L, U) + this.solve(odds, L, U));
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
  const L = Number(tokens[ptr++]);
  const U = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.countPairwiseXorBandParity(a, L, U).toString());
});
