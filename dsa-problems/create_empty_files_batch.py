#!/usr/bin/env python3
"""
Create empty problem files for Greedy, Stacks, and StringsClassic topics
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems")

# Problem definitions
PROBLEMS = {
    "Greedy": {
        "prefix": "GRD",
        "problems": [
            ("001", "campus-shuttle-driver-swaps"),
            ("002", "lab-kit-distribution"),
            ("003", "festival-stall-placement"),
            ("004", "library-power-backup"),
            ("005", "shuttle-overtime-minimizer"),
            ("006", "robotics-component-bundling-loss-quality"),
            ("007", "campus-wifi-expansion"),
            ("008", "exam-proctor-allocation"),
            ("009", "shuttle-refuel-with-refund"),
            ("010", "library-merge-queues"),
            ("011", "campus-event-ticket-caps"),
            ("012", "workshop-task-cooldown-priority"),
            ("013", "auditorium-seat-refunds"),
            ("014", "festival-bandwidth-split"),
            ("015", "robotics-median-after-batches-stale"),
            ("016", "shuttle-schedule-delay-minimizer"),
        ]
    },
    "Stacks": {
        "prefix": "STK",
        "problems": [
            ("001", "notebook-undo-simulator"),
            ("002", "lab-mixed-bracket-repair"),
            ("003", "conveyor-weighted-deduplication"),
            ("004", "rooftop-sunset-count"),
            ("005", "workshop-next-taller-width"),
            ("006", "assembly-previous-greater-parity"),
            ("007", "trading-desk-threshold-jump"),
            ("008", "canteen-token-climb-span"),
            ("009", "lab-sliding-min-stack"),
            ("010", "stadium-max-tracker"),
            ("011", "circuit-postfix-variables"),
            ("012", "campus-expression-optimizer"),
            ("013", "auditorium-histogram-one-booster"),
            ("014", "shuttle-validation-time-windows"),
            ("015", "bike-repair-plates"),
            ("016", "assembly-line-span-reset"),
        ]
    },
    "StringsClassic": {
        "prefix": "STC",
        "problems": [
            ("001", "kmp-prefix-function"),
            ("002", "pattern-search-kmp"),
            ("003", "z-function"),
            ("004", "pattern-search-z"),
            ("005", "suffix-array-doubling"),
            ("006", "lcp-array-kasai"),
            ("007", "longest-repeated-substring-sa"),
            ("008", "distinct-substrings-sa"),
            ("009", "minimal-rotation-sa"),
            ("010", "lcp-two-suffixes"),
            ("011", "lcs-two-strings-sa"),
            ("012", "diff-substrings-two-strings"),
            ("013", "palindromic-tree-eertree"),
            ("014", "longest-palindrome-one-wildcard"),
            ("015", "aho-corasick-cooldown-scoring"),
            ("016", "suffix-automaton-queries"),
        ]
    }
}

def create_files_for_topic(topic_name, prefix, problems):
    """Create all files for a given topic"""
    topic_dir = BASE_DIR / topic_name
    
    # Ensure directories exist
    for subdir in ["problems", "editorials", "testcases", "quizzes", "images"]:
        (topic_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    created_count = 0
    
    for num, slug in problems:
        filename = f"{prefix}-{num}-{slug}"
        
        # Create testcases YAML
        testcase_file = topic_dir / "testcases" / f"{filename}.yaml"
        if not testcase_file.exists():
            testcase_file.touch()
            created_count += 1
        
        # Create quizzes YAML
        quiz_file = topic_dir / "quizzes" / f"{filename}.yaml"
        if not quiz_file.exists():
            quiz_file.touch()
            created_count += 1
        
        # Create image directory and README
        image_dir = topic_dir / "images" / f"{prefix}-{num}"
        image_dir.mkdir(parents=True, exist_ok=True)
        image_readme = image_dir / "README.md"
        if not image_readme.exists():
            image_readme.touch()
            created_count += 1
    
    print(f"✅ {topic_name}: Created {created_count} new files")
    return created_count

def main():
    print("=" * 60)
    print("Creating Empty Problem Files for Greedy, Stacks, StringsClassic")
    print("=" * 60)
    print()
    
    total_created = 0
    
    for topic_name, config in PROBLEMS.items():
        count = create_files_for_topic(
            topic_name, 
            config["prefix"], 
            config["problems"]
        )
        total_created += count
    
    print()
    print("=" * 60)
    print(f"✅ TOTAL: Created {total_created} files across 3 topics")
    print("=" * 60)
    print()
    print("Summary:")
    for topic_name, config in PROBLEMS.items():
        num_problems = len(config["problems"])
        print(f"  • {topic_name}: {num_problems} problems × 5 files = {num_problems * 5} files")
    print()
    print("Next steps: Manually add content following UNIVERSAL_DSA_GENERATION_PROMPT.md")

if __name__ == "__main__":
    main()
