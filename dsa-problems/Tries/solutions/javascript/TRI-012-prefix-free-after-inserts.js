const readline = require('readline');

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
  }

  insert(number) {
    let node = this.root;
    for (const char of number) {
      if (node.isEnd) return false;
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
    }
    
    if (node.children.size > 0) return false;
    node.isEnd = true;
    return true;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const lines = [];
rl.on('line', (line) => {
  lines.push(line);
}).on('close', () => {
  const n = parseInt(lines[0]);
  const solution = new Solution();
  const results = [];
  
  for (let i = 1; i <= n; i++) {
    results.push(solution.insert(lines[i].trim()));
  }
  
  console.log('[' + results.join(',') + ']');
});
