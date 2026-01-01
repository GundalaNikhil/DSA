#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    long long minInversionsAfterSwap(const vector<int>& arr) {
        int n = arr.size();
        long long best = countInversions(arr);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                vector<int> temp = arr;
                swap(temp[i], temp[j]);
                long long inv = countInversions(temp);
                if (inv < best) {
                    best = inv;
                }
            }
        }

        return best;
    }

private:
    long long countInversions(vector<int> arr) {
        if (arr.empty()) {
            return 0;
        }
        vector<int> temp(arr.size());
        return mergeSort(arr, temp, 0, (int)arr.size() - 1);
    }

    long long mergeSort(vector<int>& arr, vector<int>& temp, int left, int right) {
        if (left >= right) {
            return 0;
        }
        int mid = left + (right - left) / 2;
        long long inv = mergeSort(arr, temp, left, mid);
        inv += mergeSort(arr, temp, mid + 1, right);
        inv += merge(arr, temp, left, mid, right);
        return inv;
    }

    long long merge(vector<int>& arr, vector<int>& temp, int left, int mid, int right) {
        int i = left;
        int j = mid + 1;
        int k = left;
        long long inv = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                inv += (mid - i + 1);
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (i = left; i <= right; i++) {
            arr[i] = temp[i];
        }

        return inv;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.minInversionsAfterSwap(arr) << "\n";
    return 0;
}
