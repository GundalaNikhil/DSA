#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    int weightedMiddleValue(ListNode* head) {
        if (!head) return 0;

        // Pass 1: Total weight
        long long totalWeight = 0;
        ListNode* curr = head;
        while (curr) {
            totalWeight += curr->val;
            curr = curr->next;
        }

        long long threshold = (totalWeight + 1) / 2;

        // Pass 2: Find node
        long long currentSum = 0;
        curr = head;
        while (curr) {
            currentSum += curr->val;
            if (currentSum >= threshold) {
                return curr->val;
            }
            curr = curr->next;
        }
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        cur->next = new ListNode(v);
        cur = cur->next;
    }

    Solution solution;
    cout << solution.weightedMiddleValue(dummy.next) << "\n";
    return 0;
}
