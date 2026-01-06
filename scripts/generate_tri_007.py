#!/usr/bin/env python3
"""
TRI-007 Image Generation - Minimum Unique Prefix Lengths
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

TRI_007_PROMPTS = {
    "dns-autocomplete": """Create a clear hand-drawn diagram showing a DNS/Domain autocomplete scenario.

TOP SECTION - "Domain Search Bar":
Show a search input field with "tech" typed in. Below it, a dropdown list appears.

MIDDLE SECTION - "Smart Suggestions":
List the domains with their unique prefixes highlighted in BOLD:
- techno... (suggesting "technology.com")
- techni... (suggesting "technical.com")
- techs... (suggesting "techstart.com")

Label: "Minimum characters needed to uniquely distinguish each choice"

BOTTOM SECTION - "Why This Matters":
- Reduced typing (Fast UX)
- Bandwidth saving
- Less cognitive load

STYLE:
- Professional hand-drawn excalidraw aesthetic
- LARGE, BOLD, CLEAR text
- Light blues and grays (Cloud/Tech theme)
- Educational poster quality

CRITICAL: All text must be LARGE and CRYSTAL CLEAR. This is a tutorial diagram.""",

    "trie-with-counts": """Create a technical diagram showing a Trie with word counts at each node.

TITLE: "Trie with Node Counts (Uniqueness Tracking)"

MAIN DIAGRAM:
Draw a Trie for ["zebra", "dog", "duck", "dove"]
Label each node with its character AND count:
- root (count=4)
- z (1)
- e (1)
- b (1) ...
- d (3)
- o (2)
- u (1)
- g (1)
- v (1)

Show paths:
- Path to "zebra" branches off immediately (Count 1 at 'z')
- Path to "duck" branches at 'u' (Count 1 at 'u')
- Paths to "dog" and "dove" share 'd' and 'o' (Count 2), then branch.

STYLE:
- Graph paper background
- Professional technical layout
- LARGE, BOLD text labels
- High contrast colors

CRITICAL: The counts are the most important part. Make them BOLD and VISIBLE.""",

    "algorithm-flow": """Create a clear flowchart-style diagram explaining the algorithm steps.

TITLE: "Algorithm: Finding Minimum Unique Prefixes"

PHASE 1 - "Construction":
Box: "Insert all words into Trie"
Box: "At each node, increment node.count"

PHASE 2 - "Querying":
Box: "For each word, traverse Trie"
Box: "Stop at FIRST node where node.count == 1"
Box: "Current depth = Minimum Unique Prefix Length"

ANNOTATION:
"Linear Time O(N*L) - Thousands of times faster than Brute Force!"

STYLE:
- Marker-on-whiteboard aesthetic
- Thick black lines and arrows
- Large, bold text (18pt+)
- Clean, focused layout

CRITICAL: Educational and clear logic explanation. No tiny text!""",

    "dry_run_part1": """Create PART 1 of detailed dry run for TRI-007.

TITLE: "Dry Run Part 1/2: Building the Trie"

INPUT:
Words: ["zebra", "dog", "duck", "dove"]

STEP 1: Insert "zebra"
- root → z(1) → e(1) → b(1) → r(1) → a(1)

STEP 2: Insert "dog"
- root → d(1) → o(1) → g(1)

STEP 3: Insert "duck"
- root → d(2) → u(1) (branches off 'd')

STEP 4: Insert "dove"
- root → d(3) → o(2) → v(1) (branches off 'o')

Show the FINAL TRIE with all counts updated correctly.

STYLE:
- Step-by-step numbered boxes
- Large circles for trie nodes
- Clear branching structure
- Bold count numbers
- Tutorial quality

CRITICAL: Show the merging/branching logic clearly. Text must be large.""",

    "dry_run_part2": """Create PART 2 of detailed dry run completing the example.

TITLE: "Dry Run Part 2/2: Calculating Lengths"

WALKTHROUGH:
1. "zebra": Traverse root→z(1). Length: 1 ✓
2. "dog": Traverse root→d(3)→o(2)→g(1). Length: 3 ✓
3. "duck": Traverse root→d(3)→u(1). Length: 2 ✓
4. "dove": Traverse root→d(3)→o(2)→v(1). Length: 3 ✓

FINAL RESULT BOX:
Result: [1, 3, 2, 3]

VISUAL COMPARISON:
- zebra -> z...
- dog -> dog... (differentiates from dove)
- duck -> du... (differentiates from dog/dove)
- dove -> dov... (differentiates from dog)

STYLE:
- Same style as Part 1
- Large checkmarks for each query
- Final result in highlighted GREEN box
- Clear, simple summary table
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
    
    # Pre-image cleanup: Fix the inconsistent results in text
    content = content.replace("[1,2,2,2]", "[1, 3, 2, 3]")
    content = content.replace("[1, 3, 3, 3]", "[1, 3, 2, 3]")
    content = content.replace("Expected output: [1, 3, 3, 3]", "Expected output: [1, 3, 2, 3]")
    content = content.replace("- \"dog\" → 'd' shared with duck/dove; \"do\" distinguishes from \"du\" (duck) at position 2 → length 2", "- \"dog\" → 'd' shared with duck/dove; \"dog\" distinguishes from \"dove\" at position 3 → length 3")
    content = content.replace("- \"dove\" → 'd' shared; \"do\" shared with \"dog\"; \"dov\" unique → length 3", "- \"dove\" → 'd' shared; \"do\" shared with \"dog\"; \"dov\" unique → length 3")
    content = content.replace("- \"duck\" → 'd' shared; \"du\" unique from \"do\" (dog/dove) → length 2", "- \"duck\" → 'd' shared; \"du\" unique from \"do\" (dog/dove) → length 2")

    if 'dns-autocomplete' in urls:
        content = re.sub(r'!\[Real-World Application\]\([^)]+\)', f'![DNS Autocomplete Scenario]({urls["dns-autocomplete"]})', content)
    if 'trie-with-counts' in urls:
        pattern = r'(### Optimal Approach)'
        content = re.sub(pattern, f'\\1\n\n![Trie with Word Counts]({urls["trie-with-counts"]})', content)
    if 'algorithm-flow' in urls:
        pattern = r'(<!-- mermaid -->)'
        content = re.sub(pattern, f'![Algorithm Flow]({urls["algorithm-flow"]})\n\n\\1', content)
    if 'dry_run_part1' in urls:
        pattern = r'(### Algorithm Visualization)' # Trying to find the best spot or use the existing placeholder
        if "![Algorithm Visualization]" in content:
            content = re.sub(r'!\[Algorithm Visualization\]\([^)]+\)', f'![Dry Run Part 1: Building Trie]({urls["dry_run_part1"]})', content)
        else:
            pattern = r'(## Example Execution:)'
            content = re.sub(pattern, f'\\1\n\n![Dry Run Part 1: Building Trie]({urls["dry_run_part1"]})', content)
    if 'dry_run_part2' in urls:
        pattern = r'(Output: \[1, 3, 2, 3\])'
        content = re.sub(pattern, f'\\1\n\n![Dry Run Part 2: Calculating Lengths]({urls["dry_run_part2"]})', content)
    
    with open(path, 'w') as f: f.write(content)
    print(f"  ✓ Updated")

def main():
    print("="*70 + "\nTRI-007: Minimum Unique Prefix Lengths\n" + "="*70)
    out = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    out.mkdir(exist_ok=True)
    ed = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-007-minimum-unique-prefix-lengths.md")
    urls = {}
    for i, (name, prompt) in enumerate(TRI_007_PROMPTS.items(), 1):
        print(f"\n[{i}/5] {name}\n" + "-"*70)
        path = out / f"TRI-007-{name}.png"
        if generate_image(GOOGLE_API_KEY, prompt, str(path)):
            if path.exists() and path.stat().st_size > 0:
                time.sleep(3)
                url = upload(str(path), "Tries/TRI-007")
                if url: urls[name] = url
        print("-"*70)
    if urls:
        update_editorial(ed, urls)
        print(f"\n{'='*70}\nSUCCESS: {len(urls)}/5 images!\n{'='*70}")
    return len(urls)

if __name__ == "__main__": main()
