#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

class Solution {
public:
    long long huffmanCost(const vector<int>& freq, int m) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        for (int f : freq) {
            pq.push((long long)f);
        }
        
        while ((pq.size() - 1) % (m - 1) != 0) {
            pq.push(0);
        }
        
        long long totalCost = 0;
        
        while (pq.size() > 1) {
            long long sum = 0;
            for (int i = 0; i < m; i++) {
                sum += pq.top();
                pq.pop();
            }
            totalCost += sum;
            pq.push(sum);
        }
        
        return totalCost;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<int> freq(n);
        for (int i = 0; i < n; i++) cin >> freq[i];
        
        Solution solution;
        cout << solution.huffmanCost(freq, m) << "\n";
    }
    return 0;
}
