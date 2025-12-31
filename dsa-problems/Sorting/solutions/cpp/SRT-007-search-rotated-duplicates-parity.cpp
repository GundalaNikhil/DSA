#include <vector>
#include <iostream>

using namespace std;

class Solution {
    int findPivot(const vector<int>& arr, int low, int high) {
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] > arr[high]) {
                low = mid + 1;
            } else if (arr[mid] < arr[high]) {
                high = mid;
            } else {
                high--;
            }
        }
        return low;
    }

    pair<int, int> searchRange(const vector<int>& arr, int low, int high, int target) {
        int start = -1, end = -1;
        
        int l = low, r = high;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] >= target) {
                if (arr[mid] == target) start = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        if (start == -1) return {-1, -1};
        
        l = low; r = high;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= target) {
                if (arr[mid] == target) end = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return {start, end};
    }

    int countEvens(int L, int R) {
        if (L > R) return 0;
        int len = R - L + 1;
        if (len % 2 == 0) return len / 2;
        return (L % 2 == 0) ? (len + 1) / 2 : (len - 1) / 2;
    }

public:
    int countEvenIndices(const vector<int>& arr, int x) {
        int n = arr.size();
        int pivot = findPivot(arr, 0, n - 1);
        
        int count = 0;
        if (pivot > 0) {
            pair<int, int> range = searchRange(arr, 0, pivot - 1, x);
            if (range.first != -1) {
                count += countEvens(range.first, range.second);
            }
        }
        
        pair<int, int> range = searchRange(arr, pivot, n - 1, x);
        if (range.first != -1) {
            count += countEvens(range.first, range.second);
        }
        
        return count;
    }
};
