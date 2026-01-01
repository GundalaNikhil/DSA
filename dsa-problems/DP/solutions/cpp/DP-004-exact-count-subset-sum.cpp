#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

class Solution {
public:
    bool exactCountSubsetSum(const vector<int>& arr, int target, int k) {
        if (k == 0) return target == 0;
        int words = (target >> 6) + 1;
        vector<vector<uint64_t>> bits(k + 1, vector<uint64_t>(words, 0));
        bits[0][0] = 1ULL;

        auto setOr = [&](vector<uint64_t>& dst, const vector<uint64_t>& src) {
            for (int i = 0; i < words; i++) dst[i] |= src[i];
        };

        auto shiftOr = [&](vector<uint64_t>& dst, const vector<uint64_t>& src, int shift) {
            if (shift == 0) { setOr(dst, src); return; }
            int wordShift = shift >> 6;
            int bitShift = shift & 63;
            int maxWord = target >> 6;
            vector<uint64_t> tmp(words, 0);

            for (int i = 0; i <= maxWord; i++) {
                uint64_t val = src[i];
                if (!val) continue;
                int j = i + wordShift;
                if (j > maxWord) continue;
                tmp[j] |= (val << bitShift);
                if (bitShift != 0 && j + 1 <= maxWord) tmp[j + 1] |= (val >> (64 - bitShift));
            }

            int lastBits = target & 63;
            if (lastBits != 63) {
                uint64_t mask = (1ULL << (lastBits + 1)) - 1ULL;
                tmp[maxWord] &= mask;
            }
            setOr(dst, tmp);
        };

        for (int x : arr) {
            for (int cnt = k; cnt >= 1; cnt--) shiftOr(bits[cnt], bits[cnt - 1], x);
        }

        int w = target >> 6, b = target & 63;
        return ((bits[k][w] >> b) & 1ULL) != 0ULL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target, k;
    cin >> n >> target >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution sol;
    cout << (sol.exactCountSubsetSum(arr, target, k) ? "true" : "false") << '\n';
    return 0;
}
