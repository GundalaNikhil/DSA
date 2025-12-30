import sys

def invert(A):
    n = len(A)
    # Augment
    M = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]

    for i in range(n):
        pivot = i
        for j in range(i + 1, n):
            if abs(M[j][i]) > abs(M[pivot][i]):
                pivot = j
        M[i], M[pivot] = M[pivot], M[i]

        div = M[i][i]
        for j in range(i, 2 * n):
            M[i][j] /= div

        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(i, 2 * n):
                    M[k][j] -= factor * M[i][j]

    return [row[n:] for row in M]

def absorption_stats(P, s: int):
    n = len(P)
    absorbing = []
    transient = []

    for i in range(n):
        if abs(P[i][i] - 1.0) < 1e-9:
            absorbing.append(i)
        else:
            transient.append(i)

    if s in absorbing:
        res = [0.0]
        for idx in absorbing:
            res.append(1.0 if idx == s else 0.0)
        return res

    t_size = len(transient)
    a_size = len(absorbing)

    Q = [[0.0] * t_size for _ in range(t_size)]
    R = [[0.0] * a_size for _ in range(t_size)]

    for i in range(t_size):
        u = transient[i]
        for j in range(t_size):
            v = transient[j]
            Q[i][j] = P[u][v]
        for j in range(a_size):
            v = absorbing[j]
            R[i][j] = P[u][v]

    I_minus_Q = [[(1.0 if i == j else 0.0) - Q[i][j] for j in range(t_size)] for i in range(t_size)]
    N = invert(I_minus_Q)

    s_idx = transient.index(s)

    expected_steps = sum(N[s_idx])

    probs = [0.0] * a_size
    for j in range(a_size):
        for k in range(t_size):
            probs[j] += N[s_idx][k] * R[k][j]

    return [expected_steps] + probs

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        n = int(next(iterator))
        P = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(float(next(iterator)))
            P.append(row)

        num_queries = int(next(iterator))
        query_states = []
        for _ in range(num_queries):
            query_states.append(int(next(iterator)))

        num_absorbing = int(next(iterator))
        absorbing_indices = []
        for _ in range(num_absorbing):
            absorbing_indices.append(int(next(iterator)))

        # Process each query and collect results
        absorption_probs = []
        expected_steps = []

        for s in query_states:
            res = absorption_stats(P, s)
            if res:
                expected_steps.append(f"{res[0]:.6f}")
                # For each absorbing state, get its probability
                # res[0] is expected steps, res[1:] are absorption probs for all absorbing states
                for a_idx in absorbing_indices:
                    # Find which position in res corresponds to absorbing state a_idx
                    # Need to map from global state index to position in absorption probs
                    absorbing_states = []
                    for i in range(n):
                        if abs(P[i][i] - 1.0) < 1e-9:
                            absorbing_states.append(i)

                    if a_idx in absorbing_states:
                        pos = absorbing_states.index(a_idx)
                        if pos + 1 < len(res):
                            absorption_probs.append(f"{res[pos + 1]:.6f}")

        # Output absorption probabilities first
        print(" ".join(absorption_probs))
        # Output expected steps second
        print(" ".join(expected_steps))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
