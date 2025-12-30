#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int toggleRangesMinFlips(vector<int>& A, vector<int>& B) {
        int n = A.size();
        int count = 0;
        int prevDiff = 0;
        
        for (int i = 0; i < n; i++) {
            int currDiff = A[i] ^ B[i];
            if (currDiff == 1 && prevDiff == 0) {
                count++;
            }
            prevDiff = currDiff;
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    vector<int> B(n);
    for (int i = 0; i < n; i++) cin >> B[i];

    Solution solution;
    cout << solution.toggleRangesMinFlips(A, B) << "\n";
    return 0;
}
