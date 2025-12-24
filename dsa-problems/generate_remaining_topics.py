#!/usr/bin/env python3
"""Generate empty problem files for all remaining DSA topics"""

import os
import sys

BASE_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"

# Topic definitions with their problem counts
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

def get_problem_slugs(topic_dir):
    """Extract problem slugs from the basic practice file"""
    practice_files = [
        f for f in os.listdir(topic_dir) 
        if f.startswith("basic-") and f.endswith("-practice.md")
    ]
    
    if not practice_files:
        print(f"Warning: No practice file found for {topic_dir}")
        return []
    
    practice_file = os.path.join(topic_dir, practice_files[0])
    slugs = []
    titles = []
    
    with open(practice_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        
        current_title = None
        for i, line in enumerate(lines):
            if line.startswith('## '):
                # Extract problem number and title
                current_title = line.replace('## ', '').strip()
                # Remove problem number prefix like "1) "
                if ') ' in current_title:
                    current_title = current_title.split(') ', 1)[1]
            elif line.startswith('- Slug:'):
                slug = line.replace('- Slug:', '').strip()
                slugs.append(slug)
                titles.append(current_title)
    
    return list(zip(titles, slugs))

def create_problem_file(topic, prefix, num, title, slug):
    """Create an empty problem markdown file"""
    display_id = f"{prefix}-{num:03d}"
    content = f"""# {display_id}: {title}

[Problem content to be added]
"""
    return content

def create_editorial_file(topic, prefix, num, title, slug):
    """Create an empty editorial markdown file"""
    display_id = f"{prefix}-{num:03d}"
    content = f"""# Editorial: {display_id} - {title}

[Editorial content to be added]
"""
    return content

def create_testcase_file(topic, prefix, num, title, slug):
    """Create an empty testcase YAML file"""
    display_id = f"{prefix}-{num:03d}"
    content = f"""# Testcases for {display_id}: {title}
# YAML content to be added
"""
    return content

def create_quiz_file(topic, prefix, num, title, slug):
    """Create an empty quiz YAML file"""
    display_id = f"{prefix}-{num:03d}"
    content = f"""# Quiz for {display_id}: {title}
# YAML content to be added
"""
    return content

def create_image_readme(topic, prefix, num, title, slug):
    """Create README for image directory"""
    display_id = f"{prefix}-{num:03d}"
    content = f"""# Images for {display_id}: {title}

This directory contains images and diagrams for problem {display_id}.

## Files
- Add relevant diagrams, flowcharts, and illustrations here
"""
    return content

def main():
    total_files_created = 0
    
    for topic, info in TOPICS.items():
        prefix = info["prefix"]
        count = info["count"]
        
        topic_dir = os.path.join(BASE_DIR, topic)
        
        if not os.path.exists(topic_dir):
            print(f"Warning: Directory {topic_dir} does not exist, skipping...")
            continue
        
        print(f"\n{'='*60}")
        print(f"Processing {topic} ({prefix}-001 to {prefix}-{count:03d})")
        print(f"{'='*60}")
        
        # Get problem slugs from practice file
        problem_info = get_problem_slugs(topic_dir)
        
        if not problem_info:
            print(f"Could not extract problems for {topic}, using generic names...")
            problem_info = [(f"Problem {i+1}", f"problem-{i+1}") for i in range(count)]
        
        # Ensure we have exactly 'count' problems
        if len(problem_info) < count:
            print(f"Warning: Found {len(problem_info)} problems, expected {count}")
            # Pad with generic problems
            for i in range(len(problem_info), count):
                problem_info.append((f"Problem {i+1}", f"problem-{i+1}"))
        
        problem_info = problem_info[:count]  # Take only first 'count' problems
        
        # Create subdirectories if they don't exist
        for subdir in ['problems', 'editorials', 'testcases', 'quizzes', 'images']:
            subdir_path = os.path.join(topic_dir, subdir)
            os.makedirs(subdir_path, exist_ok=True)
        
        # Create files for each problem
        for i, (title, slug) in enumerate(problem_info, start=1):
            display_id = f"{prefix}-{i:03d}"
            
            # 1. Problem file
            problem_path = os.path.join(topic_dir, 'problems', f"{display_id}-{slug}.md")
            with open(problem_path, 'w', encoding='utf-8') as f:
                f.write(create_problem_file(topic, prefix, i, title, slug))
            print(f"✓ Created {problem_path}")
            
            # 2. Editorial file
            editorial_path = os.path.join(topic_dir, 'editorials', f"{display_id}-{slug}.md")
            with open(editorial_path, 'w', encoding='utf-8') as f:
                f.write(create_editorial_file(topic, prefix, i, title, slug))
            print(f"✓ Created {editorial_path}")
            
            # 3. Testcase file
            testcase_path = os.path.join(topic_dir, 'testcases', f"{display_id}-{slug}.yaml")
            with open(testcase_path, 'w', encoding='utf-8') as f:
                f.write(create_testcase_file(topic, prefix, i, title, slug))
            print(f"✓ Created {testcase_path}")
            
            # 4. Quiz file
            quiz_path = os.path.join(topic_dir, 'quizzes', f"{display_id}-{slug}.yaml")
            with open(quiz_path, 'w', encoding='utf-8') as f:
                f.write(create_quiz_file(topic, prefix, i, title, slug))
            print(f"✓ Created {quiz_path}")
            
            # 5. Image directory with README
            image_dir = os.path.join(topic_dir, 'images', display_id)
            os.makedirs(image_dir, exist_ok=True)
            image_readme_path = os.path.join(image_dir, 'README.md')
            with open(image_readme_path, 'w', encoding='utf-8') as f:
                f.write(create_image_readme(topic, prefix, i, title, slug))
            print(f"✓ Created {image_readme_path}")
            
            total_files_created += 5
        
        print(f"\n✓ Completed {topic}: {count} problems × 5 files = {count * 5} files")
    
    print(f"\n{'='*60}")
    print(f"🎉 ALL COMPLETE!")
    print(f"{'='*60}")
    print(f"Total files created: {total_files_created}")
    print(f"Topics processed: {len(TOPICS)}")
    print(f"Total problems: {sum(info['count'] for info in TOPICS.values())}")

if __name__ == "__main__":
    main()
