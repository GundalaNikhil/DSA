const readline = require("readline");

function kmvEstimate(hashes) {
  const k = hashes.length;
  if (k === 0) return 0.0;
  const hk = hashes[k-1];
  return (k - 1) / hk;
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
  const k = parseInt(data[idx++], 10);
  const hashes = [];
  for (let i = 0; i < k; i++) hashes.push(parseFloat(data[idx++]));
  console.log(kmvEstimate(hashes).toFixed(6));
});
