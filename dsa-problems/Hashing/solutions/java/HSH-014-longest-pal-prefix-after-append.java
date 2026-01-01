import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;

    public int longestPalindromicPrefix(String s, char c) {
        String T = s + c;
        int n = T.length();

        long fwdHash = 0;
        long revHash = 0;
        long power = 1;

        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            char val = T.charAt(i);

            fwdHash = (fwdHash * BASE + val) % MOD;
            revHash = (revHash + val * power) % MOD;

            if (fwdHash == revHash) {
                maxLen = i + 1;
            }

            power = (power * BASE) % MOD;
        }

        return maxLen;
    }
}

class Main {
    public static void main(String[] args) {
        try {
            byte[] bytes = System.in.readAllBytes();
            if (bytes.length == 0) return;
            String data = new String(bytes);
            String[] raw = data.split("\\n", -1);
            for (int i = 0; i < raw.length; i++) {
                if (raw[i].endsWith("\\r")) {
                    raw[i] = raw[i].substring(0, raw[i].length() - 1);
                }
            }
            String s;
            String cstr = "";
            if (raw.length == 1) {
                s = "";
                cstr = raw[0];
            } else {
                s = raw[0];
                for (int i = 1; i < raw.length; i++) {
                    if (!raw[i].isEmpty()) {
                        cstr = raw[i];
                        break;
                    }
                }
                if (cstr.isEmpty()) cstr = raw[1];
            }
            if (cstr.isEmpty()) return;
            char c = cstr.charAt(0);
            Solution solution = new Solution();
            System.out.println(solution.longestPalindromicPrefix(s, c));
        } catch (Exception e) {
            return;
        }
    }
}
