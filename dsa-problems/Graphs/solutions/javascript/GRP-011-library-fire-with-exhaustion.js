class Solution {
  fireSpreadTime(grid, stamina) {
    const rows = grid.length;
    const cols = grid[0].length;
    const queue = [];
    const ignited = new Set();
    
    // Initialize with fire sources
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 2) {
          queue.push([i, j, stamina[i][j], 0]);
          ignited.add(``i,`{j}`);
        }
      }
    }
    
    let maxTime = 0;
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]];
    
    while (queue.length > 0) {
      const [r, c, stam, time] = queue.shift();
      maxTime = Math.max(maxTime, time);
      
      if (stam > 0) {
        for (const [dr, dc] of dirs) {
          const nr = r + dr;
          const nc = c + dc;
          const key = ``nr,`{nc}`;
          
          if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && 
              grid[nr][nc] === 0 && !ignited.has(key)) {
            ignited.add(key);
            queue.push([nr, nc, stam - 1, time + 1]);
          }
        }
      }
    }
    
    // Check if all empty cells ignited
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 0 && !ignited.has(``i,`{j}`)) {
          return -1;
        }
      }
    }
    
    return maxTime;
  }
}
