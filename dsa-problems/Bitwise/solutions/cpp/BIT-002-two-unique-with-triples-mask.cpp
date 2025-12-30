#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoUniqueWithTriplesMask(vector<int>& a, int M) {
        int splitBit = -1;

        for (int i = 0; i < 31; i++) {
            if (!((M >> i) & 1)) continue;

            int count = 0;
            for (int x : a) {
                if ((x >> i) & 1) count++;
            }

            if (count % 3 == 1) {
                splitBit = i;
                break;
            }
        }

        // If no split bit found in M, find any distinguishing bit
        if (splitBit == -1) {
            for (int i = 0; i < 31; i++) {
                int count = 0;
                for (int x : a) {
                    if ((x >> i) & 1) count++;
                }
                if (count % 3 == 1) {
                    splitBit = i;
                    break;
                }
            }
        }

        int num1 = 0, num2 = 0;

        for (int i = 0; i < 31; i++) {
            int c1 = 0, c2 = 0;
            for (int x : a) {
                int bitVal = (x >> i) & 1;
                if ((x >> splitBit) & 1) {
                    c2 += bitVal;
                } else {
                    c1 += bitVal;
                }
            }
            if (c1 % 3 == 1) num1 |= (1 << i);
            if (c2 % 3 == 1) num2 |= (1 << i);
        }

        vector<int> res = {num1, num2};
        sort(res.begin(), res.end());
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int M;
    cin >> M;

    Solution solution;
    vector<int> result = solution.twoUniqueWithTriplesMask(a, M);
    cout << result[0] << " " << result[1] << "\n";
    return 0;
}
