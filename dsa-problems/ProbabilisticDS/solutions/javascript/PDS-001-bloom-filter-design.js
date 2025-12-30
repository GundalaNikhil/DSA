const readline = require("readline");

function designBloom(n, f) {
  const ln2 = Math.log(2);
  
  const mDouble = -(n * Math.log(f)) / (ln2 * ln2);
  const m = Math.ceil(mDouble);
  
  const kDouble = (m / n) * ln2;
  const k = Math.round(kDouble);
  
  const exponent = -(k * n) / m;
  const fpr = Math.pow(1 - Math.exp(exponent), k);
  
  return [m, k, fpr];
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
  const f = parseFloat(data[1]);
  const res = designBloom(n, f);
  console.log(res[0] + " " + res[1] + " " + res[2].toFixed(6));
});
