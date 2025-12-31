const readline = require("readline");

function totalSize(sizes) {
  let S = 0;
  for (const s of sizes) {
    S += s * s;
  }
  return S;
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
  const t = parseInt(data[idx++], 10);
  const sizes = [];
  for (let i = 0; i < t; i++) sizes.push(parseInt(data[idx++], 10));
  const S = totalSize(sizes);
  console.log(S + " " + (S <= 4 * n ? "YES" : "NO"));
});
