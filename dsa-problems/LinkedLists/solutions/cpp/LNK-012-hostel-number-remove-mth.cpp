#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* removeMth(ListNode* head, int M) {
        if (M <= 0) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* curr = &dummy;

        for (int i = 0; i < M - 1; i++) {
            if (!curr) return head;
            curr = curr->next;
        }

        if (curr && curr->next) {
            ListNode* toDelete = curr->next;
            curr->next = curr->next->next;
            delete toDelete; // Good practice in C++
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
    int M;
    cin >> M;

    Solution solution;
    ListNode* res = solution.removeMth(dummy.next, M);
    
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
