const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    
    const sol = new Solution();
    const res = sol.getAlternatingPermutations(s);
    
    if(res.length === 0) {
        console.log("NONE");
    } else {
        res.forEach(p => console.log(p));
    }
});

class Solution {
    getAlternatingPermutations(s) {
        const results = new Set();
        const used = new Array(s.length).fill(false);
        const chars = s.split('');
        
        const isVowel = (c) => "aeiou".includes(c);
        
        const backtrack = (current) => {
            if (current.length === s.length) {
                results.add(current);
                return;
            }
            
            const lastChar = current.length > 0 ? current[current.length - 1] : null;
            const lastIsVowel = lastChar ? isVowel(lastChar) : false;
            
            for (let i = 0; i < s.length; i++) {
                if (!used[i]) {
                    const nextChar = chars[i];
                    const nextIsVowel = isVowel(nextChar);
                    
                    if (current.length === 0 || lastIsVowel !== nextIsVowel) {
                        used[i] = true;
                        backtrack(current + nextChar);
                        used[i] = false;
                    }
                }
            }
        };
        
        backtrack("");
        const sortedRes = Array.from(results).sort();
        return sortedRes;
    }
}
