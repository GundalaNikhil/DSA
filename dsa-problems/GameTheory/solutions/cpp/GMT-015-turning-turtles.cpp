#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string turningTurtles(int n, int k, string s) {
        long long xorSum = 0;
        long long mod = k + 1;
        for (int i = 0; i < (int)s.length(); i++) {
            if (s[i] == 'H') {
                xorSum ^= ((i % mod) + 1);
            }
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    if (cin >> n >> k) {
        string s;
        cin >> s;
        
        Solution solution;
        cout << solution.turningTurtles(n, k, s) << "\n";
    }
    return 0;
}
