function longestAlternatingVC(s) {
    if (!s) return [0, ""];

    const vowels = "aeiou";
    const isVowel = (c) => vowels.includes(c);

    let maxLen = 1;
    let bestStart = 0;
    let currentLen = 1;
    let start = 0;
    
    // JS string index access
    let prevIsVowel = isVowel(s[0]);

    for (let i = 1; i < s.length; i++) {
        const currIsVowel = isVowel(s[i]);
        if (currIsVowel !== prevIsVowel) {
            currentLen++;
            if (currentLen > maxLen) {
                maxLen = currentLen;
                bestStart = start;
            }
        } else {
            start = i;
            currentLen = 1;
        }
        prevIsVowel = currIsVowel;
    }

    return [maxLen, s.substring(bestStart, bestStart + maxLen)];
}
















const fs = require('fs');
const s = fs.readFileSync(0, 'utf-8').trim();
const res = longestAlternatingVC(s);
console.log(res[0]);
console.log(res[1]);
