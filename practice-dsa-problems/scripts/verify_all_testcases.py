
import os

BASE_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/practice-dsa-problems"
CATEGORIES = [
    "AdvancedGraphs", "Arrays", "DP", "Geometry", "Graphs", 
    "Heaps", "LinkedLists", "MathAdvanced", "Matrix", 
    "NumberTheory", "Recursion", "SegmentTree", "Strings", 
    "Trees", "Tries"
]

def check_category(category):
    prob_dir = os.path.join(BASE_DIR, category, "problems")
    test_dir = os.path.join(BASE_DIR, category, "testcases")
    
    if not os.path.exists(prob_dir):
        return f"{category}: Problems dir missing"
        
    # Get problem IDs
    problems = []
    for f in os.listdir(prob_dir):
        if f.endswith(".md"):
            # Assuming format CATEGORY-XXX-slug.md
            parts = f.split("-")
            if len(parts) >= 2:
                pid = f"{parts[0]}-{parts[1]}"
                problems.append(pid)
    
    problems.sort()
    
    # Get test cases
    testcases = set()
    if os.path.exists(test_dir):
        for f in os.listdir(test_dir):
            if f.endswith(".json") or f.endswith(".yaml"):
                 # Assuming format CATEGORY-XXX-slug.json
                parts = f.split("-")
                if len(parts) >= 2:
                    pid = f"{parts[0]}-{parts[1]}"
                    testcases.add(pid)
    
    missing = []
    for p in problems:
        if p not in testcases:
            missing.append(p)
            
    status = "OK" if not missing else "MISSING"
    return {
        "category": category,
        "problems": len(problems),
        "testcases": len(testcases),
        "status": status,
        "missing": missing
    }

print(f"{'Category':<20} | {'Problems':<10} | {'TestCases':<10} | {'Status':<10}")
print("-" * 60)

total_problems = 0
total_testcases = 0

all_passed = True

for cat in CATEGORIES:
    res = check_category(cat)
    if isinstance(res, str):
        print(res)
        continue
        
    print(f"{res['category']:<20} | {res['problems']:<10} | {res['testcases']:<10} | {res['status']:<10}")
    if res['missing']:
        print(f"  Missing: {', '.join(res['missing'])}")
        all_passed = False
        
    total_problems += res['problems']
    total_testcases += res['testcases']

print("-" * 60)
print(f"{'TOTAL':<20} | {total_problems:<10} | {total_testcases:<10} | {'PASSED' if all_passed else 'FAILED'}")
