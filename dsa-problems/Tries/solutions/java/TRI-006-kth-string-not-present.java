import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Read all tokens
        int n = sc.nextInt();
        int L = sc.nextInt();
        int k = sc.nextInt();
        
        Set<String> inserted = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (sc.hasNext()) {
                inserted.add(sc.next());
            }
        }
        
        List<String> allStrings = new ArrayList<>();
        
        // Order: a, aa, ab, ..., az, b, ba, bb, ..., bz, c, ...
        for (char c = 'a'; c <= 'z'; c++) {
            // Add single character if not inserted and L >= 1
            if (L >= 1 && !inserted.contains(String.valueOf(c))) {
                allStrings.add(String.valueOf(c));
            }
            
            // Add all multi-char strings starting with this char
            for (int length = 2; length <= L; length++) {
                generateCombinations(String.valueOf(c), length - 1, inserted, allStrings);
            }
        }
        
        System.out.println(k <= allStrings.size() ? allStrings.get(k - 1) : "");
        sc.close();
    }
    
    static void generateCombinations(String prefix, int remaining, Set<String> inserted, List<String> result) {
        if (remaining == 0) {
            if (!inserted.contains(prefix)) {
                result.add(prefix);
            }
            return;
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            generateCombinations(prefix + c, remaining - 1, inserted, result);
        }
    }
}
