def solve(expr: str) -> str:
    postfix = []
    ops = []
    redundant = 0
    
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '(': 0}
    
    # 0: Start, 1: Operand, 2: Operator, 3: Open, 4: Close
    last_type = 0
    
    for c in expr:
        if c.isalnum():
            if last_type == 1 or last_type == 4:
                return "ERROR Invalid syntax 0"
            postfix.append(c)
            last_type = 1
        elif c == '(':
            if last_type == 1 or last_type == 4:
                return "ERROR Invalid syntax 0"
            ops.append(c)
            last_type = 3
        elif c == ')':
            if last_type == 0 or last_type == 2 or last_type == 3:
                return "ERROR Invalid syntax 0"
            
            has_op = False
            while ops and ops[-1] != '(':
                postfix.append(ops.pop())
                has_op = True
            
            if not ops:
                return "ERROR Mismatched parentheses 0"
            ops.pop() # Pop '('
            
            if not has_op:
                redundant += 1
            
            last_type = 4
        elif c in prec:
            if last_type == 0 or last_type == 2 or last_type == 3:
                return "ERROR Invalid syntax 0"
            
            while ops and ops[-1] != '(' and \
                  (prec[ops[-1]] > prec[c] or \
                  (prec[ops[-1]] == prec[c] and c != '^')):
                postfix.append(ops.pop())
            ops.append(c)
            last_type = 2
        else:
            return "ERROR Invalid character 0"
            
    if last_type == 0 or last_type == 2 or last_type == 3:
        return "ERROR Invalid syntax 0"
        
    while ops:
        if ops[-1] == '(':
            return "ERROR Mismatched parentheses 0"
        postfix.append(ops.pop())
        
    return f"POSTFIX {''.join(postfix)} {redundant}"


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
