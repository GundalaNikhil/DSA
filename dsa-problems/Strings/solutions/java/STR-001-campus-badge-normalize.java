class Solution {
    public String normalizeBadge(String s) {
        if (s == null || s.isEmpty()) return "";

        StringBuilder result = new StringBuilder();
        boolean lastWasAlnum = false;

        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                result.append(Character.toLowerCase(c));
                lastWasAlnum = true;
            } else {
                // Non-alphanumeric character
                if (lastWasAlnum && result.length() > 0) {
                    result.append('-');
                    lastWasAlnum = false;
                }
            }
        }

        // Remove trailing hyphen if present
        if (result.length() > 0 && result.charAt(result.length() - 1) == '-') {
            result.setLength(result.length() - 1);
        }

        return result.toString();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.normalizeBadge(s));
        sc.close();
    }
}
