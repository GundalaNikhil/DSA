import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int L = sc.nextInt();
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int minXor = Integer.MAX_VALUE;
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xorVal = arr[i] ^ arr[j];
                if (xorVal <= L) {
                    minXor = Math.min(minXor, xorVal);
                }
            }
        }
        
        System.out.println(minXor == Integer.MAX_VALUE ? -1 : minXor);
        sc.close();
    }
}
