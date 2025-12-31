#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int countDistinctSubstrings(string s) {
        int n = s.length();
        unordered_set<long long> distinctHashes;
        // Pre-allocate to avoid resizing overhead if possible, though hard to predict size
        // distinctHashes.reserve(n * n / 2); 
        
        for (int i = 0; i < n; i++) {
            long long currentHash = 0;
            for (int j = i; j < n; j++) {
                currentHash = (currentHash * BASE + s[j]) % MOD;
                distinctHashes.insert(currentHash);
            }
        }
        
        return distinctHashes.size() + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.countDistinctSubstrings(s) << "\n";
    }
    
    return 0;
}
