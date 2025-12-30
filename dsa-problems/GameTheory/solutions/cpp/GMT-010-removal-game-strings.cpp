#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    int getGrundy(int k) {
        if (k == 0) return 0;
        if (k == 1) return 1;
        if (k == 2) return 0;
        int rem = k % 3;
        if (rem == 0) return 2;
        if (rem == 1) return 1;
        return 0;
    }
public:
    string stringGame(int n, vector<string>& strings) {
        int xorSum = 0;
        for (const string& s : strings) {
            if (s.empty()) continue;
            int groups = 1;
            for (size_t i = 1; i < s.length(); i++) {
                if (s[i] != s[i - 1]) {
                    groups++;
                }
            }
            xorSum ^= getGrundy(groups);
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<string> strings(n);
        for (int i = 0; i < n; i++) {
            cin >> strings[i];
        }
        
        Solution solution;
        cout << solution.stringGame(n, strings) << "\n";
    }
    return 0;
}
