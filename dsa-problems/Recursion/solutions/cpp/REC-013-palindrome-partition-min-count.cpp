#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
    int N;
    int L;
    string S;
    vector<vector<bool>> is_pal;
    vector<int> min_count;
    vector<string> best_partition;
    int current_min;

public:
    string minPalindromePartitions(string s, int l) {
        S = s;
        L = l;
        N = s.length();
        
        // Precompute Palindromes
        is_pal.assign(N, vector<bool>(N, false));
        for (int len = 1; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1;
                if (S[i] == S[j]) {
                    if (len <= 2 || is_pal[i + 1][j - 1]) {
                        is_pal[i][j] = true;
                    }
                }
            }
        }

        current_min = N + 1;
        best_partition.clear();
        vector<string> current;
        backtrack(0, current);
        
        if(best_partition.empty()) {
            string res = "";
            for(int i=0; i<N; i++) {
                res += S[i];
                if(i < N-1) res += " ";
            }
            return res;
        }
        
        string res = "";
        for(size_t i=0; i<best_partition.size(); i++) {
            res += best_partition[i];
            if(i < best_partition.size()-1) res += " ";
        }
        return res;
    }

    void backtrack(int start, vector<string>& current) {
        if (start == N) {
            int count = current.size();
            if (count < current_min) {
                current_min = count;
                best_partition = current;
            }
            return;
        }

        // Pruning
        if (current.size() >= current_min) return;

        // Try palindromes length 1 to L
        // Python: range(start, min(start + L, n)) -> end from start to ...
        // Logic: start to end. Length = end - start + 1.
        // Python calls: start:end+1
        int max_end = min(start + L, N);
        for (int end = start; end < max_end; end++) {
            if (is_pal[start][end]) {
                current.push_back(S.substr(start, end - start + 1));
                backtrack(end + 1, current);
                if (current_min == (int)best_partition.size() && !best_partition.empty()) {
                     // Optimization: if we found best, do we stop? 
                     // Python loop continues but backtrack prunes.
                     // Python logic: if we found BETTER, Update.
                     // If we found SAME, Python keeps first found? 
                     // Python: if count < min: update. if count == min: append.
                     // Python returns all_partitions[0].
                     // To match Python traversal order, we just update if count < current_min.
                     // If count == current_min, we ignore (Keep first found).
                }
                current.pop_back();
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    int L; cin >> L;
    
    Solution sol;
    cout << sol.minPalindromePartitions(s, L) << endl;
    return 0;
}
