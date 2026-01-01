class TrieNode {
  constructor() {
    this.children = new Map();
    this.strings = [];
  }
}

function minimalRemovalUniquePrefixes(L, strings) {
  const root = new TrieNode();

  // Build trie
  for (const s of strings) {
    let node = root;
    for (let i = 0; i < Math.min(s.length, L); i++) {
      const c = s[i];
      if (!node.children.has(c)) {
        node.children.set(c, new TrieNode());
      }
      node = node.children.get(c);
    }
    node.strings.push(s);
  }

  // Find conflicts
  let totalDeletions = 0;

  function findConflicts(node, depth) {
    if (depth === L) {
      if (node.strings.length > 1) {
        // Sort by length descending
        node.strings.sort((a, b) => b.length - a.length);

        // Delete all except longest
        for (let i = 1; i < node.strings.length; i++) {
          const s = node.strings[i];
          if (s.length >= L) {
            totalDeletions += s.length - (L - 1);
          }
        }
      }
      return;
    }

    for (const child of node.children.values()) {
      findConflicts(child, depth + 1);
    }
  }

  findConflicts(root, 0);
  return totalDeletions;
}


const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const L = parseInt(tokens[ptr++]);
    const strings_n = parseInt(tokens[ptr++]);
    const strings = [];
    for(let i=0; i<strings_n; i++) strings.push(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.minimalRemovalUniquePrefixes(L, strings));
});
