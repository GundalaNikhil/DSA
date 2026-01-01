import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode stablePartition(ListNode head, int x) {
        ListNode lessHead = new ListNode(0);
        ListNode equalHead = new ListNode(0);
        ListNode greaterHead = new ListNode(0);
        
        ListNode less = lessHead;
        ListNode equal = equalHead;
        ListNode greater = greaterHead;
        
        ListNode curr = head;
        while (curr != null) {
            if (curr.val < x) {
                less.next = curr;
                less = less.next;
            } else if (curr.val == x) {
                equal.next = curr;
                equal = equal.next;
            } else {
                greater.next = curr;
                greater = greater.next;
            }
            curr = curr.next;
        }
        
        // Connect lists
        greater.next = null; // Terminate the end
        equal.next = greaterHead.next; // Equal -> Greater
        less.next = equalHead.next != null ? equalHead.next : greaterHead.next; // Less -> (Equal or Greater)
        
        return lessHead.next;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int i = 0; i < n; i++) {
            cur.next = new ListNode(sc.nextInt());
            cur = cur.next;
        }
        int x = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.stablePartition(dummy.next, x);
        
        boolean first = true;
        while (res != null) {
            if (!first) System.out.print(" ");
            System.out.print(res.val);
            first = false;
            res = res.next;
        }
        System.out.println();
        sc.close();
    }
}
