function shortestCoveringWindow(arr, T) {
  if (!arr || arr.length === 0 || !T || T.size === 0) {
    return [0, []];
  }

  const required = new Map();
  for (let s of T) {
    required.set(s, 1);
  }

  const windowCounts = new Map();
  let left = 0,
    formed = 0;
  let minLen = Infinity;
  let resultLeft = 0,
    resultRight = 0;

  for (let right = 0; right < arr.length; right++) {
    const s = arr[right];
    windowCounts.set(s, (windowCounts.get(s) || 0) + 1);

    if (required.has(s) && windowCounts.get(s) === 1) {
      formed++;
    }

    while (formed === T.size && left <= right) {
      if (right - left + 1 < minLen) {
        minLen = right - left + 1;
        resultLeft = left;
        resultRight = right;
      }

      const leftS = arr[left];
      windowCounts.set(leftS, windowCounts.get(leftS) - 1);
      if (required.has(leftS) && windowCounts.get(leftS) === 0) {
        formed--;
      }

      left++;
    }
  }

  if (minLen === Infinity) {
    return [0, []];
  }

  return [minLen, arr.slice(resultLeft, resultRight + 1)];
}
































const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const arr_n = parseInt(tokens[ptr++]);
    const arr = [];
    for(let i=0; i<arr_n; i++) arr.push(tokens[ptr++]);
    const T_n = parseInt(tokens[ptr++]);
    const T = new Set();
    for(let i=0; i<T_n; i++) T.add(tokens[ptr++]);
    const res = shortestCoveringWindow(arr, T);
    console.log(res[0]);
    if(res[1].length > 0) { for(const s of res[1]) console.log(s); } else { console.log('NONE'); }
});
