class TrieNode {
    constructor() {
        this.children = new Map();
    }
}

class Solution {
    constructor() {
        this.nodeCount = 0;
    }

    countDistinctSubstrings(s) {
        if (!s || s.length === 0) return 0;

        const root = new TrieNode();
        const n = s.length;

        // Insert all suffixes
        for (let i = 0; i < n; i++) {
            this.insertSuffix(root, s, i);
        }

        return this.nodeCount;
    }

    insertSuffix(root, s, start) {
        let curr = root;

        for (let i = start; i < s.length; i++) {
            const c = s[i];

            if (!curr.children.has(c)) {
                curr.children.set(c, new TrieNode());
                this.nodeCount++;  // New node = new distinct substring
            }

            curr = curr.children.get(c);
        }
    }
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', (line) => {
    const s = line.trim();
    const sol = new Solution();
    console.log(sol.countDistinctSubstrings(s));
    rl.close();
});
