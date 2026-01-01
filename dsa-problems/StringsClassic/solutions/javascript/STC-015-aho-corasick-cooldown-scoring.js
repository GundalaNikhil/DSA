const readline = require("readline");

class Node {
  constructor() {
    this.children = new Array(26).fill(null);
    this.fail = null;
    this.output = null;
    this.patterns = []; // [len, weight] for cooldown, or just indices for counting
  }
}

class Solution {
  buildAhoCorasick(patterns, weights = null) {
    const root = new Node();

    // 1. Build Trie
    for (let i = 0; i < patterns.length; i++) {
      let curr = root;
      for (let j = 0; j < patterns[i].length; j++) {
        const idx = patterns[i].charCodeAt(j) - 97;
        if (!curr.children[idx]) curr.children[idx] = new Node();
        curr = curr.children[idx];
      }
      const w = weights ? weights[i] : 1;
      curr.patterns.push([patterns[i].length, w]);
    }

    // 2. Build Failure Links
    const q = [];
    for (let i = 0; i < 26; i++) {
      if (root.children[i]) {
        root.children[i].fail = root;
        q.push(root.children[i]);
      } else {
        root.children[i] = root;
      }
    }

    let head = 0;
    while (head < q.length) {
      const curr = q[head++];

      if (curr.fail.patterns.length > 0) curr.output = curr.fail;
      else curr.output = curr.fail.output;

      for (let i = 0; i < 26; i++) {
        if (curr.children[i]) {
          curr.children[i].fail = curr.fail.children[i];
          q.push(curr.children[i]);
        } else {
          curr.children[i] = curr.fail.children[i];
        }
      }
    }

    return root;
  }

  maxCooldownScore(text, patterns, weights, g) {
    const root = this.buildAhoCorasick(patterns, weights);

    // 3. DP
    const n = text.length;
    const dp = new Array(n + 1).fill(0);
    let curr = root;

    for (let i = 0; i < n; i++) {
      dp[i + 1] = dp[i];
      const idx = text.charCodeAt(i) - 97;
      curr = curr.children[idx];

      let temp = curr;
      while (temp !== root) {
        for (const [len, w] of temp.patterns) {
          const prevIdx = i + 1 - len - g;
          const prevScore = (prevIdx < 0) ? 0 : dp[prevIdx];
          if (prevScore + w > dp[i + 1]) {
            dp[i + 1] = prevScore + w;
          }
        }
        if (!temp.output) break;
        temp = temp.output;
      }
    }

    return dp[n];
  }

  countMatches(text, patterns) {
    const root = this.buildAhoCorasick(patterns);
    let curr = root;
    let count = 0;

    for (let i = 0; i < text.length; i++) {
      const idx = text.charCodeAt(i) - 97;
      curr = curr.children[idx];

      let temp = curr;
      while (temp !== root) {
        count += temp.patterns.length;
        if (!temp.output) break;
        temp = temp.output;
      }
    }

    return count;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;

  // Detect format: MD has first token as number (k), YAML has first token as string (text)
  const firstToken = data[0];
  let isMDFormat = false;
  try {
    const k = parseInt(firstToken, 10);
    // If parsing succeeds and result is reasonable, it's MD format
    isMDFormat = !isNaN(k) && k > 0 && k < 100000;
  } catch (e) {
    isMDFormat = false;
  }

  const solution = new Solution();
  let idx = 0;

  if (isMDFormat) {
    try {
      const k = parseInt(data[idx++], 10);
      const patterns = [];
      const weights = [];
      for (let i = 0; i < k; i++) {
        patterns.push(data[idx++]);
        weights.push(parseInt(data[idx++], 10));
      }
      const g = parseInt(data[idx++], 10);
      const text = data[idx] || "";
      console.log(solution.maxCooldownScore(text, patterns, weights, g).toString());
    } catch (e) {
      // Fallback
    }
  } else {
    try {
      const text = data[idx++];
      const k = parseInt(data[idx++], 10);
      const patterns = [];
      for (let i = 0; i < k; i++) {
        patterns.push(data[idx++]);
      }
      console.log(solution.countMatches(text, patterns).toString());
    } catch (e) {
      // Fallback
    }
  }
});
