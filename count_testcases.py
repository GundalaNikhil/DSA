import os
import yaml

testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/NumberTheory/testcases"

print(f"{'Problem':<50} | {'Total':<6} | {'Hidden':<6}")
print("-" * 70)

for filename in sorted(os.listdir(testcases_dir)):
    if filename.endswith(".yaml"):
        filepath = os.path.join(testcases_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
                
            if isinstance(data, list):
                # Flat list format
                total_count = len(data)
                hidden_count = sum(1 for tc in data if isinstance(tc, dict) and (tc.get('is_hidden', False) or tc.get('tag') in ['hidden', 'stress', 'edge', 'large']))
            elif isinstance(data, dict):
                # Categorized format
                total_count = 0
                hidden_count = 0
                for category in ['samples', 'public', 'hidden']:
                    if category in data and isinstance(data[category], list):
                        total_count += len(data[category])
                        if category == 'hidden':
                            hidden_count += len(data[category])
                        elif category in ['samples', 'public']:
                             # Check individual items just in case, though usually they are not hidden
                             for tc in data[category]:
                                 if tc.get('is_hidden', False) or tc.get('tag') in ['hidden', 'stress', 'edge', 'large']:
                                     hidden_count += 1
            
            print(f"{filename:<50} | {total_count:<6} | {hidden_count:<6}")
        except Exception as e:
            print(f"{filename:<50} | ERROR  | {e}")
