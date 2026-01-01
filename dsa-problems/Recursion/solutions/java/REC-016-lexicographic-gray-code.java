import java.util.*;

class Solution {
    public List<String> grayCode(int n) {
        if (n == 0) return new ArrayList<>(Arrays.asList("0")); // Edge case if n=0 allowed
        if (n == 1) return new ArrayList<>(Arrays.asList("0", "1"));
        
        List<String> prev = grayCode(n - 1);
        List<String> result = new ArrayList<>();
        
        // Prefix 0
        for (String s : prev) {
            result.add("0" + s);
        }
        
        // Prefix 1 to reversed
        for (int i = prev.size() - 1; i >= 0; i--) {
            result.add("1" + prev.get(i));
        }
        
        return result;
    }
}





class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Solution sol = new Solution();
        List<String> res = sol.grayCode(n);
        for(String out_s : res) System.out.println(out_s);
        if(res.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
