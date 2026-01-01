function canRotateToPalindrome(s) {
    if (!s || s.length <= 1) return true;
    const n = s.length;
    const doubled = s + s;

    for (let i = 0; i < n; i++) {
        const rotated = doubled.substring(i, i + n);
        if (isPalindrome(rotated)) return true;
    }
    return false;
}

function isPalindrome(s) {
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}














const fs = require('fs');
const s = fs.readFileSync(0, 'utf-8').trim();
console.log(canRotateToPalindrome(s) ? 'true' : 'false');
