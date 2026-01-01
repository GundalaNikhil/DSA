const readline = require("readline");

class Solution {
  longestPalindromicPrefix(s, c) {
    const T = s + c;
    const n = T.length;

    const MOD = 1000000007n;
    const BASE = 313n;

    let fwdHash = 0n;
    let revHash = 0n;
    let power = 1n;

    let maxLen = 0;

    for (let i = 0; i < n; i++) {
      const val = BigInt(T.charCodeAt(i));

      fwdHash = (fwdHash * BASE + val) % MOD;
      revHash = (revHash + val * power) % MOD;

      if (fwdHash === revHash) {
        maxLen = i + 1;
      }

      power = (power * BASE) % MOD;
    }

    return maxLen;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8");
if (input.length > 0) {
  const raw = input.split("\n").map((line) => line.replace(/\r$/, ""));
  let s = "";
  let cstr = "";
  if (raw.length === 1) {
    s = "";
    cstr = raw[0];
  } else {
    s = raw[0];
    for (let i = 1; i < raw.length; i++) {
      if (raw[i].length > 0) {
        cstr = raw[i];
        break;
      }
    }
    if (cstr.length === 0) cstr = raw[1];
  }
  if (cstr.length > 0) {
    const c = cstr[0];
    const solution = new Solution();
    console.log(solution.longestPalindromicPrefix(s, c));
  }
}
