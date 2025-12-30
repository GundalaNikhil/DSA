#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    struct Pair {
        int val;
        int idx;
    };
    
    vector<long long> counts;
    
    vector<Pair> mergeSort(vector<Pair>& arr, long long T) {
        int n = arr.size();
        if (n <= 1) return arr;
        
        int mid = n / 2;
        vector<Pair> left(arr.begin(), arr.begin() + mid);
        vector<Pair> right(arr.begin() + mid, arr.end());
        
        left = mergeSort(left, T);
        right = mergeSort(right, T);
        
        // Count step
        int q = 0;
        for (int p = 0; p < left.size(); p++) {
            long long threshold = (long long)left[p].val - T;
            while (q < right.size() && right[q].val < threshold) {
                q++;
            }
            counts[left[p].idx] += (right.size() - q);
        }
        
        // Merge step
        vector<Pair> res;
        res.reserve(n);
        int i = 0, j = 0;
        while (i < left.size() && j < right.size()) {
            if (left[i].val <= right[j].val) {
                res.push_back(left[i++]);
            } else {
                res.push_back(right[j++]);
            }
        }
        while (i < left.size()) res.push_back(left[i++]);
        while (j < right.size()) res.push_back(right[j++]);
        return res;
    }

public:
    vector<long long> countWithinThreshold(const vector<int>& arr, long long T) {
        int n = arr.size();
        counts.assign(n, 0);
        vector<Pair> pairs(n);
        for (int i = 0; i < n; i++) {
            pairs[i] = {arr[i], i};
        }
        
        mergeSort(pairs, T);
        return counts;
    }
};
