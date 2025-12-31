import sys

def lsh_candidate_prob(b: int, r: int, s: float) -> float:
    prob_band_match = s ** r
    prob_all_bands_mismatch = (1.0 - prob_band_match) ** b
    return 1.0 - prob_all_bands_mismatch

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    b = int(data[0])
    r = int(data[1])
    s = float(data[2])
    print(f"{lsh_candidate_prob(b, r, s):.6f}")

if __name__ == "__main__":
    main()
