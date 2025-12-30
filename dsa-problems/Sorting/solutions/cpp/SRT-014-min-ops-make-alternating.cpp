#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    struct Top {
        int val = -1;
        int count = 0;
    };
    
    pair<Top, Top> getTopTwo(const map<int, int>& counts) {
        Top first, second;
        for (auto const& [val, count] : counts) {
            if (count > first.count) {
                second = first;
                first = {val, count};
            } else if (count > second.count) {
                second = {val, count};
            }
        }
        return {first, second};
    }

public:
    int minChanges(const vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return 0;
        
        map<int, int> evenCounts;
        map<int, int> oddCounts;
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) evenCounts[arr[i]]++;
            else oddCounts[arr[i]]++;
        }
        
        auto [e1, e2] = getTopTwo(evenCounts);
        auto [o1, o2] = getTopTwo(oddCounts);
        
        if (e1.val != o1.val) {
            return n - (e1.count + o1.count);
        } else {
            int opt1 = n - (e1.count + o2.count);
            int opt2 = n - (e2.count + o1.count);
            return min(opt1, opt2);
        }
    }
};
