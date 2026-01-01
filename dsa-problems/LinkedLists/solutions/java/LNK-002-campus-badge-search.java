import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public int findFirstIndex(ListNode head, int target) {
        ListNode current = head;
        int index = 0;
        
        while (current != null) {
            if (current.val == target) {
                return index;
            }
            current = current.next;
            index++;
        }
        
        return -1;
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
        
        int target = sc.nextInt();
        Solution solution = new Solution();
        System.out.println(solution.findFirstIndex(dummy.next, target));
        sc.close();
    }
}
