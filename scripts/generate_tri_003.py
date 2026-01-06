#!/usr/bin/env python3
"""
TRI-003 Image Generation - Distinct Substrings Count via Trie
Generates 5 high-quality explanatory images including detailed dry run.
"""

import sys
import os
import re
import time
from pathlib import Path
from google import genai
from google.genai import types
import cloudinary
import cloudinary.uploader

# API Credentials
GOOGLE_API_KEY = "AIzaSyArgfdzbWUOpaoYqg9_DnAcNeUt7j6Zg9k"
CLOUDINARY_CLOUD_NAME = "dy4dvna3t"
CLOUDINARY_API_KEY = "422129878775651"
CLOUDINARY_API_SECRET = "sBGz50Rxzzwk9pFAMFxyjvQN5uk"

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

# Enhanced prompts with CLEAR, READABLE text - 5 images total
TRI_003_PROMPTS = {
    "dna-scenario": """Create a clear hand-drawn diagram showing DNA sequence analysis scenario.

TOP SECTION - "DNA Sequence Lab":
Show a DNA sequencestring "ATAT" in a rounded box with clear labeling

MIDDLE SECTION - "Finding All Patterns":
List all distinct substrings clearly in a grid format:
• "A" (appears 2 times)
• "T" (appears 2 times)  
• "AT" (appears 2 times)
• "TA" (appears 1 time)
• "ATA" (appears 1 time)
• "TAT" (appears 1 time)
• "ATAT" (appears 1 time)

Total: 7 DISTINCT patterns

BOTTOM SECTION - "Applications":
Show 3 small icons with labels:
🧬 Genetic Fingerprinting
🔬 Disease Markers
📊 Pattern Recognition

STYLE:
- Hand-drawn excalidraw aesthetic
- LARGE, BOLD text for readability
- Clean layout with good spacing
- Light blue/green colors for biology theme
- Professional educational poster quality

CRITICAL: All text must be LARGE (18pt+) and CRYSTAL CLEAR for teaching purposes.""",
    
    "suffix-trie-concept": """Create a clean technical diagram explaining the suffix trie concept for counting substrings.

TOP SECTION - "Why Suffix Trie Works":
Box 1: "String: abc"
Box 2: "Suffixes: abc, bc, c"
Box 3: "Each suffix contains all its own substrings"

MIDDLE SECTION - "Trie Visualization for 'abc'":
Draw a clean tree structure:
```
       root
         |
         a ← substring "a"
         |
         b ← substring "ab"
         |
         c ← substring "abc"
        /
       b ← substring "b"  
       |
       c ← substring "bc"
      /
     c ← substring "c"
```

Show nodes numbered: Total nodes = 6 (but drawn correctly as 5 unique paths)

BOTTOM SECTION - "Key Insight":
"Each node in trie = 1 distinct substring"
"Count nodes (excluding root) = Count distinct substrings"

STYLE:
- Clean graph paper / grid background
- Large clear labels on all nodes
- Thick connecting lines
- Number each node clearly
- Professional technical diagram quality
- ALL TEXT BOLD AND READABLE

CRITICAL: This explains the core concept - make it crystal clear!""",
    
    "construction-steps": """Create a 3-column step-by-step construction diagram.

TITLE: "Building Suffix Trie for 'aaa'"

COLUMN 1 - "Step 1: Insert 'aaa'":
Show trie after first suffix:
root → a(1) → a(2) → a(3)
Label: "Creates 3 new nodes"
Label: "Substrings: a, aa, aaa"

COLUMN 2 - "Step 2: Insert 'aa'":
Show trie (same as above):
root → a(1) → a(2) → a(3)
Add arrow showing path being reused
Label: "0 new nodes (path exists!)"
Label: "Same substrings already counted"

COLUMN 3 - "Step 3: Insert 'a'":
Show final trie (same):
root → a(1) → a(2) → a(3)
Add arrow showing path being reused  
Label: "0 new nodes (path exists!)"
Label: "Result: 3 distinct substrings"

BOTTOM - "Final Count":
Large box: "Total Nodes = 3"
"Distinct Substrings = {a, aa, aaa}"

STYLE:
- Whiteboard marker aesthetic  
- Clear column separation with light backgrounds
- LARGE step numbers in circles
- Green checkmarks ✓ for paths
- Thick tree diagrams
- High contrast colors

CRITICAL: Show WHY reusing paths means no new substrings. Teaching diagram!""",
    
    "dry-run-aba-part1": """Create PART 1 of detailed dry run walkthrough for string "aba".

TITLE: "Dry Run: Building Suffix Trie for 'aba' (Part 1/2)"

INPUT BOX:
String: "aba"
Suffixes to insert: "aba", "ba", "a"

STEP 1 - "Insert suffix 'aba'":
Show progression:
```
Start: root (empty)

After 'a': root → a (Node 1) ← CREATE node "a"
After 'ab': root → a → b (Node 2) ← CREATE node "ab"  
After 'aba': root → a → b → a (Node 3) ← CREATE node "aba"
```

Visual tree after Step 1:
```
    root
     |
     a ← Node 1 (substring: "a")
     |
     b ← Node 2 (substring: "ab")
     |
     a ← Node 3 (substring: "aba")
```

STATISTICS BOX:
Nodes created: 3
Substrings so far: {a, ab, aba}

STYLE:
- Step number in large circle
- Tree drawn with thick lines
- Each node labeled with number AND substring
- CREATE actions in GREEN
- Clear progression arrows
- Educational walkthrough quality

Label: "→ Continue to Part 2/2"

CRITICAL: Show EVERY detail of the insertion process!""",
    
    "dry-run-aba-part2": """Create PART 2 of detailed dry run walkthrough for string "aba".

TITLE: "Dry Run: Building Suffix Trie for 'aba' (Part 2/2)"

STEP 2 - "Insert suffix 'ba'":
Show progression:
```
Start from root

After 'b': root → b (Node 4) ← CREATE new node "b"
After 'ba': root → b → a (Node 5) ← CREATE node "ba"
```

Visual tree after Step 2:
```
    root
    / \\
   a   b ← Node 4 (substring: "b")
   |   |
   b   a ← Node 5 (substring: "ba")
   |
   a
```

STEP 3 - "Insert suffix 'a'":
```
Start from root

After 'a': root → a (Node 1) ← REUSE existing!
```

NO NEW NODES - Path already exists!

FINAL TRIE:
```
    root
    / \\
   a   b
   |   |
   b   a
   |
   a
```

FINAL RESULT BOX (LARGE):
Total Nodes: 5
Distinct Substrings: {a, ab, aba, b, ba}
Count: 5 ✓

STYLE:
- Continue same style from Part 1
- REUSE actions in ORANGE/YELLOW
- CREATE actions in GREEN
- Final result in large highlighted box
- Clear tree structure
- All text LARGE and BOLD

CRITICAL: Show the complete walkthrough with final answer!"""
}


def generate_image(api_key, prompt, output_path):
    """Generate high-quality image."""
    client = genai.Client(api_key=api_key)
    
    print(f"Generating...")
    
    # Use best available model
    models_to_try = [
        "gemini-2.5-flash-image",
        "gemini-2.0-flash-exp-image-generation",
    ]
    
    for model_name in models_to_try:
        try:
            print(f"  Trying: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE', 'TEXT']
                )
            )
            
            if response.candidates and len(response.candidates) > 0:
                for part in response.candidates[0].content.parts:
                    if part.inline_data:
                        img_data = part.inline_data.data
                        with open(output_path, "wb") as f:
                            f.write(img_data)
                        print(f"  ✓ Success! ({len(img_data):,} bytes)")
                        return True
            
        except Exception as e:
            print(f"  ✗ {model_name} failed: {e}")
            continue
    
    return False


def upload_to_cloudinary(image_path, folder):
    """Upload to Cloudinary."""
    print(f"  Uploading...")
    try:
        response = cloudinary.uploader.upload(
            image_path,
            folder=folder,
            overwrite=True,
            resource_type="image"
        )
        url = response['secure_url']
        print(f"  ✓ Uploaded: {url}")
        return url
    except Exception as e:
        print(f"  ✗ Upload error: {e}")
        return None


def update_editorial(editorial_path, image_urls):
    """Update editorial with images."""
    print(f"\nUpdating editorial...")
    
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    # Replace placeholder images
    if 'dna-scenario' in image_urls:
        content = re.sub(
            r'!\[Problem Concept\]\([^)]+\)',
            f'![DNA Sequence Analysis Scenario]({image_urls["dna-scenario"]})',
            content
        )
    
    if 'suffix-trie-concept' in image_urls:
        # Insert after "Why Trie?" section
        pattern = r'(\*\*Example: "aaa"\*\*)'
        replacement = f'![Suffix Trie Concept]({image_urls["suffix-trie-concept"]})\n\n\\1'
        content = re.sub(pattern, replacement, content)
    
    if 'construction-steps' in image_urls:
        # Insert after the construction example
        pattern = r'(Total nodes = 3 \(excluding root\)\\nDistinct substrings = 3: \{"a", "aa", "aaa"\})'
        replacement = f'\\1\n\n![Suffix Trie Construction Steps]({image_urls["construction-steps"]})'
        content = re.sub(pattern, replacement, content)
    
    if 'dry-run-aba-part1' in image_urls:
        # Insert in dry run section
        pattern = r'(\*\*Example: "aba"\*\*)'
        replacement = f'\\1\n\n![Dry Run Part 1: Inserting aba]({image_urls["dry-run-aba-part1"]})'
        content = re.sub(pattern, replacement, content)
    
    if 'dry-run-aba-part2' in image_urls:
        # Insert after part 1
        pattern = r'(Distinct substrings: "a", "ab", "aba", "b", "ba" \(5 distinct strings)'
        replacement = f'\\1\n\n![Dry Run Part 2: Complete Walkthrough]({image_urls["dry-run-aba-part2"]})'
        content = re.sub(pattern, replacement, content)
    
    with open(editorial_path, 'w') as f:
        f.write(content)
    
    print(f"  ✓ Editorial updated")


def main():
    print("=" * 70)
    print("TRI-003 IMAGE GENERATION - Distinct Substrings via Trie")
    print("=" * 70)
    
    problem_id = "TRI-003"
    output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    output_dir.mkdir(exist_ok=True)
    
    editorial_path = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-003-distinct-substrings-count-trie.md")
    
    image_urls = {}
    total = len(TRI_003_PROMPTS)
    
    for i, (image_name, prompt) in enumerate(TRI_003_PROMPTS.items(), 1):
        print(f"\n[{i}/{total}] {image_name}")
        print("-" * 70)
        
        local_path = output_dir / f"{problem_id}-{image_name}.png"
        
        if generate_image(GOOGLE_API_KEY, prompt, str(local_path)):
            if local_path.exists() and local_path.stat().st_size > 0:
                time.sleep(3)
                url = upload_to_cloudinary(str(local_path), f"Tries/{problem_id}")
                if url:
                    image_urls[image_name] = url
        
        print("-" * 70)
    
    if image_urls:
        update_editorial(editorial_path, image_urls)
        print(f"\n{'='*70}")
        print(f"SUCCESS: {len(image_urls)}/{total} images generated!")
        print(f"{'='*70}")
    else:
        print(f"\n{'='*70}")
        print(f"ERROR: No images generated")
        print(f"{'='*70}")
    
    return len(image_urls)


if __name__ == "__main__":
    main()
