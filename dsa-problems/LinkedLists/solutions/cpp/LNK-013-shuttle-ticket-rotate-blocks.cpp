#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* rotateBlocks(ListNode* head, int b, int k) {
        if (!head || b <= 0) return head;

        ListNode dummy(0);
        ListNode* prevTail = &dummy;
        ListNode* curr = head;

        while (curr) {
            ListNode* blockHead = curr;
            ListNode* blockTail = curr;
            int len = 1;

            for (int i = 0; i < b - 1 && blockTail->next; i++) {
                blockTail = blockTail->next;
                len++;
            }

            ListNode* nextBlockHead = blockTail->next;
            blockTail->next = nullptr;

            pair<ListNode*, ListNode*> rotated = rotateList(blockHead, len, k);
            
            prevTail->next = rotated.first;
            prevTail = rotated.second;

            curr = nextBlockHead;
        }

        return dummy.next;
    }

private:
    pair<ListNode*, ListNode*> rotateList(ListNode* head, int len, int k) {
        if (len <= 1 || k % len == 0) {
            ListNode* tail = head;
            while (tail->next) tail = tail->next;
            return {head, tail};
        }

        k %= len;
        int moves = len - k;

        ListNode* newTail = head;
        for (int i = 0; i < moves - 1; i++) {
            newTail = newTail->next;
        }

        ListNode* newHead = newTail->next;
        newTail->next = nullptr;

        ListNode* temp = newHead;
        while (temp->next) temp = temp->next;
        temp->next = head;

        return {newHead, newTail};
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
    int b, k;
    cin >> b >> k;

    Solution solution;
    ListNode* res = solution.rotateBlocks(dummy.next, b, k);
    
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
