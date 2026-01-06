#!/usr/bin/env python3
"""
TRI-006 Image Generation - Lexicographic k-th String Not Present
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

TRI_006_PROMPTS = {
    "username-scenario": """Create a clear hand-drawn diagram showing a username suggestion scenario.

TOP SECTION - "User Registration":
Show a registration form. Username field has "alice" typed in, but a RED "X" says "Username Already Taken!"

MIDDLE SECTION - "Generating Suggestions":
Show a "Magic Wand" icon generating a list of available (missing) usernames by lexicographical order.
Suggestions:
1. "aa" ✓
2. "ab" ✓
3. "ac" ✓
Label: "Finding the k-th available string of length ≤ L"

BOTTOM SECTION - "Why This Matters":
- Available username discovery
- Product ID generation
- Token allocation

STYLE:
- Professional hand-drawn excalidraw aesthetic
- LARGE, BOLD, CLEAR text
- High contrast
- Educational poster quality

CRITICAL: All text must be LARGE and CRYSTAL CLEAR. This is a tutorial diagram.""",

    "lexicographic-space": """Create a technical diagram visualizing the lexicographical search space.

TITLE: "Lexicographical Search Space (Length ≤ 2)"

MAIN DIAGRAM:
Show strings arranged in a giant sorted list:
a, aa, ab, ac, ..., az, b, ba, bb, ..., zz

Highlight specific strings:
- "a" (Boxed, RED, labeled "Taken")
- "b" (Boxed, RED, labeled "Taken")
- "aa" (Boxed, GREEN, labeled "Missing #1")
- "ac" (Boxed, GREEN, labeled "Missing #2")
- "ad" (Boxed, GREEN, labeled "Missing #3")

Show an arrow pointing to "ad" with label "k-th Missing String (k=3)"

STYLE:
- Graph paper background
- Professional technical layout
- LARGE, BOLD text labels
- High visibility color coding (Red=Taken, Green=Available)

CRITICAL: The sorted order must be obvious. Text MUST be readable.""",

    "dfs-counting-logic": """Create a clear whiteboard-style diagram explaining the DFS counting logic.

TITLE: "DFS: Navigating to the k-th Missing String"

MAIN CONCEPT:
Show a trie node 'root' branching into 'a', 'b', 'c'...
Label on branch 'a': "Missing strings in this subtree = 25"
Label on branch 'b': "Missing strings in this subtree = 26"

LOGIC BOX:
If k <= MissingInSubtree:
   → "Go down this branch!"
Else:
   → "k = k - MissingInSubtree; Try next branch"

ANNOTATION:
"Using Combinatorics to leap over hundreds of strings at once!"

STYLE:
- Marker-on-whiteboard aesthetic
- Thick black lines and arrows
- Large, bold text (18pt+)
- Clean, focused layout

CRITICAL: Educational and clear logic explanation. No tiny text!""",

    "dry_run_part1": """Create PART 1 of detailed dry run for TRI-006.

TITLE: "Dry Run Part 1/2: Navigation Decision"

INPUT:
Inserted: ["a", "ab"]
L=2, k=3 (Find 3rd missing string)

STAGE 1 - "At Root":
Draw trie: Root → a* → b (where * is end marker)
Check branch 'a':
- Strings under 'a' (length 1, 2): a, aa, ab, ac, ..., az
- Total strings = 27
- Taken: "a", "ab"
- Missing: 27 - 2 = 25
Decision: 3 <= 25? YES! → "Enter 'a' branch"

STAGE 2 - "At Node 'a'":
Draw node 'a' with children candidates 'a', 'b', 'c', 'd'...
Goal: Find k=3rd missing under 'a'

STYLE:
- Step-by-step numbered boxes
- Large circles for trie nodes
- Green highlight for chosen path
- Bold calculations
- Tutorial quality

CRITICAL: Show the decision math clearly. Text must be large.""",

    "dry_run_part2": """Create PART 2 of detailed dry run completing the example.

TITLE: "Dry Run Part 2/2: Picking the Character"

CONTINUING AT NODE 'a' (k=3):
Show children check list:
1. Child 'a' → String "aa" → MISSING ✓ (Count=1)
   - k=3 > 1? YES → Skip "aa", k = 3 - 1 = 2
2. Child 'b' → String "ab" → TAKEN ✗ (Count=0)
   - Skip "ab", k remains 2
3. Child 'c' → String "ac" → MISSING ✓ (Count=1)
   - k=2 > 1? YES → Skip "ac", k = 2 - 1 = 1
4. Child 'd' → String "ad" → MISSING ✓ (Count=1)
   - k=1 <= 1? YES → FOUND IT!

FINAL RESULT BOX:
k-th Missing String = "ad"

VISUAL:
"a" + "d" = "ad" (Depth 2, Prefix "a")

STYLE:
- Same style as Part 1
- Large checkboxes for each child check
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
    
    if 'username-scenario' in urls:
        content = re.sub(r'!\[Problem Concept\]\([^)]+\)', f'![Username Generation Scenario]({urls["username-scenario"]})', content)
    if 'lexicographic-space' in urls:
        pattern = r'(### 📚 Detailed Explanation)'
        content = re.sub(pattern, f'\\1\n\n![Lexicographical Search Space]({urls["lexicographic-space"]})', content)
    if 'dfs-counting-logic' in urls:
        pattern = r'(### ✅ Optimal Approach)'
        content = re.sub(pattern, f'\\1\n\n![DFS Counting Logic]({urls["dfs-counting-logic"]})', content)
    if 'dry_run_part1' in urls:
        pattern = r'(### 🧪 Test Case Walkthrough)'
        content = re.sub(pattern, f'\\1\n\n![Dry Run Part 1]({urls["dry_run_part1"]})', content)
    if 'dry_run_part2' in urls:
        pattern = r'(Answer: "ac")' # Note: Editorial says "ac" but wait, the example in editorial has inserted=["a", "ab"], L=2, k=3. Let's check my logic again.
        # Editorial says:
        # 1. "aa" k=1
        # 2. "ac" k=2
        # 3. "ad" k=3
        # Wait, the editorial example says result is "ad" but then says Answer: "ac".
        # Let's check:
        # missing: aa, ac, ad...
        # So k=1: aa, k=2: ac, k=3: ad.
        # My prompt says result is "ad".
        # I should fix the editorial text if it's wrong.
        content = re.sub(pattern, f'Answer: "ad"\n\n![Dry Run Part 2]({urls["dry_run_part2"]})', content)
    
    with open(path, 'w') as f: f.write(content)
    print(f"  ✓ Updated")

def main():
    print("="*70 + "\nTRI-006: k-th String Not Present\n" + "="*70)
    out = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    out.mkdir(exist_ok=True)
    ed = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-006-kth-string-not-present.md")
    urls = {}
    for i, (name, prompt) in enumerate(TRI_006_PROMPTS.items(), 1):
        print(f"\n[{i}/5] {name}\n" + "-"*70)
        path = out / f"TRI-006-{name}.png"
        if generate_image(GOOGLE_API_KEY, prompt, str(path)):
            if path.exists() and path.stat().st_size > 0:
                time.sleep(3)
                url = upload(str(path), "Tries/TRI-006")
                if url: urls[name] = url
        print("-"*70)
    if urls:
        update_editorial(ed, urls)
        print(f"\n{'='*70}\nSUCCESS: {len(urls)}/5 images!\n{'='*70}")
    return len(urls)

if __name__ == "__main__": main()
