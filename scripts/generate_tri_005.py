#!/usr/bin/env python3
"""TRI-005: Binary Trie Min XOR Pair - 5 comprehensive images"""
import sys, os, re, time
from pathlib import Path
from google import genai
from google.genai import types
import cloudinary
import cloudinary.uploader

GOOGLE_API_KEY = "AIzaSyArgfdzbWUOpaoYqg9_DnAcNeUt7j6Zg9k"
CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET = "dy4dvna3t", "422129878775651", "sBGz50Rxzzwk9pFAMFxyjvQN5uk"
cloudinary.config(cloud_name=CLOUDINARY_CLOUD_NAME, api_key=CLOUDINARY_API_KEY, api_secret=CLOUDINARY_API_SECRET)

TRI_005_PROMPTS = {
    "network-routing": """Hand-drawn diagram: Network Packet Routing Optimization

TOP: "IP Address Similarity Detection"
Show 2 IP addresses as binary:
IP 1: 3 = 00011
IP 2: 5 = 00101
XOR = 00110 = 6 (only 2 bits different) ✓

MIDDLE: "Binary Trie for Efficient Matching"
Small tree showing how binary trie organizes IPs by bits

BOTTOM: "Applications" - 3 boxes:
📡 Network Optimization
💾 Data Deduplication  
🔐 Error Correction

STYLE: Excalidraw hand-drawn, LARGE clear text, network theme colors (blue/green), professional educational quality.
CRITICAL: All text LARGE and READABLE for teaching!""",

    "binary-trie-structure": """Technical diagram: Binary Trie Structure Explained

TITLE: "Binary Trie for Numbers [3, 5, 10]"

TOP: Show binary representations clearly:
3  = 00011 (4 bits shown for clarity)
5  = 00101
10 = 1010

MAIN: Binary tree diagram:
```
         root
        /    \\
      0        1
     /          \\
    0            0
   / \\           \\
  1   1          1
 /     \\         \\
1(3)   0(5)     0(10)
```

Show paths clearly:
Path for 3:  0→0→1→1 ✓
Path for 5:  0→1→0→1 ✓  
Path for 10: 1→0→1→0 ✓

LEGEND:
• Each level = 1 bit (MSB to LSB)
• Left child = 0, Right child = 1
• Leaf nodes store numbers

STYLE: Graph paper grid, thick tree lines, LARGE labels, professional technical diagram.
CRITICAL: Show bit-by-bit structure clearly!""",

    "greedy-query": """Whiteboard diagram: Greedy Query Strategy for Min XOR

TITLE: "Finding Closest Match to 5 (0101)"

Trie contains: 3 (0011), 10 (1010)

STEP-BY-STEP Query Process:
```
Query: 5 = 0101

Bit 3 (MSB): Want 0 ✓
  → Go LEFT (0 branch exists)
  
Bit 2: Want 1
  → Check: only 0 available
  → MUST take 0 (compromise)
  
Bit 1: Want 0 ✓
  → Go LEFT (0 available)
  
Bit 0 (LSB): Want 1 ✓
  → Go RIGHT (1 available)

Result: 0011 = 3
XOR(5,3) = 0101 ⊕ 0011 = 0110 = 6
```

GREEDY RULE BOX:
"At each bit: prefer SAME bit (XOR=0)
If not available, take opposite (XOR=1)"

STYLE: Whiteboard markers, colored paths (green=match, red=compromise), LARGE steps, clear annotations.
CRITICAL: Show greedy decision at EVERY bit!""",

    "dry-run-part1": """Dry Run Part 1/2: Building Trie and First Queries

TITLE: "Test Case: arr=[3,10,5,25], L=8"

INPUT:
Binary representations (5 bits):
3  = 00011
10 = 01010
5  = 00101
25 = 11001

STEP 1: Build Binary Trie
Insert all numbers (show final trie structure)

STEP 2: Query 3
```
Find closest to 3 in trie
Greedy traversal: 0→0→1→0→1
Match: 5 (00101)
XOR: 3⊕5 = 00011⊕00101 = 00110 = 6
Check: 6 ≤ 8 ✓ VALID
Current min = 6
```

STEP 3: Query 10
```
Find closest to 10
Best match: 3 (00011)
XOR: 10⊕3 = 01010⊕00011 = 01001 = 9
Check: 9 > 8 ✗ INVALID (exceeds limit)
Current min = 6 (unchanged)
```

Label: "→ Continue to Part 2/2"

STYLE: Step numbers in circles, green for valid/red for invalid, clear binary calculations.
CRITICAL: Show limit checking!""",

    "dry-run-part2": """Dry Run Part 2/2: Remaining Queries and Final Result

STEP 4: Query 5
```
Find closest to 5
Best match: 3 (00011)  
XOR: 5⊕3 = 00101⊕00011 = 00110 = 6
Check: 6 ≤ 8 ✓ VALID
Current min = 6 (already found)
```

STEP 5: Query 25
```
Find closest to 25 (11001)
Try all paths...
Closest: 10 (01010)
XOR: 25⊕10 = 11001⊕01010 = 10011 = 19
Check: 19 > 8 ✗ INVALID
Current min = 6 (unchanged)
```

FINAL RESULT (LARGE BOX):
```
Minimum XOR ≤ 8: 6
Pair: (3, 5)

Verification:
✓ 3⊕5 = 6 ✤ 8
✓ All other valid pairs checked
✓ Answer: 6
```

COMPLEXITY:
Naive O(n²): 16 comparisons
Binary Trie: O(n×30): ~120 ops
Speedup: ~8x

STYLE: Final result highlighted, all XOR calculations shown, complexity comparison.
CRITICAL: Complete walkthrough with verification!"""
}

def generate_image(api_key, prompt, output_path):
    client = genai.Client(api_key=api_key)
    print(f"Generating...")
    for model in ["gemini-2.5-flash-image", "gemini-2.0-flash-exp-image-generation"]:
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
    except: return None

def update_editorial(path, urls):
    print(f"\nUpdating editorial...")
    with open(path, 'r') as f: content = f.read()
    if 'network-routing' in urls:
        content = re.sub(r'!\[Problem Concept\]\([^)]+\)', f'![Network Routing Scenario]({urls["network-routing"]})', content)
    if 'binary-trie-structure' in urls:
        content = re.sub(r'(\*\* Binary Trie for \[3, 5, 10\]:\*\*)', f'\\1\n\n![Binary Trie Structure]({urls["binary-trie-structure"]})', content)
    if 'greedy-query' in urls:
        content = re.sub(r'(Result: 3, XOR = 5\^3 = 6)', f'![Greedy Query Strategy]({urls["greedy-query"]})\n\n\\1', content)
    if 'dry-run-part1' in urls:
        content = re.sub(r'(\*\*Step 1: Build Trie\*\*)', f'![Dry Run Part 1]({urls["dry-run-part1"]})\n\n\\1', content)
    if 'dry-run-part2' in urls:
        content = re.sub(r'(Minimum XOR ≤ 8: 6)', f'![Dry Run Part 2]({urls["dry-run-part2"]})\n\n\\1', content)
    with open(path, 'w') as f: f.write(content)
    print(f"  ✓ Updated")

def main():
    print("="*70 + "\nTRI-005: Binary Trie Min XOR\n" + "="*70)
    out = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    out.mkdir(exist_ok=True)
    ed = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-005-binary-trie-min-xor-pair-limit.md")
    urls = {}
    for i, (name, prompt) in enumerate(TRI_005_PROMPTS.items(), 1):
        print(f"\n[{i}/5] {name}\n" + "-"*70)
        path = out / f"TRI-005-{name}.png"
        if generate_image(GOOGLE_API_KEY, prompt, str(path)):
            if path.exists() and path.stat().st_size > 0:
                time.sleep(3)
                url = upload(str(path), "Tries/TRI-005")
                if url: urls[name] = url
        print("-"*70)
    if urls:
        update_editorial(ed, urls)
        print(f"\n{'='*70}\nSUCCESS: {len(urls)}/5 images!\n{'='*70}")
    return len(urls)

if __name__ == "__main__": main()
