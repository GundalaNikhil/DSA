#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long maxFinalStrength(const vector<int>& strengths, const vector<int>& priority) {
        long long totalSum = 0;
        bool has1 = false, has2 = false, has3 = false;
        
        for (size_t i = 0; i < strengths.size(); i++) {
            totalSum += strengths[i];
            if (priority[i] == 1) has1 = true;
            else if (priority[i] == 2) has2 = true;
            else if (priority[i] == 3) has3 = true;
        }
        
        long long penalty = 0;
        if (has1 && has2 && has3) penalty = 2;
        else if (has1 && has2) penalty = 1;
        else if (has2 && has3) penalty = 1;
        else if (has1 && has3) penalty = 2;
        
        return totalSum - penalty;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> strengths(n), priority(n);
        for (int i = 0; i < n; i++) cin >> strengths[i];
        for (int i = 0; i < n; i++) cin >> priority[i];
        
        Solution solution;
        cout << solution.maxFinalStrength(strengths, priority) << "\n";
    }
    return 0;
}
