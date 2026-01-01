class TrieNode {
    constructor() {
        this.children = new Map();
        this.word = null;
        this.rarity = Infinity;
    }
}

class Solution {
    constructor() {
        this.root = new TrieNode();
    }

    replaceWords(dictionary, sentence) {
        // Build trie
        for (const [word, rarity] of Object.entries(dictionary)) {
            this.insert(word, rarity);
        }

        // Process sentence
        const words = sentence.split(' ');
        const result = words.map(word => this.findReplacement(word));
        return result.join(' ');
    }

    insert(word, rarity) {
        let curr = this.root;

        for (const c of word) {
            if (!curr.children.has(c)) {
                curr.children.set(c, new TrieNode());
            }
            curr = curr.children.get(c);
        }

        // Update only if this is better
        if (rarity < curr.rarity ||
            (rarity === curr.rarity && (curr.word === null || word.length < curr.word.length))) {
            curr.word = word;
            curr.rarity = rarity;
        }
    }

    findReplacement(word) {
        let curr = this.root;
        let best = null;
        let bestRarity = Infinity;

        for (const c of word) {
            if (!curr.children.has(c)) break;

            curr = curr.children.get(c);

            if (curr.word !== null) {
                if (curr.rarity < bestRarity ||
                    (curr.rarity === bestRarity && curr.word.length < best.length)) {
                    best = curr.word;
                    bestRarity = curr.rarity;
                }
            }
        }

        return best !== null ? best : word;
    }
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const lines = [];
rl.on('line', (line) => lines.push(line.trim()));
rl.on('close', () => {
    const n = parseInt(lines[0]);
    const dictionary = {};
    
    for (let i = 1; i <= n; i++) {
        const parts = lines[i].split(' ');
        const word = parts[0];
        const rarity = parseInt(parts[1]);
        dictionary[word] = rarity;
    }
    
    const sentence = lines[n + 1];
    
    const sol = new Solution();
    console.log(sol.replaceWords(dictionary, sentence));
});
