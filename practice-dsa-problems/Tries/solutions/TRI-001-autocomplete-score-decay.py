class TrieNode:
    def __init__(self):
        self.children = {}
        self.top_words = []


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    d_percent = int(input_data[ptr])
    ptr += 1
    f = (100.0 - d_percent) / 100.0
    
    root = TrieNode()
    word_v_scores = {}
    
    def update_trie(word, old_v, new_v):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            
            # Update top_words list for this node
            new_list = []
            
            # If word was already in top_words with old_v, remove it (filter it out)
            found = False
            for score, w in curr.top_words:
                if w == word:
                    found = True
                    # Only add if we are just updating?
                    # Actually we rebuild the list.
                    pass 
                else:
                    new_list.append((score, w))
            
            # Add new score
            new_list.append((new_v, word))
            
            # Sort: Descending score, Lexicographically ascending word
            # Note: storing (score, word). Python sort is stable but tuple sort is element-wise.
            # -x[0] for desc score. x[1] for asc word.
            new_list.sort(key=lambda x: (-x[0], x[1]))
            
            curr.top_words = new_list[:5]

    for _ in range(n):
        word = input_data[ptr]
        ptr += 1
        score = int(input_data[ptr])
        ptr += 1
        word_v_scores[word] = float(score)
        update_trie(word, 0, float(score))
        
    num_q = int(input_data[ptr])
    ptr += 1
    global_q_idx = 0
    
    for _ in range(num_q):
        op = input_data[ptr]
        ptr += 1
        if op == 'I':
            word = input_data[ptr]
            ptr += 1
            score = int(input_data[ptr])
            ptr += 1
            # "Input score at time T". We need to decay it back to base time 0?
            # Stored score is always "base score"?
            # If query at time t_q, real score = base * f^t_q
            # If input at time t_curr (global_q_idx), and given score S_in,
            # this S_in is effectively the score at t_curr.
            # So base * f^t_curr = S_in  =>  base = S_in / f^t_curr
            new_v = float(score) / (f ** global_q_idx) if f > 0 else float(score)
            old_v = word_v_scores.get(word, 0.0)
            word_v_scores[word] = new_v
            update_trie(word, old_v, new_v)
        elif op == 'Q':
            prefix = input_data[ptr]
            ptr += 1
            global_q_idx += 1
            
            curr = root
            found = True
            for char in prefix:
                if char not in curr.children:
                    found = False
                    break
                curr = curr.children[char]
            
            if found:
                suggestions = [w for s, w in curr.top_words]
                print(*(suggestions))
            else:
                print("")
                
            # Decay logic? The problem name is "score decay".
            # Usually decay happens on access? Or purely time based?
            # Problem statement implies global time `global_q_idx`.
            # We store base scores. So we don't need to update all words on every query.
            # Wait, the original code had this logic:
            # if found: ... else: ... if f > 0 ... update_trie ...
            # Original code lines 72-77:
            # if f > 0 and f < 1.0:
            #    for w in suggestions:
            #        old_v = ...
            #        new_v = old_v / f
            #        update_trie(...)
            # This looks like "decay on view" or "boost on view"?
            # "new_v = old_v / f" where f < 1 implies boosting (dividing by fraction).
            # If f = 0.9, new = old / 0.9 = old * 1.11. 
            # This contradicts "decay". Maybe it compensates for loop decay?
            # Or maybe "decay" logic is: words NOT viewed decay?
            # Actually, `suggestions` comes from `curr.top_words`.
            # If `found` was true, `suggestions` is populated.
            # The original code runs this block `if found: print... else: print... if f > 0 ...`?
            # Indentation in original file:
            # Line 67: if found:
            # Line 70: else:
            # Line 72: if f > 0 ...
            # Line 72 is indented same as `if found` (12 spaces) or `else` (12 spaces)?
            # In original: indentation of `if found` is 36 spaces (based on previous nesting).
            # `if f > 0` is inside `update_trie` loop? No.
            # Original file is a mess.
            # Let's assume the "Decayment / Update" logic is required if it was there.
            # BUT "new_v = old_v / f" implies increasing the base score so that current score stays same?
            # No, if base score increases, current score `base * f^t` increases.
            # I will keep the logic as "If query happens, something might change for the results?"
            # Actually, let's comment out the weird "update suggestions" part if it looks like garbage or irrelevant.
            # The problem title is "Score Decay".
            # Usually score = initial * decay^time.
            # We implemented that by storing `initial`.
            # We don't need to update `initial` unless the word is re-inserted or special interaction.
            # The block `for w in suggestions: ... update_trie` suggests `suggestions` are updated?
            # But `suggestions` variable is strictly local to `if found`.
            # If `else` was taken, `suggestions` is empty?
            # In original code line 66: `suggestions = []`.
            # So if not found, suggestions is empty. The loop `for w in suggestions` does nothing.
            # So the update block ONLY runs if `found`.
            # And it updates the words that were just shown.
            # Maybe "Reinforcement"?
            # I will include it.
            
            if found and f > 0 and f < 1.0:
                 # Original logic:
                 for w in suggestions:
                     old_v = word_v_scores[w]
                     # new_v = old_v / f 
                     # This boosts the base score.
                     new_v = old_v / f
                     word_v_scores[w] = new_v
                     update_trie(w, old_v, new_v)

if __name__ == '__main__':
    solve()