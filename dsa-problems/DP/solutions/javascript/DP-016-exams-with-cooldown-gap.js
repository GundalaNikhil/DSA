function maxScore(exams, g) {
  exams.sort((a, b) => a[1] - b[1]);
  const ends = exams.map((e) => e[1]);
  const n = exams.length;
  const dp = Array(n + 1).fill(0n);
  for (let i = 1; i <= n; i++) {
    const [s, e, w] = exams[i - 1];
    let l = 0,
      r = ends.length;
    const target = s - g;
    while (l < r) {
      const m = (l + r) >> 1;
      if (ends[m] <= target) l = m + 1;
      else r = m;
    }
    const take = dp[l] + BigInt(w);
    const skip = dp[i - 1];
    dp[i] = take > skip ? take : skip;
  }
  return Number(dp[n]);
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

  let ptr = 0;
  const parts = data[ptr++].split(/\s+/).map(Number);
  const n = parts[0];
  const g = parts[1];
  const exams = [];
  for (let i = 0; i < n; i++) {
    const exam = data[ptr++].split(/\s+/).map(Number);
    exams.push(exam);
  }

  console.log(maxScore(exams, g));
});
