#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    int upperBound(const vector<int>& arr, long long val) {
        int l = 0, r = arr.size() - 1;
        int res = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= val) {
                res = mid + 1;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }

    long long countLessEqual(const vector<int>& A, const vector<int>& B, long long wA, long long wB, long long val) {
        long long count = 0;
        count += (long long)upperBound(A, val) * wA;
        count += (long long)upperBound(B, val) * wB;
        return count;
    }

    long long findKth(const vector<int>& A, const vector<int>& B, long long wA, long long wB, long long k) {
        long long low = -2000000000LL;
        long long high = 2000000000LL;
        long long ans = high;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (countLessEqual(A, B, wA, wB, mid) > k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

public:
    string weightedMedian(const vector<int>& A, const vector<int>& B, long long wA, long long wB) {
        long long n = A.size();
        long long m = B.size();
        long long total = n * wA + m * wB;
        
        if (total % 2 == 1) {
            return to_string(findKth(A, B, wA, wB, total / 2));
        } else {
            long long val1 = findKth(A, B, wA, wB, total / 2 - 1);
            long long val2 = findKth(A, B, wA, wB, total / 2);
            long long sum = val1 + val2;
            if (sum % 2 == 0) {
                return to_string(sum / 2);
            } else {
                return to_string(sum / 2) + ".5";
            }
        }
    }
};
