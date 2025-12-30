import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode deduplicateAtMostTwo(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode prev = head;
        ListNode current = head.next;
        int count = 1;

        while (current != null) {
            if (current.val == prev.val) {
                count++;
                if (count > 2) {
                    // Remove current
                    prev.next = current.next;
                    current = current.next; // Move to next node without advancing prev
                } else {
                    // Keep current
                    prev = current;
                    current = current.next;
                }
            } else {
                // New value found
                count = 1;
                prev = current;
                current = current.next;
            }
        }
        return head;
    }
}

public class Main {
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

        Solution solution = new Solution();
        ListNode res = solution.deduplicateAtMostTwo(dummy.next);
        
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
