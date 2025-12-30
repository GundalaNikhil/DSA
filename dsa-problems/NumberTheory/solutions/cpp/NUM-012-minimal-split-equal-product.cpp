#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long minimalProductSplit(long long x) {
        string s = to_string(x);
        int n = s.length();
        long long minProd = -1; // Using -1 to indicate not set
        
        for (int i = 1; i < n; i++) {
            string part1 = s.substr(0, i);
            string part2 = s.substr(i);
            
            long long a = stoll(part1);
            long long b = stoll(part2);
            
            long long prod = a * b;
            if (prod > 0) {
                if (minProd == -1 || prod < minProd) {
                    minProd = prod;
                }
            }
        }
        
        return minProd;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x;
    if (cin >> x) {
        Solution solution;
        cout << solution.minimalProductSplit(x) << "\n";
    }
    return 0;
}
