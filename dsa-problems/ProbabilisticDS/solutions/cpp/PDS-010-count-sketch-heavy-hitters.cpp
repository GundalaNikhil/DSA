#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countSketchEstimate(const vector<int>& count, const vector<int>& sign) {
        int d = count.size();
        vector<int> estimates(d);
        for (int i = 0; i < d; i++) {
            estimates[i] = count[i] * sign[i];
        }
        sort(estimates.begin(), estimates.end());
        return estimates[d / 2];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d;
    if (cin >> d) {
        vector<int> count(d), sign(d);
        for (int i = 0; i < d; i++) {
            cin >> count[i] >> sign[i];
        }
    
        Solution solution;
        cout << solution.countSketchEstimate(count, sign) << "\n";
    }
    return 0;
}
