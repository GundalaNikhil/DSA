#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int maxRepeatedBlockLength(string s) {
        int n = s.length();
        int low = 0, high = n / 2;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            if (check(s, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    bool check(const string& s, int len) {
        int n = s.length();
        unordered_map<long long, int> firstOccurrence;
        
        long long currentHash = 0;
        long long power = 1;
        
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + s[i]) % MOD;
        }
        firstOccurrence[currentHash] = 0;
        
        for (int i = 1; i <= n - len; i++) {
            long long remove = (s[i - 1] * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            currentHash = (currentHash * BASE + s[i + len - 1]) % MOD;
            
            if (firstOccurrence.count(currentHash)) {
                if (i >= firstOccurrence[currentHash] + len) {
                    return true;
                }
            } else {
                firstOccurrence[currentHash] = i;
            }
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.maxRepeatedBlockLength(s) << "\n";
    }
    
    return 0;
}
