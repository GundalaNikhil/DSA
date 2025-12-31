#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countVisible(const vector<int>& h) {
        int count = 0;
        int maxH = -1;
        
        for (int height : h) {
            if (height > maxH) {
                count++;
                maxH = height;
            }
        }
        return count;
    }
};
