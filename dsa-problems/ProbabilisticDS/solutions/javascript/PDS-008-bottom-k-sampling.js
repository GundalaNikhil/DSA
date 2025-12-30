const readline = require("readline");

function jaccardEstimate(a, b) {
  let matches = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i] === b[i]) {
      matches++;
    }
  }
  return matches / a.length;
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
  const a = [];
  const b = [];
  for (let i = 0; i < k; i++) a.push(parseFloat(data[idx++]));
  for (let i = 0; i < k; i++) b.push(parseFloat(data[idx++]));
  console.log(jaccardEstimate(a, b).toFixed(6));
});
