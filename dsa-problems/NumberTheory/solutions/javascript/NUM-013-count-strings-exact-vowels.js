const readline = require("readline");

const MOD = 1000000007n;

function power(base, exp) {
  let res = 1n;
  base %= MOD;
  while (exp > 0n) {
    if (exp % 2n === 1n) res = (res * base) % MOD;
    base = (base * base) % MOD;
    exp /= 2n;
  }
  return res;
}

function modInverse(n) {
  return power(n, MOD - 2n);
}

function countStrings(n, k) {
  if (k < 0 || k > n) return 0;
  
  const N = BigInt(n);
  const K = BigInt(k);
  
  // Compute factorial directly if n is small, or use array
  // Given n <= 10^6, array is needed.
  // But JS memory limit might be tight for 10^6 BigInts?
  // Let's optimize: we only need fact[n], invFact[k], invFact[n-k].
  // We can compute fact[n] in O(n), then invFact.
  
  // We can just compute these three values.
  
  let factN = 1n;
  let factK = 1n;
  let factNK = 1n;
  
  for (let i = 1n; i <= N; i++) {
    factN = (factN * i) % MOD;
    if (i === K) factK = factN;
    if (i === (N - K)) factNK = factN;
  }
  
  // Handle 0! = 1
  if (K === 0n) factK = 1n;
  if (N - K === 0n) factNK = 1n;
  
  const invFactK = modInverse(factK);
  const invFactNK = modInverse(factNK);
  
  const nCr = factN * invFactK % MOD * invFactNK % MOD;
  const vowels = power(5n, K);
  const consonants = power(21n, N - K);
  
  return (nCr * vowels % MOD * consonants % MOD).toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  console.log(countStrings(n, k));
});
