import sys
class Op:
    def __init__(self, type, pos, val=None):
        self.type = type
        self.pos = pos
        self.val = val
def transform(b, a):
    if not b:
        return None
    if a.type == 'INS' and b.type == 'INS':
        if a.pos < b.pos:
            return Op('INS', b.pos + 1, b.val)
        elif a.pos == b.pos:
            return Op('INS', b.pos + 1, b.val)
        else:
            return b
    elif a.type == 'INS' and b.type == 'DEL':
        if a.pos <= b.pos:
            return Op('DEL', b.pos + 1)
        else:
            return b
    elif a.type == 'DEL' and b.type == 'INS':
        if a.pos < b.pos:
            return Op('INS', b.pos - 1, b.val)
        else:
            return b
    elif a.type == 'DEL' and b.type == 'DEL':
        if a.pos < b.pos:
            return Op('DEL', b.pos - 1)
        elif a.pos == b.pos:
            return None
        else:
            return b
    return b
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    lst = []
    for _ in range(n):
        lst.append(int(input_data[ptr]))
        ptr += 1
        
    qa_count = int(input_data[ptr])
    ptr += 1
    qb_count = int(input_data[ptr])
    ptr += 1
    
    ops_a = []
    for _ in range(qa_count):
        tp = input_data[ptr]
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        val = None
        if tp == 'INS':
            val = int(input_data[ptr])
            ptr += 1
        ops_a.append(Op(tp, pos, val))
        
    ops_b = []
    for _ in range(qb_count):
        tp = input_data[ptr]
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        val = None
        if tp == 'INS':
            val = int(input_data[ptr])
            ptr += 1
        ops_b.append(Op(tp, pos, val))
        
    transformed_b = []
    for ob in ops_b:
        curr_ob = ob
        for oa in ops_a:
            if curr_ob:
                curr_ob = transform(curr_ob, oa)
        if curr_ob:
            transformed_b.append(curr_ob)
            
    final_ops = ops_a + transformed_b
    for op in final_ops:
        if op.type == 'INS':
            lst.insert(op.pos - 1, op.val)
        else:
            if 1 <= op.pos <= len(lst):
                lst.pop(op.pos - 1)
                
    print(*(lst))
if __name__ == '__main__':
    solve()