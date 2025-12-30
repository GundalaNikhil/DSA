const readline = require("readline");

function lshCandidateProb(b, r, s) {
  const probBandMatch = Math.pow(s, r);
  const probAllBandsMismatch = Math.pow(1.0 - probBandMatch, b);
  return 1.0 - probAllBandsMismatch;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const b = parseInt(data[0], 10);
  const r = parseInt(data[1], 10);
  const s = parseFloat(data[2]);
  console.log(lshCandidateProb(b, r, s).toFixed(6));
});
