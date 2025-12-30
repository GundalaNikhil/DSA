def eval_postfix(tokens: list[str], vars: dict[str, int]) -> int:
    stack = []
    MOD = 1000000007
    
    for token in tokens:
        if token in vars:
            stack.append(vars[token] % MOD)
        elif token.lstrip("-").isdigit(): # Handle negative numbers
            stack.append(int(token) % MOD)
        elif token == "DUP":
            stack.append(stack[-1])
        elif token == "SWAP":
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        else:
            b = stack.pop()
            a = stack.pop()
            res = 0
            
            if token == "+":
                res = (a + b) % MOD
            elif token == "-":
                res = (a - b + MOD) % MOD
            elif token == "*":
                res = (a * b) % MOD
            elif token == "/":
                res = a // b # Integer division
            elif token == "%":
                res = a % b
            
            stack.append(res)
            
    return stack[-1]


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
