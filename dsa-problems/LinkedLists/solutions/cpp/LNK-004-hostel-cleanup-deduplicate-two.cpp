#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* deduplicateAtMostTwo(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* prev = head;
        ListNode* current = head->next;
        int count = 1;

        while (current != nullptr) {
            if (current->val == prev->val) {
                count++;
                if (count > 2) {
                    // Remove current
                    prev->next = current->next;
                    // Delete current if memory management is required, 
                    // but for competitive programming we often just skip.
                    // delete current; 
                    current = prev->next;
                } else {
                    prev = current;
                    current = current->next;
                }
            } else {
                count = 1;
                prev = current;
                current = current->next;
            }
        }
        return head;
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
    ListNode* res = solution.deduplicateAtMostTwo(dummy.next);
    
    bool first = true;
    while (res) {
        if (!first) cout << " ";
        cout << res->val;
        first = false;
        res = res->next;
    }
    cout << "\n";
    return 0;
}
