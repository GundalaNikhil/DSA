#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <tuple>
using namespace std;

class Solution {
private:
    int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
public:
    int shortestPathWithWalls(vector<vector<int>>& grid, int k) {
        int rows = grid.size();
        int cols = grid[0].size();
        
        if (rows == 1 && cols == 1) return 0;
        
        queue<tuple<int,int,int,int>> q;  // row, col, walls_left, steps
        set<tuple<int,int,int>> visited;
        
        q.push({0, 0, k, 0});
        visited.insert({0, 0, k});
        
        while (!q.empty()) {
            auto [r, c, walls, steps] = q.front();
            q.pop();
            
            for (auto& dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                
                int newWalls = walls - grid[nr][nc];
                
                if (newWalls >= 0 && visited.find({nr, nc, newWalls}) == visited.end()) {
                    if (nr == rows - 1 && nc == cols - 1) {
                        return steps + 1;
                    }
                    
                    visited.insert({nr, nc, newWalls});
                    q.push({nr, nc, newWalls, steps + 1});
                }
            }
        }
        
        return -1;
    }
};
