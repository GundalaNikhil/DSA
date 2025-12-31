import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode alternatingReverse(ListNode head, int l, int k) {
        if (head == null || k <= 1) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        // Move to the starting position l
        for (int i = 0; i < l - 1; i++) {
            if (prev.next == null) return head;
            prev = prev.next;
        }

        boolean reverse = true;
        while (prev.next != null) {
            if (reverse) {
                // Reverse next k nodes
                ListNode tail = prev.next;
                ListNode curr = prev.next.next;
                int count = 1;
                while (curr != null && count < k) {
                    ListNode temp = curr.next;
                    curr.next = prev.next;
                    prev.next = curr;
                    tail.next = temp;
                    curr = temp;
                    count++;
                }
                prev = tail; // Move prev to the end of the reversed block
            } else {
                // Skip next k nodes
                int count = 0;
                while (prev.next != null && count < k) {
                    prev = prev.next;
                    count++;
                }
            }
            reverse = !reverse; // Toggle mode
        }

        return dummy.next;
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
        
        int l = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.alternatingReverse(dummy.next, l, k);
        
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
