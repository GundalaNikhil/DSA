import java.util.*;

class Solution {
    public List<Integer> findSubset(List<Integer> arr, int k, int target) {
        List<Integer> current = new ArrayList<>();
        if (backtrack(0, 0, 0, arr, k, target, current)) {
            return current;
        }
        return new ArrayList<>();
    }

    private boolean backtrack(int index, int count, int currentSum, List<Integer> arr, int k, int target, List<Integer> current) {
        if (count == k) {
            return currentSum == target;
        }
        if (index == arr.size()) {
            return false;
        }
        
        // Pruning
        if (arr.size() - index < k - count) {
            return false;
        }

        // Option 1: Include
        current.add(arr.get(index));
        if (backtrack(index + 1, count + 1, currentSum + arr.get(index), arr, k, target, current)) {
            return true;
        }
        current.remove(current.size() - 1);

        // Option 2: Exclude
        if (backtrack(index + 1, count, currentSum, arr, k, target, current)) {
            return true;
        }

        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int target = sc.nextInt();
        
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++) {
             if(sc.hasNextInt()) arr.add(sc.nextInt());
        }
        
        Solution sol = new Solution();
        List<Integer> res = sol.findSubset(arr, k, target);
        if(res.isEmpty()) {
            System.out.println("NONE");
        } else {
            for(int i=0; i<res.size(); i++) System.out.print(res.get(i) + (i==res.size()-1?"":" "));
            System.out.println();
        }
        sc.close();
    }
}
