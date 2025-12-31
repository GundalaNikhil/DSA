const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null]; // 0 and 1
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
  }

  insert(s) {
    let node = this.root;
    for (const char of s) {
      const idx = parseInt(char);
      if (node.children[idx] === null) {
        node.children[idx] = new TrieNode();
      }
      node = node.children[idx];
    }
    node.isEnd = true;
  }

  dfs(node, path, L) {
    if (path.length === L) {
      return node.isEnd ? null : path;
    }

    // Try '0' first
    if (node.children[0] === null) {
      return path + "0".repeat(L - path.length);
    }

    let result = this.dfs(node.children[0], path + "0", L);
    if (result !== null) return result;

    // Try '1'
    if (node.children[1] === null) {
      return path + "1" + "0".repeat(L - path.length - 1);
    }

    return this.dfs(node.children[1], path + "1", L);
  }

  findShortestAbsent(binaryStrings, L) {
    if (binaryStrings.length === Math.pow(2, L)) {
      return "";
    }

    for (const s of binaryStrings) {
      this.insert(s);
    }

    return this.dfs(this.root, "", L) || "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [L, n] = lines[0].split(" ").map(Number);
  const binaryStrings = [];
  for (let i = 1; i <= n; i++) {
    binaryStrings.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.findShortestAbsent(binaryStrings, L);

  console.log(result);
});
