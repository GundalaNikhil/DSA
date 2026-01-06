import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 28:
        return
    s = input_data[0]
    t = input_data[1]
    weights = [int(x) for x in input_data[2:]]
    if len(s) != len(t):
        print("false")
        return
    s_to_t = {}
    t_to_s = {}
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                print("false")
                return
            else:
                if char_t in t_to_s:
                    print("false")
                    return
                w_s = weights[ord(char_s) - ord("a")]
                w_t = weights[ord(char_t) - ord("a")]
                if w_s != w_t:
                    print("false")
                    return
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s
                
    print("true")


if __name__ == "__main__":
    solve()
