import os
import re
import sys

def get_file_content(filepath):
    """Reads file content."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file_content(filepath, content):
    """Writes content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def standardize_headers(content):
    """Standardizes headers in the editorial content."""
    original_content = content
    
    # 1. Replace "Walkthrough: Sample Testcase" variations
    # Regex covers:
    # ## Walkthrough: Sample Testcase
    # ## 🧪 Walkthrough: Sample Testcase
    # ## Sample Walkthrough
    pattern_sample = re.compile(r"^##\s+(?:🧪\s*)?Walkthrough:\s*Sample Testcase.*$", re.MULTILINE | re.IGNORECASE)
    content = pattern_sample.sub("## 🧪 Test Case Walkthrough (Dry Run)", content)

    # 2. Replace "Step-by-Step Visual Walkthrough"
    pattern_visual = re.compile(r"^##\s+(?:🎯\s*)?Step-by-Step Visual Walkthrough.*$", re.MULTILINE | re.IGNORECASE)
    content = pattern_visual.sub("## 🧪 Test Case Walkthrough (Dry Run)", content)

    # 3. Replace simple "Test Case Walkthrough" if it doesn't have (Dry Run)
    # Be careful not to replace the correct one if it's already correct.
    # Look for line that is EXACTLY "## Test Case Walkthrough" or "## 🧪 Test Case Walkthrough"
    pattern_simple = re.compile(r"^##\s+(?:🧪\s*)?Test Case Walkthrough\s*$", re.MULTILINE)
    content = pattern_simple.sub("## 🧪 Test Case Walkthrough (Dry Run)", content)
    
    # 4. Replace "Visual Walkthrough"
    pattern_vis_simple = re.compile(r"^##\s+Visual Walkthrough\s*$", re.MULTILINE)
    content = pattern_vis_simple.sub("## 🧪 Test Case Walkthrough (Dry Run)", content)

    # 5. Replace "Sample Walkthrough"
    pattern_samp_simple = re.compile(r"^##\s+Sample Walkthrough\s*$", re.MULTILINE)
    content = pattern_samp_simple.sub("## 🧪 Test Case Walkthrough (Dry Run)", content)

    # 6. Replace "Dry Run"
    pattern_dry = re.compile(r"^##\s+Dry Run\s*$", re.MULTILINE)
    content = pattern_dry.sub("## 🧪 Test Case Walkthrough (Dry Run)", content)

    return content

def process_file(filepath):
    """Process a single editorial file."""
    content = get_file_content(filepath)
    if not content:
        return False

    new_content = standardize_headers(content)
    
    if new_content != content:
        write_file_content(filepath, new_content)
        return True
    return False

def process_all(base_path, specific_topics=None):
    """Process all editorials in dsa-problems."""
    count_files = 0
    count_updated = 0
    
    if specific_topics:
        topics = specific_topics
    else:
        # Get all subdirs in base_path
        topics = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        topics = sorted(topics)

    for topic in topics:
        editorials_dir = os.path.join(base_path, topic, "editorials")
        if not os.path.exists(editorials_dir):
            continue
            
        files = [f for f in os.listdir(editorials_dir) if f.endswith(".md")]
        for filename in files:
            filepath = os.path.join(editorials_dir, filename)
            count_files += 1
            if process_file(filepath):
                print(f"Updated: {topic}/{filename}")
                count_updated += 1
                
    print(f"Total files scanned: {count_files}")
    print(f"Total files updated: {count_updated}")

if __name__ == "__main__":
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"
    
    topics = sys.argv[1:] if len(sys.argv) > 1 else None
    process_all(base_path, topics)
