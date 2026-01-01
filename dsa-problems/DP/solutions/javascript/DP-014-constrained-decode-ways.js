const MOD = 1_000_000_007n;

function decodeWays(s) {
  if (s.length === 0 || s[0] === "0") return 0;
  let prev2 = 1n, prev1 = 1n;
  for (let i = 1; i < s.length; i++) {
    const pair = Number(s[i - 1]) * 10 + Number(s[i]);
    let cur = 0n;
    if (s[i] !== "0") {
      cur = (cur + prev1) % MOD;
      if (pair === 20 || (pair > 10 && pair <= 26)) cur = (cur + prev2) % MOD;
    } else {
      if (pair === 20) cur = (cur + prev2) % MOD;
    }
    prev2 = prev1;
    prev1 = cur;
  }
  return Number(prev1 % MOD);
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  const s = data[0];
  console.log(decodeWays(s));
});
