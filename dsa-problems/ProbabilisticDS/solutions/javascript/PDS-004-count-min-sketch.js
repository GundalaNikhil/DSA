const readline = require("readline");

function cmsParams(epsilon, delta) {
  const w = Math.ceil(Math.E / epsilon);
  const d = Math.ceil(Math.log(1.0 / delta));
  return [w, d];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const epsilon = parseFloat(data[0]);
  const delta = parseFloat(data[1]);
  const res = cmsParams(epsilon, delta);
  console.log(res[0] + " " + res[1]);
});
