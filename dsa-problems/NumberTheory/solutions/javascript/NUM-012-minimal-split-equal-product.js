const readline = require("readline");

function minimalProductSplit(x) {
  const s = x.toString();
  const n = s.length;
  let minProd = -1n;
  
  for (let i = 1; i < n; i++) {
    const part1 = s.substring(0, i);
    const part2 = s.substring(i);
    
    const a = BigInt(part1);
    const b = BigInt(part2);
    
    const prod = a * b;
    if (prod > 0n) {
      if (minProd === -1n || prod < minProd) {
        minProd = prod;
      }
    }
  }
  
  return minProd.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  // Use BigInt for input parsing to handle 10^12 safely in JS (though Number is fine up to 9*10^15)
  // But consistent BigInt usage is better.
  const x = BigInt(data[0]);
  console.log(minimalProductSplit(x));
});
