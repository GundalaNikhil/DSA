#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* stablePartition(ListNode* head, int x) {
        ListNode lessHead(0), equalHead(0), greaterHead(0);
        ListNode *less = &lessHead, *equal = &equalHead, *greater = &greaterHead;
        
        ListNode* curr = head;
        while (curr) {
            if (curr->val < x) {
                less->next = curr;
                less = less->next;
            } else if (curr->val == x) {
                equal->next = curr;
                equal = equal->next;
            } else {
                greater->next = curr;
                greater = greater->next;
            }
            curr = curr->next;
        }
        
        greater->next = nullptr;
        equal->next = greaterHead.next;
        less->next = equalHead.next ? equalHead.next : greaterHead.next;
        
        return lessHead.next;
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
    int x;
    cin >> x;

    Solution solution;
    ListNode* res = solution.stablePartition(dummy.next, x);
    
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
