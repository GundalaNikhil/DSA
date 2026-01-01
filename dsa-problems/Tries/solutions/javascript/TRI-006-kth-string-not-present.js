const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

function* allCombinationsOfLength(length) {
    const chars = 'abcdefghijklmnopqrstuvwxyz';
    
    function* helper(current, remaining) {
        if (remaining === 0) {
            yield current;
            return;
        }
        for (const c of chars) {
            yield* helper(current + c, remaining - 1);
        }
    }
    
    yield* helper('', length);
}

const lines = [];
rl.on('line', (line) => lines.push(line.trim()));
rl.on('close', () => {
    const [n, L, k] = lines[0].split(' ').map(Number);
    
    const inserted = new Set();
    for (let i = 1; i <= n; i++) {
        inserted.add(lines[i]);
    }
    
    const allStrings = [];
    
    // Order: a, aa, ab, ..., az, b, ba, bb, ..., bz, c, ...
    const chars = 'abcdefghijklmnopqrstuvwxyz';
    for (const char of chars) {
        // Add single character if not inserted and L >= 1
        if (L >= 1 && !inserted.has(char)) {
            allStrings.push(char);
        }
        
        // Add all multi-char strings starting with this char
        for (let length = 2; length <= L; length++) {
            for (const rest of allCombinationsOfLength(length - 1)) {
                const combo = char + rest;
                if (!inserted.has(combo)) {
                    allStrings.push(combo);
                }
            }
        }
    }
    
    console.log(k <= allStrings.length ? allStrings[k - 1] : '');
});
