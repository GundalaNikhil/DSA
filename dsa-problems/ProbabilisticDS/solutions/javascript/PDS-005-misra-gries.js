const readline = require("readline");

function misraGries(stream, k) {
  const counts = new Map();
  
  for (const x of stream) {
    if (counts.has(x)) {
      counts.set(x, counts.get(x) + 1);
    } else if (counts.size < k - 1) {
      counts.set(x, 1);
    } else {
      // Decrement all
      const toRemove = [];
      for (const [key, val] of counts) {
        if (val - 1 === 0) {
          toRemove.push(key);
        } else {
          counts.set(key, val - 1);
        }
      }
      for (const key of toRemove) {
        counts.delete(key);
      }
    }
  }
  
  const res = Array.from(counts.keys()).sort((a, b) => a - b);
  return res;
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
  const k = parseInt(data[idx++], 10);
  const stream = [];
  for (let i = 0; i < n; i++) stream.push(parseInt(data[idx++], 10));
  const res = misraGries(stream, k);
  console.log(res.join(" "));
});
