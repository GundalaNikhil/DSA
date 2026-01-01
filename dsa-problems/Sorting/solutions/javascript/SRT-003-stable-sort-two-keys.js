class Solution {
  stableSort(records) {
    // JavaScript's sort is stable (since ES2019)
    records.sort((a, b) => {
      if (a[0] !== b[0]) {
        return a[0] - b[0];
      }
      return a[1] - b[1]; // Ascending for key2
    });
    return records;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const records = [];
for (let i = 0; i < n; i++) {
  const a = parseInt(data[idx++], 10);
  const b = parseInt(data[idx++], 10);
  records.push([a, b]);
}
const solution = new Solution();
const result = solution.stableSort(records);
const lines = result.map((r) => `${r[0]} ${r[1]}`);
console.log(lines.join("\n"));
