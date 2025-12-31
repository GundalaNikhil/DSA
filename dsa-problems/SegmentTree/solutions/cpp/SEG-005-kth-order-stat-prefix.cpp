#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct Node {
    int count;
    Node *left, *right;
    
    Node(int count, Node* left, Node* right) : count(count), left(left), right(right) {}
};

class Solution {
    vector<Node*> roots;
    vector<int> unique;
    
    Node* build(int l, int r) {
        if (l == r) return new Node(0, nullptr, nullptr);
        int mid = (l + r) / 2;
        return new Node(0, build(l, mid), build(mid + 1, r));
    }
    
    Node* update(Node* node, int l, int r, int idx) {
        if (l == r) {
            return new Node(node->count + 1, nullptr, nullptr);
        }
        int mid = (l + r) / 2;
        Node* left = node->left;
        Node* right = node->right;
        if (idx <= mid) {
            left = update(left, l, mid, idx);
        } else {
            right = update(right, mid + 1, r, idx);
        }
        return new Node(left->count + right->count, left, right);
    }
    
    int query(Node* node, int l, int r, int k) {
        if (l == r) return l;
        int mid = (l + r) / 2;
        int leftCount = node->left->count;
        if (k <= leftCount) {
            return query(node->left, l, mid, k);
        } else {
            return query(node->right, mid + 1, r, k - leftCount);
        }
    }

public:
    vector<int> kthPrefix(const vector<int>& arr, const vector<pair<int,int>>& queries) {
        int n = arr.size();
        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        this->unique = sorted;
        int m = unique.size();
        
        Node* nullRoot = build(0, m - 1);
        roots.clear();
        
        Node* prev = nullRoot;
        for (int x : arr) {
            int idx = lower_bound(unique.begin(), unique.end(), x) - unique.begin();
            Node* curr = update(prev, 0, m - 1, idx);
            roots.push_back(curr);
            prev = curr;
        }
        
        vector<int> results;
        for (const auto& q : queries) {
            int r = q.first;
            int k = q.second;
            int idx = query(roots[r], 0, m - 1, k);
            results.push_back(unique[idx]);
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<pair<int, int>> queries(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // PREFIX
        cin >> queries[i].first >> queries[i].second;
    }
    Solution sol;
    vector<int> results = sol.kthPrefix(arr, queries);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
