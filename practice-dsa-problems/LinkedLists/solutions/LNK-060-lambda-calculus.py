import sys
class Term:
    pass
class Var(Term):
    def __init__(self, name): self.name = name
    def __repr__(self): return self.name
class Abs(Term):
    def __init__(self, var, body): self.var = var; self.body = body
    def __repr__(self): return f"( L{self.var} . {self.body} )"
class App(Term):
    def __init__(self, left, right): self.left = left; self.right = right
    def __repr__(self): return f"{self.left} {self.right}"
def parse(tokens):
    def parse_expr(idx):
        if idx >= len(tokens):
            return None, idx
            
        if tokens[idx] == '(':
            if idx + 1 < len(tokens) and tokens[idx + 1].startswith('L'):
                var = tokens[idx + 1][1:]
                # Expecting ( L<var> . <body> )
                # tokens: '(', 'Lvar', '.', body..., ')'
                # idx:     0     1      2     3...
                body, next_idx = parse_expr(idx + 3)
                # After body, expect ')'
                return Abs(var, body), next_idx + 1
            else:
                # App: ( left right ) ?
                # The provided code had complex logic. Let's simplify or fix indentation.
                # Original logic:
                # if tokens[idx] == '(': ...
                # else: ...
                
                # Parsing lambda calculus usually:
                # Term ::= Var | L<var> . Term | Term Term
                # The provided parser seems to handle parentheses.
                
                # Let's fix the specific indentation error first.
                pass
        
        # Based on original LNK-060 logic structure which was broken:
        if tokens[idx] == '(':
            if idx + 1 < len(tokens) and tokens[idx + 1].startswith('L'):
                var = tokens[idx + 1][1:]
                body, next_idx = parse_expr(idx + 3) # Skipping '(', 'Lvar', '.'
                return Abs(var, body), next_idx + 1 # Skip ')'
            else:
                # ( Term Term ... ) ? No, simplified parser usually.
                # Recursive descent for application?
                # The original code:
                # else:
                #    left, next_idx = parse_expr(idx + 1)
                #    if next_idx < len(tokens) and tokens[next_idx] != ')':
                #       right, final_idx = parse_expr(next_idx)
                #       return App(left, right), final_idx + 1
                #    return left, next_idx + 1
                
                left, next_idx = parse_expr(idx + 1) # Parse inside parens
                if next_idx < len(tokens) and tokens[next_idx] != ')':
                    right, final_idx = parse_expr(next_idx)
                    return App(left, right), final_idx + 1
                return left, next_idx + 1
        else:
            return Var(tokens[idx]), idx + 1

    expr, idx = parse_expr(0)
    # If there are more tokens, assume they are applications to the left expression?
    # Or just return the first parsed expression.
    # The original loop:
    # while idx < len(tokens):
    #    right, idx = parse_expr(idx)
    #    expr = App(expr, right)
    
    while idx < len(tokens) and tokens[idx] != ')':
        right, idx = parse_expr(idx)
        expr = App(expr, right)
        
    return expr

def substitute(term, var, arg):
    if isinstance(term, Var):
        return arg if term.name == var else term
    if isinstance(term, Abs):
        if term.var == var:
            return term
        return Abs(term.var, substitute(term.body, var, arg))
    if isinstance(term, App):
        return App(substitute(term.left, var, arg), substitute(term.right, var, arg))

def reduce_step(term):
    if isinstance(term, App):
        if isinstance(term.left, Abs):
            return substitute(term.left.body, term.left.var, term.right), True
        new_left, changed = reduce_step(term.left)
        if changed:
            return App(new_left, term.right), True
        new_right, changed = reduce_step(term.right)
        if changed:
            return App(term.left, new_right), True
    if isinstance(term, Abs):
        new_body, changed = reduce_step(term.body)
        if changed:
            return Abs(term.var, new_body), True
    return term, False

def flatten(term):
    if isinstance(term, Var):
        return [term.name]
    if isinstance(term, Abs):
        return ['(', f"L{term.var}", '.', *flatten(term.body), ')']
    if isinstance(term, App):
        l = flatten(term.left)
        r = flatten(term.right)
        if isinstance(term.left, Abs):
            l = ['(', *l, ')']
        if isinstance(term.right, App) or isinstance(term.right, Abs):
            r = ['(', *r, ')']
        return l + r

def solve():
    # Use sys.stdin.read().split() for consistent handling, 
    # but tokens need to be preserved.
    # The original tokenization:
    # tokens = str(new_ast).replace('(', ' ( ').replace(')', ' ) ').replace('.', ' . ').split()
    # But for input reading:
    # k = int(line1.strip())
    # tokens = sys.stdin.readline().split()
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    ptr = 0
    if ptr < len(input_data):
        k = int(input_data[ptr])
        ptr += 1
    else:
        return
        
    curr_tokens = input_data[ptr:]
    
    for _ in range(k):
        changed = False
        try:
            ast = parse(curr_tokens)
            new_ast, changed = reduce_step(ast)
            if not changed:
                break
                
            # Flatten AST back to tokens
            curr_tokens = flatten(new_ast)
            
        except BaseException:
            break
            
    print(*(curr_tokens))

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    solve()