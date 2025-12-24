import math
import yaml
import random

def solve(m, registers):
    if m == 16:
        alpha = 0.673
    elif m == 32:
        alpha = 0.697
    elif m == 64:
        alpha = 0.709
    else:
        alpha = 0.7213 / (1 + 1.079 / m)
    
    total_sum = sum(math.pow(2, -r) for r in registers)
    e = alpha * (m ** 2) / total_sum
    
    if e <= 2.5 * m:
        v = registers.count(0)
        if v > 0:
            e = m * math.log(m / v)
            
    return e

def make_test_case(registers):
    m = len(registers)
    e = solve(m, registers)
    return {
        "input": f"{m}\n" + " ".join(map(str, registers)),
        "output": f"{e:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([1]*16)
        ],
        "public": [
            make_test_case([0]*16),
            make_test_case([1]*32),
            make_test_case([5]*64)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case([20]*16))
    tc["hidden"].append(make_test_case([0]*65536))
    
    # Boundary cases
    tc["hidden"].append(make_test_case([0, 1]*8)) # 16 registers, half zeroes
    
    # Random cases
    for m in [16, 128, 1024]:
        regs = [random.randint(0, 10) for _ in range(m)]
        tc["hidden"].append(make_test_case(regs))

    # Stress case
    m_stress = 65536
    regs_stress = [random.randint(0, 20) for _ in range(m_stress)]
    tc["hidden"].append(make_test_case(regs_stress))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
