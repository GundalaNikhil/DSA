class Solution {
  ladders(start, end, dict) {
    const wordSet = new Set(dict);
    wordSet.add(start);
    wordSet.add(end);

    const isVowel = (c) => "aeiou".includes(c);
    const isAlternating = (a, b) => isVowel(a[0]) !== isVowel(b[0]);

    const parents = new Map();
    const dist = new Map();
    const queue = [start];
    dist.set(start, 0);

    let found = false;
    let head = 0;

    while (head < queue.length) {
      if (found) break; // Finish processing current level then stop
      // We need to be careful not to process next level if found.
      
      // Collect current level nodes
      const levelSize = queue.length - head;
      const currentLevelNodes = [];
      for(let i=0; i<levelSize; i++) currentLevelNodes.push(queue[head+i]);
      
      // Check if end is in this level
      if (currentLevelNodes.includes(end)) found = true;
      
      const levelVisited = new Set();
      
      for (let i = 0; i < levelSize; i++) {
        const curr = queue[head++];
        const curDist = dist.get(curr);
        
        // Generate neighbors
        const chars = curr.split("");
        for (let j = 0; j < chars.length; j++) {
          const original = chars[j];
          for (let k = 0; k < 26; k++) {
            const c = String.fromCharCode(97 + k);
            if (c === original) continue;
            chars[j] = c;
            const neighbor = chars.join("");
            
            if (wordSet.has(neighbor) && isAlternating(curr, neighbor)) {
               if (!dist.has(neighbor)) {
                 if (!levelVisited.has(neighbor)) {
                   dist.set(neighbor, curDist + 1);
                   queue.push(neighbor);
                   levelVisited.add(neighbor);
                 }
                 if (!parents.has(neighbor)) parents.set(neighbor, []);
                 parents.get(neighbor).push(curr);
               } else if (dist.get(neighbor) === curDist + 1) {
                 if (!parents.has(neighbor)) parents.set(neighbor, []);
                 parents.get(neighbor).push(curr);
               }
            }
          }
          chars[j] = original;
        }
      }
    }

    const results = [];
    if (found) {
      const backtrack = (curr, path) => {
        if (curr === start) {
          results.push([...path].reverse());
          return;
        }
        const pars = parents.get(curr) || [];
        for (const p of pars) {
          path.push(p);
          backtrack(p, path);
          path.pop();
        }
      };
      backtrack(end, [end]);
    }
    
    results.sort((a, b) => {
        const sa = a.join(" ");
        const sb = b.join(" ");
        return sa.localeCompare(sb);
    });

    return results;
  }
}
