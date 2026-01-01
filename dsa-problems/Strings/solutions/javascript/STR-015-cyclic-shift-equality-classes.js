function cyclicShiftEquivalenceClasses(strings) {
  function minimalRotation(s) {
    const doubled = s + s;
    const n = s.length;
    const failure = new Array(2 * n).fill(-1);
    let k = 0;

    for (let j = 1; j < 2 * n; j++) {
      let i = failure[j - k - 1];
      while (i !== -1 && doubled[j] !== doubled[k + i + 1]) {
        if (doubled[j] < doubled[k + i + 1]) {
          k = j - i - 1;
        }
        i = failure[i];
      }

      if (doubled[j] !== doubled[k + i + 1]) {
        if (doubled[j] < doubled[k + i + 1]) {
          k = j;
        }
        failure[j - k] = -1;
      } else {
        failure[j - k] = i + 1;
      }
    }

    return s.slice(k) + s.slice(0, k);
  }

  const canonicalSet = new Set();
  for (const s of strings) {
    const canonical = minimalRotation(s);
    canonicalSet.add(canonical);
  }

  return canonicalSet.size;
}

































const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const strings_n = parseInt(tokens[ptr++]);
    const strings = [];
    for(let i=0; i<strings_n; i++) strings.push(tokens[ptr++]);
    console.log(cyclicShiftEquivalenceClasses(strings));
});
