#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> kthSmallestInWindows(const vector<int>& arr, int w, int k) {
        // In C++, we can use multiset which supports deletion!
        // This simplifies things immensely compared to Java/Python heaps.
        // O(N log W)
        
        multiset<int> window;
        vector<int> result;
        
        // Optimization: Maintain an iterator to the k-th element?
        // Yes, "Moving Iterator" technique.
        // O(N) if we just move iterator, but insertion is O(log W).
        
        auto mid = window.begin(); // Points to k-th element (0-indexed k-1)
        
        for (int i = 0; i < arr.size(); i++) {
            window.insert(arr[i]);
            
            if (i < w) {
                // Initial build
                if (window.size() == k) {
                    mid = prev(window.end());
                } else if (window.size() > k) {
                    if (arr[i] < *mid) mid--;
                }
            } else {
                // Slide
                int out = arr[i - w];
                int in = arr[i];
                
                // Insert logic relative to mid
                if (in < *mid) mid--;
                
                // Remove logic
                // Be careful: mid can be invalidated if we erase it
                auto it = window.lower_bound(out); // Find ONE instance
                // If duplicates, any instance works, but we must be careful if it is mid
                
                if (it == mid) {
                    // We are removing the element mid points to.
                    // We need to shift mid.
                    // If we remove mid, the next element becomes the new k-th?
                    // So mid should move to next.
                    auto next_it = next(mid);
                    window.erase(it);
                    mid = next_it;
                } else {
                    if (*it < *mid) {
                        // Removed from left of mid, mid shifts right (to larger)
                        window.erase(it);
                        mid++;
                    } else {
                        // Removed from right of mid, mid stays (relative index same)
                        window.erase(it);
                    }
                }
            }
            
            if (i >= w - 1) {
                // Adjust mid to be exactly k-th
                // Due to insert/remove, mid can be off by 1
                // Rely on `advance` for safety in the medium solution.
                // No, O(K) is too slow.
                // Use two multisets L and R to match other languages.
                // L size = k. R size = w-k.
            }
        }
        
        // Re-implementation with Two Multisets for clarity and robustness
        multiset<int> L, R;
        result.clear();
        
        for (int i = 0; i < arr.size(); i++) {
            int val = arr[i];
            
            // ADD
            if (L.empty() || val <= *L.rbegin()) {
                L.insert(val);
            } else {
                R.insert(val);
            }
            
            // REMOVE
            if (i >= w) {
                int out = arr[i - w];
                auto itL = L.find(out);
                if (itL != L.end()) {
                    L.erase(itL);
                } else {
                    auto itR = R.find(out);
                    if (itR != R.end()) R.erase(itR);
                }
            }
            
            // BALANCE
            while (L.size() < k && !R.empty()) {
                L.insert(*R.begin());
                R.erase(R.begin());
            }
            while (L.size() > k) {
                R.insert(*L.rbegin());
                L.erase(prev(L.end()));
            }
            
            if (i >= w - 1) {
                result.push_back(*L.rbegin());
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, w, k;
    if (cin >> n >> w >> k) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        
        Solution solution;
        vector<int> result = solution.kthSmallestInWindows(arr, w, k);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
