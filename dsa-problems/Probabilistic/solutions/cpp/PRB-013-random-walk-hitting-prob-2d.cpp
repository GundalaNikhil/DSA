#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double hitProbability(int a, int b, int T) {
        if (a == 0 && b == 0) return 1.0;
        
        int offset = T;
        int size = 2 * T + 1;
        
        // Use vector of vectors
        vector<vector<double>> dp(size, vector<double>(size, 0.0));
        
        int targetX = a + offset;
        int targetY = b + offset;
        
        dp[offset][offset] = 1.0;
        
        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};
        
        for (int t = 1; t <= T; t++) {
            vector<vector<double>> nextDp(size, vector<double>(size, 0.0));
            
            nextDp[targetX][targetY] = dp[targetX][targetY];
            
            int minVal = max(0, offset - (t - 1));
            int maxVal = min(size - 1, offset + (t - 1));
            
            for (int x = minVal; x <= maxVal; x++) {
                for (int y = minVal; y <= maxVal; y++) {
                    if (dp[x][y] == 0) continue;
                    if (x == targetX && y == targetY) continue;
                    
                    double prob = dp[x][y] * 0.25;
                    for (int i = 0; i < 4; i++) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];
                        nextDp[nx][ny] += prob;
                    }
                }
            }
            dp = nextDp;
        }
        
        return dp[targetX][targetY];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, T;
    if (cin >> a >> b >> T) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.hitProbability(a, b, T) << "\n";
    }
    return 0;
}
