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
    bool canBePalindrome(ListNode* head) {
        vector<int> vals;
        while (head) {
            vals.push_back(head->val);
            head = head->next;
        }

        int left = 0;
        int right = vals.size() - 1;

        while (left < right) {
            if (vals[left] != vals[right]) {
                return isPalindrome(vals, left + 1, right) || 
                       isPalindrome(vals, left, right - 1);
            }
            left++;
            right--;
        }
        return true;
    }

private:
    bool isPalindrome(const vector<int>& vals, int left, int right) {
        while (left < right) {
            if (vals[left] != vals[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
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
    cout << (solution.canBePalindrome(dummy.next) ? "true" : "false") << "\n";
    return 0;
}
