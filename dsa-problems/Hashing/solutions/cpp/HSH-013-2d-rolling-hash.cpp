#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE1 = 313;
    const long long BASE2 = 317;

public:
    bool findMatrix(vector<vector<int>>& A, vector<vector<int>>& B) {
        int n = A.size(), m = A[0].size();
        int p = B.size(), q = B[0].size();
        
        if (p > n || q > m) return false;
        
        long long targetHash = computeMatrixHash(B, p, q);
        
        vector<vector<long long>> rowHashes(n, vector<long long>(m - q + 1));
        long long power1 = 1;
        for (int k = 0; k < q - 1; k++) power1 = (power1 * BASE1) % MOD;
        
        for (int i = 0; i < n; i++) {
            long long h = 0;
            for (int k = 0; k < q; k++) {
                h = (h * BASE1 + A[i][k]) % MOD;
            }
            rowHashes[i][0] = h;
            
            for (int j = 1; j <= m - q; j++) {
                long long remove = (A[i][j - 1] * power1) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE1 + A[i][j + q - 1]) % MOD;
                rowHashes[i][j] = h;
            }
        }
        
        long long power2 = 1;
        for (int k = 0; k < p - 1; k++) power2 = (power2 * BASE2) % MOD;
        
        for (int j = 0; j <= m - q; j++) {
            long long h = 0;
            for (int k = 0; k < p; k++) {
                h = (h * BASE2 + rowHashes[k][j]) % MOD;
            }
            if (h == targetHash) return true;
            
            for (int i = 1; i <= n - p; i++) {
                long long remove = (rowHashes[i - 1][j] * power2) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE2 + rowHashes[i + p - 1][j]) % MOD;
                
                if (h == targetHash) return true;
            }
        }
        
        return false;
    }
    
    long long computeMatrixHash(const vector<vector<int>>& M, int p, int q) {
        vector<long long> rowH(p);
        for (int i = 0; i < p; i++) {
            long long h = 0;
            for (int j = 0; j < q; j++) {
                h = (h * BASE1 + M[i][j]) % MOD;
            }
            rowH[i] = h;
        }
        
        long long finalH = 0;
        for (int i = 0; i < p; i++) {
            finalH = (finalH * BASE2 + rowH[i]) % MOD;
        }
        return finalH;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<vector<int>> A(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> A[i][j];
        }
    }
    
    int p, q;
    if (!(cin >> p >> q)) return 0;
    
    vector<vector<int>> B(p, vector<int>(q));
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < q; j++) {
            cin >> B[i][j];
        }
    }
    
    Solution solution;
    cout << (solution.findMatrix(A, B) ? "true" : "false") << "\n";
    
    return 0;
}
