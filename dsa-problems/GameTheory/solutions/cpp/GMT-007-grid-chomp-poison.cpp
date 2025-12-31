#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    map<vector<int>, bool> memo;
    vector<vector<int>> poisons;

    bool isValid(int r, int c) {
        for (const auto& p : poisons) {
            if (p[0] >= r && p[1] >= c) return false;
        }
        return true;
    }

    bool canWin(vector<int>& state) {
        if (memo.count(state)) return memo[state];

        int C = state.size();
        bool canReachLosing = false;

        for (int c = 0; c < C; c++) {
            for (int r = 0; r < state[c]; r++) {
                if (isValid(r, c)) {
                    vector<int> nextState = state;
                    for (int i = c; i < C; i++) {
                        nextState[i] = min(nextState[i], r);
                    }
                    if (!canWin(nextState)) {
                        canReachLosing = true;
                        goto end;
                    }
                }
            }
        }
        end:;

        return memo[state] = canReachLosing;
    }

public:
    string chompGame(int R, int C, vector<vector<int>>& poisons) {
        this->poisons = poisons;
        vector<int> initialState(C, R);
        return canWin(initialState) ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int R, C, K;
    if (cin >> R >> C >> K) {
        vector<vector<int>> poisons(K, vector<int>(2));
        for (int i = 0; i < K; i++) {
            cin >> poisons[i][0] >> poisons[i][1];
        }
        
        Solution solution;
        cout << solution.chompGame(R, C, poisons) << "\n";
    }
    return 0;
}
