import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    private ListNode head = null;
    private ListNode tail = null;

    public void pushBack(int value) {
        ListNode newNode = new ListNode(value);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
    }

    public int[] toArray() {
        List<Integer> list = new ArrayList<>();
        ListNode current = head;
        while (current != null) {
            list.add(current.val);
            current = current.next;
        }
        // Convert List to int[]
        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return arr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        sc.nextLine();

        Solution solution = new Solution();
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine().trim();
            if (line.startsWith("push_back")) {
                String[] parts = line.split(" ");
                int value = Integer.parseInt(parts[1]);
                solution.pushBack(value);
            } else {
                int[] arr = solution.toArray();
                for (int j = 0; j < arr.length; j++) {
                    System.out.print(arr[j]);
                    if (j + 1 < arr.length) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
