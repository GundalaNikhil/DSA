#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

struct Result {
    ListNode* head;
    int reversedGroups;
    long long sum;
};

class Solution {
public:
    Result reverseFromOffset(ListNode* head, int k, int s) {
        if (!head || k <= 1) return {head, 0, 0};

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move to s-1
        for (int i = 0; i < s - 1; i++) {
            if (!prev->next) return {head, 0, 0};
            prev = prev->next;
        }

        int groups = 0;
        long long totalSum = 0;

        while (true) {
            // Probe
            ListNode* probe = prev;
            for (int i = 0; i < k; i++) {
                probe = probe->next;
                if (!probe) return {dummy.next, groups, totalSum};
            }

            // Reverse
            ListNode* tail = prev->next;
            ListNode* curr = tail->next;
            long long groupSum = tail->val;

            for (int i = 1; i < k; i++) {
                groupSum += curr->val;
                ListNode* temp = curr->next;
                curr->next = prev->next;
                prev->next = curr;
                tail->next = temp;
                curr = temp;
            }

            groups++;
            totalSum += groupSum;
            prev = tail;
        }
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
    
    int k, s;
    cin >> k >> s;

    Solution solution;
    Result res = solution.reverseFromOffset(dummy.next, k, s);
    
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n" << res.reversedGroups << "\n" << res.sum << "\n";
    return 0;
}
