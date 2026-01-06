#!/usr/bin/env python3
"""
TRI-008 Image Generation - Dictionary Compression Size
Generates 5 high-quality explanatory images.
"""

import sys, os, re, time
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

cloudinary.config(cloud_name=CLOUDINARY_CLOUD_NAME, api_key=CLOUDINARY_API_KEY, api_secret=CLOUDINARY_API_SECRET)

TRI_008_PROMPTS = {
    "mobile-keyboard": """Create a clear hand-drawn diagram showing mobile keyboard dictionary optimization.

TOP SECTION - "Mobile Keyboard Settings":
Show a smartphone screen. A setting toggle is on: "Enable Dictionary Compression (Trie-based)".

MIDDLE SECTION - "Comparison":
- Laptop (Raw Dictionary): "Uses 12.5 MB"
- Mobile (Compressed Dictionary): "Uses 2.1 MB" ✓

Show a "Shrinking" arrow from 12.5MB to 2.1MB.

BOTTOM SECTION - "Why This Matters":
- Fits more words in small RAM
- Faster app loading
- Better performance

STYLE:
- Professional hand-drawn excalidraw aesthetic
- LARGE, BOLD, CLEAR text
- High contrast colors (Yellow/Green/Blue)
- Educational poster quality

CRITICAL: All text must be LARGE and CRYSTAL CLEAR. This is a tutorial diagram.""",

    "trie-reuse-concept": """Create a technical diagram visualizing prefix reuse in a Trie.

TITLE: "Trie Node Reuse Example: ['a', 'ab', 'abc']"

MAIN DIAGRAM:
Show 3 words stacked:
a
ab
abc

Draw a Trie for them:
root → a → b → c

Label the nodes:
- "a" node: "Shared by 3 words"
- "b" node: "Shared by 2 words"
- "c" node: "Used by 1 word"

CALCULATION BOX:
Raw Chars: 1 + 2 + 3 = 6
Trie Nodes: 4
Savings: 33% Space ✓

STYLE:
- Graph paper background
- Professional technical layout
- LARGE, BOLD text labels
- High visibility color coding

CRITICAL: The concept of "sharing" must be visually obvious. Text MUST be readable.""",

    "node-count-rules": """Create a clear whiteboard-style diagram explaining the node counting rules.

TITLE: "How to Count Trie Nodes"

RULE 1: The Root node ALWAYS counts as 1.
RULE 2: Every unique character path creates exactly ONE node.
RULE 3: Shared prefixes do NOT create duplicate nodes.

VISUAL EXAMPLE:
Words: ["car", "cat"]
Structure:
root (1) → c (1) → a (1) → r (1)
                        ↳ t (1)
Total: 5 Nodes

ANNOTATION:
"Node Count = Total Unique Prefixes + Root"

STYLE:
- Marker-on-whiteboard aesthetic
- Thick black lines and arrows
- Large, bold text (18pt+)
- Clean, focused layout

CRITICAL: Educational and clear logic explanation. No tiny text!""",

    "dry_run_part1": """Create PART 1 of detailed dry run for TRI-008.

TITLE: "Dry Run: Counting Nodes Part 1/2"

INPUT:
Words: ["a", "ab", "abc", "ace"]

STEP 1: Insert "a"
- root + 'a' = 2 nodes

STEP 2: Insert "ab"
- Reuses 'a', adds 'b' = 3 nodes

STEP 3: Insert "abc"
- Reuses 'a', 'b', adds 'c' = 4 nodes

Show the Trie so far: root → a → b → c

STYLE:
- Step-by-step numbered boxes
- Large circles for trie nodes
- Green highlights for reused paths
- Bold node counts
- Tutorial quality

CRITICAL: Show the reuse clearly.""",

    "dry_run_part2": """Create PART 2 of detailed dry run completing the example.

TITLE: "Dry Run: Counting Nodes Part 2/2"

STEP 4: Insert "ace"
- root (reuse)
- a (reuse)
- c (NEW branch!) → node count = 5
- e (NEW node) → node count = 6

FINAL TRIE STRUCTURE:
        root
          |
          a
        /   \\
       b     c
       |     |
       c     e

FINAL RESULT BOX:
Node Count = 6 ✓

COMPARISON:
Raw Characters: 1 + 2 + 3 + 3 = 9
Trie Nodes: 6
Space Saved: 3 / 9 = 33%

STYLE:
- Same style as Part 1
- Final result in highlighted GREEN box
- Clear, simple tree visualization
- Professional educational finish

CRITICAL: Complete the story with crystal clear steps and LARGE TEXT!"""
}

def generate_image(api_key, prompt, output_path):
    client = genai.Client(api_key=api_key)
    print(f"Generating...")
    models = ["gemini-2.5-flash-image", "gemini-2.0-flash-exp-image-generation"]
    for model in models:
        try:
            print(f"  Trying: {model}")
            response = client.models.generate_content(model=model, contents=prompt,
                config=types.GenerateContentConfig(response_modalities=['IMAGE', 'TEXT']))
            if response.candidates and len(response.candidates) > 0:
                for part in response.candidates[0].content.parts:
                    if part.inline_data:
                        with open(output_path, "wb") as f:
                            f.write(part.inline_data.data)
                        print(f"  ✓ Success! ({len(part.inline_data.data):,} bytes)")
                        return True
        except Exception as e:
            print(f"  ✗ {model} failed")
    return False

def upload(image_path, folder):
    print(f"  Uploading...")
    try:
        response = cloudinary.uploader.upload(image_path, folder=folder, overwrite=True, resource_type="image")
        print(f"  ✓ Uploaded: {response['secure_url']}")
        return response['secure_url']
    except Exception as e:
        print(f"  ✗ Upload error: {e}")
        return None

def update_editorial(path, urls):
    print(f"\nUpdating editorial...")
    with open(path, 'r') as f: content = f.read()
    
    if 'mobile-keyboard' in urls:
        content = re.sub(r'!\[Real-World Application\]\([^)]+\)', f'![Mobile Keyboard Optimization Scenario]({urls["mobile-keyboard"]})', content)
    if 'trie-reuse-concept' in urls:
        pattern = r'(### Optimal Approach)'
        content = re.sub(pattern, f'\\1\n\n![Trie Node Reuse Concept]({urls["trie-reuse-concept"]})', content)
    if 'node-count-rules' in urls:
        pattern = r'(<!-- mermaid -->)'
        content = re.sub(pattern, f'![Node Counting Rules]({urls["node-count-rules"]})\n\n\\1', content)
    if 'dry_run_part1' in urls:
        pattern = r'(## Example Walkthrough:)'
        content = re.sub(pattern, f'\\1\n\n![Dry Run Part 1: Initial Insertion]({urls["dry_run_part1"]})', content)
    if 'dry_run_part2' in urls:
        if "![Algorithm Visualization]" in content:
            content = re.sub(r'!\[Algorithm Visualization\]\([^)]+\)', f'![Dry Run Part 2: Branching and Final Count]({urls["dry_run_part2"]})', content)
        else:
            pattern = r'(Total nodes: 4)'
            content = re.sub(pattern, f'\\1\n\n![Dry Run Part 2: Branching and Final Count]({urls["dry_run_part2"]})', content)
    
    with open(path, 'w') as f: f.write(content)
    print(f"  ✓ Updated")

def main():
    print("="*70 + "\nTRI-008: Dictionary Compression Size\n" + "="*70)
    out = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    out.mkdir(exist_ok=True)
    ed = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-008-dictionary-compression-size.md")
    urls = {}
    for i, (name, prompt) in enumerate(TRI_008_PROMPTS.items(), 1):
        print(f"\n[{i}/5] {name}\n" + "-"*70)
        path = out / f"TRI-008-{name}.png"
        if generate_image(GOOGLE_API_KEY, prompt, str(path)):
            if path.exists() and path.stat().st_size > 0:
                time.sleep(3)
                url = upload(str(path), "Tries/TRI-008")
                if url: urls[name] = url
        print("-"*70)
    if urls:
        update_editorial(ed, urls)
        print(f"\n{'='*70}\nSUCCESS: {len(urls)}/5 images!\n{'='*70}")
    return len(urls)

if __name__ == "__main__": main()
