import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    S_count = int(input_data[ptr])
    ptr += 1
    T_steps = int(input_data[ptr])
    ptr += 1
    tape_str = input_data[ptr]
    ptr += 1
    tape = [int(c) for c in tape_str]
    head_pos = int(input_data[ptr])
    ptr += 1
    m_trans = int(input_data[ptr])
    ptr += 1
    transitions = {}
    for _ in range(m_trans):
        st = int(input_data[ptr])
        ptr += 1
        sym = int(input_data[ptr])
        ptr += 1
        nsym = int(input_data[ptr])
        ptr += 1
        move = input_data[ptr]
        ptr += 1
        nst = int(input_data[ptr])
        ptr += 1
        transitions[(st, sym)] = (nsym, move, nst)
        
    curr_state = 0
    curr_pos = head_pos - 1
    
    for _ in range(T_steps):
        # Check bounds? n size tape?
        # Assuming infinite tape or bounded?
        # Logic checks 0 and n-1 bounds.
        if curr_pos < 0 or curr_pos >= n:
            break
        sym = tape[curr_pos]
        
        if (curr_state, sym) not in transitions:
            break
            
        nsym, move, nst = transitions[(curr_state, sym)]
        tape[curr_pos] = nsym
        curr_state = nst
        
        if move == "L":
            if curr_pos == 0:
                break
            curr_pos -= 1
        else:
            if curr_pos == n - 1:
                break
            curr_pos += 1
            
    print(curr_pos + 1)
    print("".join(map(str, tape)))


if __name__ == "__main__":
    solve()
