#!/usr/bin/env python3
"""
TRI-004 Image Generation - Replace Words with Shortest Rare Prefix
Generates 5 comprehensive explanatory images including detailed dry run.
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

# 5 comprehensive images for TRI-004
TRI_004_PROMPTS = {
    "medical-scenario": """Create a clear hand-drawn diagram showing medical record compression system scenario.

TOP SECTION - "Medical Record Compression System":
Show a medical record with the word "cardiologist" highlighted

MIDDLE SECTION - "Dictionary of Medical Abbreviations":
Create a clean table:
| Prefix | Rarity | Meaning |
|--------|--------|---------|
| "card" | 5 | Common prefix |
| "cardio" | 2 | Rare specialty ★ |

Show decision process with arrows:
"cardiologist" → Check prefixes → Choose "cardio" (rarity 2 \< 5) ✓

BOTTOM SECTION - "Applications":
Show 3 boxes with icons:
🏥 Medical Records Storage
💊 ICD Coding
📊 Insurance Claims

STYLE:
- Professional hand-drawn medical theme
- LARGE, BOLD, CLEAR text
- Light blue/green medical colors
- Clean table format
- Educational poster quality

CRITICAL: This is a teaching diagram - all text must be LARGE and READABLE!""",

    "trie-with-rarity": """Create a technical diagram showing trie structure with rarity tracking.

TITLE: "Trie with Best Root Tracking"

Dictionary: {"cat": 1, "car": 2, "card": 3}

TOP - "Concept":
"Each node stores the BEST root seen so far (lowest rarity, then shortest)"

MAIN DIAGRAM - Trie Structure:
```
         root
          |
          c (best: null)
          |
          a (best: null)
         / \\
        t   r (best: "car", rarity=2) ★ END
   (best: "cat"  |
    rarity=1) ★ END  d (best: "car", rarity=2)
                      NOT "card" because "car" is shorter
                      when rarity is same ★ END
```

Each node shows:
- Character
- Best root (if any)
- Rarity score
- END marker for dictionary words

LEGEND BOX:
★ = End of dictionary word
Best root = Lowest rarity, tie-break by length

STYLE:
- Graph paper background
- Clean tree structure with thick lines
- Color code: Green for best roots, Orange for END markers
- LARGE labels
- Professional technical diagram

CRITICAL: Show WHY nodes store best roots - this is the key insight!""",

    "construction-process": """Create multi-step diagram showing trie construction with rarity updates.

TITLE: "Building Trie: Dictionary = {cat:1, car:2, card:3}"

STEP 1 - "Insert 'cat' (rarity=1)":
```
    root
     |
     c
     |
     a
     |
     t (END, root="cat", rarity=1) ★
```
Label: "First word - becomes best at node 't'"

STEP 2 - "Insert 'car' (rarity=2)":
```
    root
     |
     c
     |
     a
    / \\
   t   r (END, root="car", rarity=2) ★
(cat:1)
```
Label: "'car' creates new branch"

STEP 3 - "Insert 'card' (rarity=3)":
```
    root
     |
     c
     |
     a
    / \\
   t   r (best="car" rarity=2, NOT "card")
(cat:1) |
        d (END, root="card", rarity=3) ★
         But node 'r' keeps "car" as best!
```

RESULT BOX:
"Node 'r' stores 'car' as best root because:
 1. Among ancestors: 'car' has rarity=2
 2. 'card' has rarity=3  (2 \< 3, so 'car' wins)"

STYLE:
- Step numbers in LARGE circles
- Green for optimal choices, Red for rejected
- Clear progression with arrows
- Whiteboard aesthetic

CRITICAL: Explain the greedy choice at each step!""",

    "dry-run-cattle-part1": """Create PART 1 of detailed dry run for sentence "the cattle carried".

TITLE: "Dry Run Part 1/2: Processing 'the' and 'cattle'"

INPUT BOX:
Dictionary: {cat:1, car:2}
Sentence: "the cattle carried"

Trie Built:
```
    root
     |
     c
     |
     a
    / \\
   t   r
(cat:1)(car:2)
```

WORD 1: Process "the"
```
Step 1: Start at root
Step 2: Look for child 't' → NOT FOUND
        (root only has child 'c')
Step 3: No match found
Result: Keep original → "the"
```

WORD 2: Process "cattle"
```
Step 1: Start at root
Step 2: 'c' → Found! Move to 'c' node
Step 3: 'a' → Found! Move to 'a' node  
Step 4: 't' → Found! Move to 't' node
        ★ Node 't' is END → Found root "cat" (rarity=1)
        Save as best_root = "cat"
Step 5: 't' → Look for child 't' → NOT FOUND
        Traversal stops
Step 6: Best root found: "cat"
Result: Replace "cattle" → "cat"
```

STATS:
Words processed: 2/3
Results so far: ["the", "cat"]

Label: "→ Continue to Part 2/2"

STYLE:
- Step-by-step numbered boxes
- GREEN checkmarks for matches
- RED X for not found
- Clear tree references
- Teaching walkthrough quality

CRITICAL: Show EVERY decision point!""",

    "dry-run-cattle-part2": """Create PART 2 of detailed dry run completing the example.

TITLE: "Dry Run Part 2/2: Processing 'carried'"

WORD 3: Process "carried"
```
Step 1: Start at root
Step 2: 'c' → Found! Move to 'c' node
Step 3: 'a' → Found! Move to 'a' node
Step 4: 'r' → Found! Move to 'r' node
        ★ Node 'r' is END → Found root "car" (rarity=2)
        Save as best_root = "car"
Step 5: 'r' → Look for child 'r' → NOT FOUND
        Traversal stops
Step 6: Best root found: "car"  
Result: Replace "carried" → "car"
```

FINAL RESULT BOX (LARGE):
```
Original: "the cattle carried"
Dictionary: {cat:1, car:2}

Processing Results:
✓ "the" → "the" (no match)
✓ "cattle" → "cat" (matched "cat", rarity=1)
✓ "carried" → "car" (matched "car", rarity=2)

Final Output: "the cat car"
```

COMPLEXITY COMPARISON:
Naive: O(N × M × L) = 3 × 2 × 7 = 42 operations
Trie: O(3 × L) = 3 × 7 = 21 operations
Speedup: 2x (much better for large M!)

STYLE:
- Continue part 1 style
- Final result in highlighted box
- Green checkmarks for all results
- Complexity comparison table
- Professional completion diagram

CRITICAL: Show complete solution with performance comparison!"""
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
            print(f"  ✗ {model} failed: {e}")
    return False

def upload_to_cloudinary(image_path, folder):
    print(f"  Uploading...")
    try:
        response = cloudinary.uploader.upload(image_path, folder=folder, overwrite=True, resource_type="image")
        print(f"  ✓ Uploaded: {response['secure_url']}")
        return response['secure_url']
    except Exception as e:
        print(f"  ✗ Upload error: {e}")
        return None

def update_editorial(editorial_path, image_urls):
    print(f"\nUpdating editorial...")
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    if 'medical-scenario' in image_urls:
        content = re.sub(r'!\[Problem Concept\]\([^)]+\)', f'![Medical Record Compression Scenario]({image_urls["medical-scenario"]})', content)
    if 'trie-with-rarity' in image_urls:
        pattern = r'(\*\*Trie with Rarity Tracking:\*\*)'
        content = re.sub(pattern, f'\\1\n\n![Trie with Rarity Tracking]({image_urls["trie-with-rarity"]})', content)
    if 'construction-process' in image_urls:
        pattern = r'(Result: "the cat car")'
        content = re.sub(pattern, f'![Trie Construction Process]({image_urls["construction-process"]})\n\n\\1', content)
    if 'dry-run-cattle-part1' in image_urls:
        pattern = r'(\*\*Step-by-Step\*\*:)'
        content = re.sub(pattern, f'\\1\n\n![Dry Run Part 1]({image_urls["dry-run-cattle-part1"]})', content)
    if 'dry-run-cattle-part2' in image_urls:
        pattern = r'(Final Output: "the cat car")'
        content = re.sub(pattern, f'![Dry Run Part 2]({image_urls["dry-run-cattle-part2"]})\n\n\\1', content)
    
    with open(editorial_path, 'w') as f:
        f.write(content)
    print(f"  ✓ Editorial updated")

def main():
    print("="*70)
    print("TRI-004 IMAGE GENERATION - Replace Words with Rare Prefix")
    print("="*70)
    
    output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    output_dir.mkdir(exist_ok=True)
    editorial_path = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-004-replace-words-shortest-rare-prefix.md")
    
    image_urls = {}
    for i, (name, prompt) in enumerate(TRI_004_PROMPTS.items(), 1):
        print(f"\n[{i}/5] {name}")
        print("-"*70)
        local_path = output_dir / f"TRI-004-{name}.png"
        if generate_image(GOOGLE_API_KEY, prompt, str(local_path)):
            if local_path.exists() and local_path.stat().st_size > 0:
                time.sleep(3)
                url = upload_to_cloudinary(str(local_path), "Tries/TRI-004")
                if url:
                    image_urls[name] = url
        print("-"*70)
    
    if image_urls:
        update_editorial(editorial_path, image_urls)
        print(f"\n{'='*70}\nSUCCESS: {len(image_urls)}/5 images generated!\n{'='*70}")
    return len(image_urls)

if __name__ == "__main__":
    main()
