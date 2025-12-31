#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* alternatingReverse(ListNode* head, int l, int k) {
        if (!head || k <= 1) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move to l-1
        for (int i = 0; i < l - 1; i++) {
            if (!prev->next) return head;
            prev = prev->next;
        }

        bool reverse = true;
        while (prev->next) {
            if (reverse) {
                ListNode* tail = prev->next;
                ListNode* curr = tail->next;
                int count = 1;
                while (curr && count < k) {
                    ListNode* temp = curr->next;
                    curr->next = prev->next;
                    prev->next = curr;
                    tail->next = temp;
                    curr = temp;
                    count++;
                }
                prev = tail;
            } else {
                int count = 0;
                while (prev->next && count < k) {
                    prev = prev->next;
                    count++;
                }
            }
            reverse = !reverse;
        }
        return dummy.next;
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
    
    int l, k;
    cin >> l >> k;

    Solution solution;
    ListNode* res = solution.alternatingReverse(dummy.next, l, k);
    
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
