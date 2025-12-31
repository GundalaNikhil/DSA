const readline = require("readline");

function getDigitSum(x, b) {
  let sum = 0;
  let temp = x;
  while (temp > 0) {
    sum += temp % b;
    temp = Math.floor(temp / b);
  }
  return sum;
}

function minimalBase(x) {
  let minSum = Infinity;
  let bestBase = 2;
  
  for (let b = 2; b <= 36; b++) {
    const currentSum = getDigitSum(x, b);
    if (currentSum < minSum) {
      minSum = currentSum;
      bestBase = b;
    }
  }
  
  return [bestBase, minSum];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const x = parseInt(data[0], 10);
  const res = minimalBase(x);
  console.log(res[0] + " " + res[1]);
});
