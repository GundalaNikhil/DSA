#include <iostream>
using namespace std;

class Solution {
public:
    long long swapAdjacent2BitBlocks(int x) {
        // Cast to unsigned to ensure logical shift
        unsigned int ux = (unsigned int)x;

        unsigned int evenMask = 0x33333333;
        unsigned int oddMask = 0xCCCCCCCC;

        unsigned int evenBlocks = ux & evenMask;
        unsigned int oddBlocks = ux & oddMask;

        unsigned int result = (evenBlocks << 2) | (oddBlocks >> 2);
        return result & 0xFFFFFFFFU;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned int x;
    if (!(cin >> x)) return 0;

    Solution solution;
    cout << solution.swapAdjacent2BitBlocks((int)x) << "\n";
    return 0;
}
