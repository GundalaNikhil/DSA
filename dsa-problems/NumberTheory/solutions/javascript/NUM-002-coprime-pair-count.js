const readline = require("readline");

function countCoprimePairs(N) {
  if (N < 2) return 0;
  
  const phi = new Int32Array(N + 1);
  for (let i = 0; i <= N; i++) phi[i] = i;
  
  for (let i = 2; i <= N; i++) {
    if (phi[i] === i) { // i is prime
      for (let j = i; j <= N; j += i) {
        phi[j] -= Math.floor(phi[j] / i);
      }
    }
  }
  
  let total = 0n; // Use BigInt for safety, though N=10^5 fits in number
  for (let i = 2; i <= N; i++) {
    total += BigInt(phi[i]);
  }
  
  return total.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  console.log(countCoprimePairs(N));
});
