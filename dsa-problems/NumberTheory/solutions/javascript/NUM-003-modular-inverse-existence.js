const readline = require("readline");

function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function hasInverse(a, m) {
  return gcd(a, m) === 1;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const q = parseInt(data[idx++], 10);
  const out = [];
  for (let i = 0; i < q; i++) {
    const a = parseInt(data[idx++], 10);
    const m = parseInt(data[idx++], 10);
    out.push(hasInverse(a, m) ? "true" : "false");
  }
  console.log(out.join("\n"));
});
