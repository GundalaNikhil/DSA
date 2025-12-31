class Solution {
  shortestPathWithWalls(grid, k) {
    const rows = grid.length;
    const cols = grid[0].length;
    
    if (rows === 1 && cols === 1) return 0;
    
    const queue = [[0, 0, k, 0]];  // [row, col, walls_left, steps]
    const visited = new Set([`0,0,${k}`]);
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]];
    
    while (queue.length > 0) {
      const [r, c, walls, steps] = queue.shift();
      
      for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;
        
        if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
        
        const newWalls = walls - grid[nr][nc];
        const key = ``nr,`{nc},${newWalls}`;
        
        if (newWalls >= 0 && !visited.has(key)) {
          if (nr === rows - 1 && nc === cols - 1) {
            return steps + 1;
          }
          
          visited.add(key);
          queue.push([nr, nc, newWalls, steps + 1]);
        }
      }
    }
    
    return -1;
  }
}
