#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int>> packCombinations(const vector<int>& values, const vector<int>& packs, int target) {
        set<vector<int>> unique_results;
        vector<int> current;
        backtrack(0, 0, current, values, packs, target, unique_results);
        
        vector<vector<int>> result(unique_results.begin(), unique_results.end());
        return result;
    }

private:
    void backtrack(int idx, int currentSum, vector<int>& current, 
                   const vector<int>& values, const vector<int>& packs, int target, 
                   set<vector<int>>& results) {
        if (currentSum == target) {
            vector<int> temp = current;
            sort(temp.begin(), temp.end());
            results.insert(temp);
            return;
        }
        if (idx == values.size() || currentSum > target) {
            return;
        }

        // Option 1: Include
        int packVal = values[idx];
        int packSize = packs[idx];
        int totalVal = packVal * packSize;

        if (currentSum + totalVal <= target) {
            for(int k=0; k<packSize; ++k) current.push_back(packVal);
            backtrack(idx + 1, currentSum + totalVal, current, values, packs, target, results);
            for(int k=0; k<packSize; ++k) current.pop_back();
        }

        // Option 2: Exclude
        backtrack(idx + 1, currentSum, current, values, packs, target, results);
    }
};
