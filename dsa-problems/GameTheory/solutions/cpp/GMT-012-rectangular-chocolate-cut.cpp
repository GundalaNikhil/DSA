#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string chocolateCut(long long R, long long C) {
        long long area = R * C;
        return (area % 2 == 0) ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long R, C;
    if (cin >> R >> C) {
        Solution solution;
        cout << solution.chocolateCut(R, C) << "\n";
    }
    return 0;
}
