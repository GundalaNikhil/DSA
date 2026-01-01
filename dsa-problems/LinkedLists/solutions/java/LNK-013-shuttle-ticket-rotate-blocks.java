import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode rotateBlocks(ListNode head, int b, int k) {
        if (head == null || b <= 0) return head;

        ListNode dummy = new ListNode(0);
        ListNode prevTail = dummy;
        ListNode curr = head;

        while (curr != null) {
            // 1. Identify block start and end
            ListNode blockHead = curr;
            ListNode blockTail = curr;
            int len = 1;
            
            // Move b-1 steps to find tail of block
            for (int i = 0; i < b - 1 && blockTail.next != null; i++) {
                blockTail = blockTail.next;
                len++;
            }
            
            // 2. Detach
            ListNode nextBlockHead = blockTail.next;
            blockTail.next = null; // Cut
            
            // 3. Rotate
            ListNode[] rotated = rotateList(blockHead, len, k);
            
            // 4. Attach
            prevTail.next = rotated[0]; // New head
            prevTail = rotated[1];      // New tail
            
            // 5. Advance
            curr = nextBlockHead;
        }

        return dummy.next;
    }

    // Returns [newHead, newTail]
    private ListNode[] rotateList(ListNode head, int len, int k) {
        if (len <= 1 || k % len == 0) {
            // Find tail
            ListNode tail = head;
            while (tail.next != null) tail = tail.next;
            return new ListNode[]{head, tail};
        }

        k = k % len;
        int moves = len - k; // Moves to new tail

        ListNode newTail = head;
        for (int i = 0; i < moves - 1; i++) {
            newTail = newTail.next;
        }
        
        ListNode newHead = newTail.next;
        newTail.next = null; // Break ring
        
        // Find end of newHead to link to old head? 
        // 1->2->3, k=1. len=3. moves=2.
        // newTail = 2. newHead = 3.
        // 3->null. Need 3->1->2.
        
        ListNode temp = newHead;
        while (temp.next != null) temp = temp.next;
        temp.next = head; // Link end to start
        
        return new ListNode[]{newHead, newTail};
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
        int b = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.rotateBlocks(dummy.next, b, k);
        
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
