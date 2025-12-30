const readline = require("readline");

function buildPrefixDistinct(N) {
  const f = new Int32Array(N + 1);
  
  for (let i = 2; i <= N; i++) {
    if (f[i] === 0) { // i is prime
      for (let j = i; j <= N; j += i) {
        f[j]++;
      }
    }
  }
  
  // Use BigInt for prefix sums to be safe, though N*logN fits in 53 bits
  // Max sum approx 10^6 * 7 approx 7*10^6. Fits in standard number.
  const pref = new Float64Array(N + 1);
  for (let i = 1; i <= N; i++) {
    pref[i] = pref[i - 1] + f[i];
  }
  
  return pref;
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
  const N = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  
  const pref = buildPrefixDistinct(N);
  const out = [];
  
  for (let i = 0; i < q; i++) {
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    out.push((pref[r] - pref[l - 1]).toString());
  }
  console.log(out.join("\n"));
});
