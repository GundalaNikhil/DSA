#!/usr/bin/env python3
"""
Batch create all empty files for remaining 11 DSA topics
Total: 11 topics × 16 problems × 5 files = 880 files
"""

import os

BASE_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"

TOPICS = {
    "Hashing": {"prefix": "HSH", "count": 16},
    "Heaps": {"prefix": "HEP", "count": 16},
    "LinkedLists": {"prefix": "LNK", "count": 16},
    "MathAdvanced": {"prefix": "MTH", "count": 16},
    "NumberTheory": {"prefix": "NUM", "count": 16},
    "Probabilistic": {"prefix": "PRB", "count": 16},
    "ProbabilisticDS": {"prefix": "PDS", "count": 16},
    "Queues": {"prefix": "QUE", "count": 16},
    "Recursion": {"prefix": "REC", "count": 16},
    "SegmentTree": {"prefix": "SEG", "count": 16},
    "Sorting": {"prefix": "SRT", "count": 16},
}

def main():
    total_created = 0
    
    for topic_name, info in TOPICS.items():
        prefix = info["prefix"]
        count = info["count"]
        topic_dir = os.path.join(BASE_DIR, topic_name)
        
        print(f"\n{'='*70}")
        print(f"Creating files for {topic_name} ({prefix}-001 to {prefix}-{count:03d})")
        print(f"{'='*70}")
        
        # Ensure directories exist
        for subdir in ['problems', 'editorials', 'testcases', 'quizzes', 'images']:
            os.makedirs(os.path.join(topic_dir, subdir), exist_ok=True)
        
        for i in range(1, count + 1):
            display_id = f"{prefix}-{i:03d}"
            slug = f"problem-{i}"
            
            # 1. Problem file
            problem_file = os.path.join(topic_dir, 'problems', f"{display_id}-{slug}.md")
            with open(problem_file, 'w') as f:
                f.write(f"# {display_id}: Problem {i}\n\n[Problem content to be added]\n")
            
            # 2. Editorial file
            editorial_file = os.path.join(topic_dir, 'editorials', f"{display_id}-{slug}.md")
            with open(editorial_file, 'w') as f:
                f.write(f"# Editorial: {display_id} - Problem {i}\n\n[Editorial content to be added]\n")
            
            # 3. Testcase file
            testcase_file = os.path.join(topic_dir, 'testcases', f"{display_id}-{slug}.yaml")
            with open(testcase_file, 'w') as f:
                f.write(f"# Testcases for {display_id}: Problem {i}\n# YAML content to be added\n")
            
            # 4. Quiz file
            quiz_file = os.path.join(topic_dir, 'quizzes', f"{display_id}-{slug}.yaml")
            with open(quiz_file, 'w') as f:
                f.write(f"# Quiz for {display_id}: Problem {i}\n# YAML content to be added\n")
            
            # 5. Image directory README
            image_dir = os.path.join(topic_dir, 'images', display_id)
            os.makedirs(image_dir, exist_ok=True)
            readme_file = os.path.join(image_dir, 'README.md')
            with open(readme_file, 'w') as f:
                f.write(f"# Images for {display_id}: Problem {i}\n\n")
                f.write(f"This directory contains images and diagrams for problem {display_id}.\n\n")
                f.write("## Files\n- Add relevant diagrams, flowcharts, and illustrations here\n")
            
            total_created += 5
            
            if i % 4 == 0:
                print(f"  Created {i}/{count} problems...")
        
        print(f"✓ Completed {topic_name}: {count} problems × 5 files = {count * 5} files")
    
    print(f"\n{'='*70}")
    print(f"🎉 ALL FILES CREATED SUCCESSFULLY!")
    print(f"{'='*70}")
    print(f"Total files created: {total_created}")
    print(f"Topics processed: {len(TOPICS)}")
    print(f"Total problems: {sum(t['count'] for t in TOPICS.values())}")

if __name__ == "__main__":
    main()
