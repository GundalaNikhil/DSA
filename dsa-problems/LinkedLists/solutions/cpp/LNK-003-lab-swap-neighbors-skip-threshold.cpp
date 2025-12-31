#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

struct Result {
    ListNode* head;
    int swaps;
};

class Solution {
public:
    Result swapWithSkip(ListNode* head, int K) {
        if (!head || !head->next) return {head, 0};

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        int swapCount = 0;

        while (prev->next && prev->next->next) {
            ListNode* first = prev->next;
            ListNode* second = prev->next->next;

            bool nonNegative = (first->val >= 0 && second->val >= 0);
            bool canSwap = (K > 0);

            if (nonNegative && canSwap) {
                prev->next = second;
                first->next = second->next;
                second->next = first;

                K--;
                swapCount++;
                prev = first;
            } else {
                prev = second;
            }
        }
        return {dummy.next, swapCount};
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
    
    int K;
    cin >> K;

    Solution solution;
    Result res = solution.swapWithSkip(dummy.next, K);
    
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n";
    cout << res.swaps << "\n";
    return 0;
}
