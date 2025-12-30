const readline = require("readline");

class Solution {
  maxProfitWithConstraints(prices, dMin, dMax, C) {
    const n = prices.length;
    // Using a simple array as deque for JS (perf ok for typical N, else use library or linked list)
    // We maintain indices
    const dq = [];
    let head = 0; // Pointer to front of deque to simulate shift() in O(1) mostly
    let maxProfit = 0;

    for (let j = dMin; j < n; j++) {
      const buyCandidate = j - dMin;

      // Maintain Monotonic: pop back while larger
      while (
        dq.length > head &&
        prices[dq[dq.length - 1]] >= prices[buyCandidate]
      ) {
        dq.pop();
      }
      dq.push(buyCandidate);

      // Remove expired from front
      // Valid range start: j - dMax
      if (dq.length > head && dq[head] < j - dMax) {
        head++;
      }

      // Calculate
      if (dq.length > head) {
        const minBuyPrice = prices[dq[head]];
        const sellPrice = Math.min(prices[j], C);
        maxProfit = Math.max(maxProfit, sellPrice - minBuyPrice);
      }
    }

    return maxProfit;
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
  const prices = [];
  for (let i = 0; i < n; i++) prices.push(Number(tokens[ptr++]));

  const dMin = Number(tokens[ptr++]);
  const dMax = Number(tokens[ptr++]);
  const C = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.maxProfitWithConstraints(prices, dMin, dMax, C));
});
