const fs = require("fs");

const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 0 || data[0] === "") {
  process.exit(0);
}
const n = parseInt(data[0], 10);
process.stdout.write(n.toString());
