#include <vector>
using namespace std;

class Solution {
public:
    int countUnsafe(const vector<int>& d) {
        int unsafeCount = 0;
        for (size_t i = 0; i < d.size() - 1; ++i) {
            if (d[i] < d[i+1]) {
                unsafeCount++;
            }
        }
        return unsafeCount;
    }
};
