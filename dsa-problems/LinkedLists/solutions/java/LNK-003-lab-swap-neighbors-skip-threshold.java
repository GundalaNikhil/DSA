import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Result {
    ListNode head;
    int swaps;
    Result(ListNode head, int swaps) {
        this.head = head;
        this.swaps = swaps;
    }
}

class Solution {
    public Result swapWithSkip(ListNode head, int K) {
        if (head == null || head.next == null) {
            return new Result(head, 0);
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int swapCount = 0;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Check conditions
            boolean nonNegative = (first.val >= 0 && second.val >= 0);
            boolean canSwap = (K > 0);

            if (nonNegative && canSwap) {
                // Perform swap
                prev.next = second;
                first.next = second.next;
                second.next = first;

                // Update state
                K--;
                swapCount++;
                prev = first; // first is now the 2nd node in the pair
            } else {
                // Skip pair
                prev = second; // second is the 2nd node in the unswapped pair
            }
        }

        return new Result(dummy.next, swapCount);
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
        int K = sc.nextInt();

        Solution solution = new Solution();
        Result res = solution.swapWithSkip(dummy.next, K);
        ListNode out = res.head;
        while (out != null) {
            System.out.print(out.val + (out.next != null ? " " : ""));
            out = out.next;
        }
        System.out.println();
        System.out.println(res.swaps);
        sc.close();
    }
}
