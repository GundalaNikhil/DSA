const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const lines = [];
rl.on('line', (line) => lines.push(line.trim()));
rl.on('close', () => {
    const [n, L] = lines[0].split(' ').map(Number);
    const arr = lines[1].split(' ').map(Number);
    
    let minXor = Infinity;
    
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const xorVal = arr[i] ^ arr[j];
            if (xorVal <= L) {
                minXor = Math.min(minXor, xorVal);
            }
        }
    }
    
    console.log(minXor === Infinity ? -1 : minXor);
});
