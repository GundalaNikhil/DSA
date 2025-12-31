const readline = require("readline");

class Solution {
  constructor() {
    this.memo = new Map();
  }

  chompGame(R, C, poisons) {
    this.poisons = poisons;
    const initialState = new Array(C).fill(R);
    return this.canWin(initialState) ? "First" : "Second";
  }

  canWin(state) {
    const key = state.join(",");
    if (this.memo.has(key)) return this.memo.get(key);

    let canReachLosing = false;
    const C = state.length;

    for (let c = 0; c < C; c++) {
      for (let r = 0; r < state[c]; r++) {
        if (this.isValid(r, c)) {
          const nextState = [...state];
          for (let i = c; i < C; i++) {
            nextState[i] = Math.min(nextState[i], r);
          }
          
          if (!this.canWin(nextState)) {
            canReachLosing = true;
            break;
          }
        }
      }
      if (canReachLosing) break;
    }

    this.memo.set(key, canReachLosing);
    return canReachLosing;
  }

  isValid(r, c) {
    for (const [pr, pc] of this.poisons) {
      if (pr >= r && pc >= c) return false;
    }
    return true;
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const R = parseInt(flatData[idx++]);
  const C = parseInt(flatData[idx++]);
  const K = parseInt(flatData[idx++]);
  
  const poisons = [];
  for (let i = 0; i < K; i++) {
      const r = parseInt(flatData[idx++]);
      const c = parseInt(flatData[idx++]);
      poisons.push([r, c]);
  }

  const solution = new Solution();
  console.log(solution.chompGame(R, C, poisons));
});
