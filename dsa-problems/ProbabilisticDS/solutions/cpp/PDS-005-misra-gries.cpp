#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> misraGries(const vector<int>& stream, int k) {
        map<int, int> counts;
        
        for (int x : stream) {
            if (counts.count(x)) {
                counts[x]++;
            } else if (counts.size() < k - 1) {
                counts[x] = 1;
            } else {
                // Decrement all
                vector<int> toRemove;
                for (auto& pair : counts) {
                    pair.second--;
                    if (pair.second == 0) {
                        toRemove.push_back(pair.first);
                    }
                }
                for (int key : toRemove) {
                    counts.erase(key);
                }
            }
        }
        
        vector<int> res;
        for (auto& pair : counts) {
            res.push_back(pair.first);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> stream(n);
        for (int i = 0; i < n; i++) cin >> stream[i];
    
        Solution solution;
        vector<int> res = solution.misraGries(stream, k);
        for (int i = 0; i < (int)res.size(); i++) {
            if (i) cout << " ";
            cout << res[i];
        }
        cout << "\n";
    }
    return 0;
}
