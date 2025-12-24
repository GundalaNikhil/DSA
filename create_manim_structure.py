#!/usr/bin/env python3
"""
Create manim folder structure mirroring dsa-problems structure.
For each problem file in dsa-problems/[Topic]/problems/*.md,
create corresponding manim/[Topic]/video-scripts/*.py
"""

import os
import glob
from pathlib import Path

# Base paths
DSA_PROBLEMS_BASE = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"
MANIM_BASE = "/Users/nikhilgundala/Desktop/NTB/DSA/manim"

# Get all topic folders
topics = [
    "AdvancedGraphs", "Arrays", "Bitwise", "Concurrency", "DP",
    "GameTheory", "Geometry", "Graphs", "GraphsBasics", "Greedy",
    "Hashing", "Heaps", "LinkedLists", "MathAdvanced", "NumberTheory",
    "Probabilistic", "ProbabilisticDS", "Queues", "Recursion",
    "SegmentTree", "Sorting", "Stacks", "Strings", "StringsClassic",
    "Trees", "TreesDP", "Tries"
]

def create_manim_structure():
    """Create manim folder structure for all topics and problems"""
    
    created_dirs = []
    created_files = []
    
    for topic in topics:
        # Create topic folder
        topic_path = os.path.join(MANIM_BASE, topic)
        if not os.path.exists(topic_path):
            os.makedirs(topic_path)
            created_dirs.append(topic_path)
            print(f"Created directory: {topic}/")
        
        # Create video-scripts subfolder
        video_scripts_path = os.path.join(topic_path, "video-scripts")
        if not os.path.exists(video_scripts_path):
            os.makedirs(video_scripts_path)
            created_dirs.append(video_scripts_path)
            print(f"Created directory: {topic}/video-scripts/")
        
        # Find all problem files in dsa-problems
        problems_path = os.path.join(DSA_PROBLEMS_BASE, topic, "problems")
        if os.path.exists(problems_path):
            problem_files = glob.glob(os.path.join(problems_path, "*.md"))
            
            for problem_file in problem_files:
                # Extract problem filename without extension
                problem_name = os.path.basename(problem_file).replace(".md", "")
                
                # Create corresponding .py file in manim
                py_file_path = os.path.join(video_scripts_path, f"{problem_name}.py")
                
                if not os.path.exists(py_file_path):
                    # Create empty Python file with basic template
                    with open(py_file_path, 'w') as f:
                        f.write(f'''"""
Manim animation script for {problem_name}

This script creates an animated visualization for the problem:
{problem_name}

Topic: {topic}
"""

from manim import *


class {problem_name.replace("-", "_").title().replace("_", "")}Scene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("{problem_name}", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
''')
                    created_files.append(py_file_path)
                    print(f"Created file: {topic}/video-scripts/{problem_name}.py")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total directories created: {len(created_dirs)}")
    print(f"Total files created: {len(created_files)}")
    print("\nFolder structure created successfully!")
    print(f"\nManim base directory: {MANIM_BASE}")

if __name__ == "__main__":
    create_manim_structure()
