const readline = require("readline");

function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function latticePoints(x1, y1, x2, y2) {
  const dx = Math.abs(x1 - x2);
  const dy = Math.abs(y1 - y2);
  return gcd(dx, dy) + 1;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const x1 = parseInt(data[0], 10);
  const y1 = parseInt(data[1], 10);
  const x2 = parseInt(data[2], 10);
  const y2 = parseInt(data[3], 10);
  console.log(latticePoints(x1, y1, x2, y2));
});
