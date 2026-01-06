#!/usr/bin/env python3
"""
Generate explanatory images for TRI-002 editorial using Google AI Studio.
Uses imagen-3-pro-generate-001 for higher quality images.
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

# Configure Cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

# Image prompts for TRI-002 - More detailed and explanatory
TRI_002_PROMPTS = {
    "real-world-scenario": """Hand-drawn sketch diagram showing a Git version control scenario. Draw 3 developer workspace windows side-by-side:
    
Window 1 (left): Branch name "feature/xuser-auth" with a small 'x' highlighted/circled in red
Window 2 (middle): Branch name "feature/user-autz" with 'z' circled in red  
Window 3 (right): Branch name "feature/user-aauth" with duplicate 'a' circled in red

Below the windows, draw an arrow pointing down to a merged/grouped section showing "feature/user-a" with annotation "Common prefix after removing 1 char from each".

Use simple excalidraw style: rough hand-drawn lines, minimal colors (black outlines, light blue windows, red circles for typos, green for the result). Add small Git branch icons (forked circles). Label each window with "Dev 1", "Dev 2", "Dev 3". Keep it clean and educational like a whiteboard explanation.""",
    
    "trie-variants": """Technical sketch showing how word variants are generated and inserted into a trie structure.

Top section - "Variant Generation" (show for one example word "interview"):
- Original: "interview" (underlined)
- Deletion at pos 0: "nterview" 
- Deletion at pos 1: "iterview"
- Deletion at pos 2: "inerview"
... (show "..." for middle deletions)
- Deletion at pos 8: "intervie"

Bottom section - Show trie structure with word ID tracking:
Draw a trie tree (circles for nodes, edges labeled with characters). At ROOT, branches to 'i' and 'n'. 
Show word IDs in curly braces at each node: {0,1,2} meaning all 3 words pass through.
Mark the deepest node where all IDs present with a star/highlight.

Use clean hand-drawn style with annotations. Add legend: "○ = node, {ID} = word coverage". Use graph paper aesthetic with grid background.""",
    
    "algorithm-flow": """Whiteboard-style flowchart showing the algorithm steps in 3 clear phases.

Phase 1 - "Variant Generation" (left column, blue):
Box 1: "For each word W"
Box 2: "Insert W into trie (mark with word_id)"
Box 3: "For each position i in W"
Box 4: "Delete char at i → create variant V"
Box 5: "Insert V into trie (mark with word_id)"

Phase 2 - "DFS Traversal" (middle column, green):
Box 1: "Start at trie root"
Box 2: "Track current prefix P"
Box 3: "At each node N"
Box 4: "Check: Does N have ALL word_ids?"
Box 5: "If yes & |P| > max: Update max_prefix = P"

Phase 3 - "Result" (right column, orange):
Box: "Return max_prefix"

Connect phases with arrows. Use marker-on-whiteboard aesthetic: bold lines, colored boxes, clear labels. Add small example annotation showing word_ids {0,1,2} at a node.""",
    
    "test-walkthrough": """Detailed step-by-step walkthrough diagram for test case with annotations.

Input at top in dashed box:
words = ["abc", "axbc", "abxc"]
Goal: Find longest common prefix after ≤1 deletion per word

Step 1 (show trie after insertions):
"Variants generated:"
- Word 0 "abc": abc, bc, ac, ab
- Word 1 "axbc": axbc, xbc, abc, ac, ab  
- Word 2 "abxc": abxc, bxc, axc, abc, abc

Step 2 (show trie structure):
Small tree diagram with nodes labeled:
Root → a {0,1,2} → b {0,1,2} → c {0,1} 
Mark "ab" node with ★ and annotation "All 3 words reach here!"

Step 3 (result):
"Longest common prefix = 'ab' (length 2)"
Show visual: "abc"→"ab", "axbc"→"ab" (delete x), "abxc"→"ab" (delete x)

Use clean hand-drawn style with step numbers in circles, green checkmarks for matches, simple tree diagrams. Educational and clear layout."""
}


def generate_image(api_key, prompt, output_path, model="gemini-2.0-flash-exp-image-generation"):
    """Generate an image using Google AI Studio API."""
    client = genai.Client(api_key=api_key)
    
    print(f"Generating with {model}: {output_path}")
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )
        
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                # inline_data.data is already binary bytes
                img_data = part.inline_data.data
                
                with open(output_path, "wb") as f:
                    f.write(img_data)
                print(f"✓ Image saved ({len(img_data)} bytes)")
                return True
        
        print(f"✗ No image found in response")
        return False
        
    except Exception as e:
        print(f"✗ Error generating image: {e}")
        return False


def upload_to_cloudinary(image_path, folder):
    """Upload an image to Cloudinary and return the URL."""
    print(f"Uploading to Cloudinary: {folder}/")
    try:
        response = cloudinary.uploader.upload(
            image_path,
            folder=folder,
            overwrite=True,
            resource_type="image"
        )
        url = response['secure_url']
        print(f"✓ Uploaded: {url}")
        return url
    except Exception as e:
        print(f"✗ Cloudinary upload error: {e}")
        return None


def update_editorial_markdown(editorial_path, image_urls):
    """Update editorial markdown file with Cloudinary image URLs."""
    print(f"Updating editorial: {editorial_path}")
    
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    # Insert images at appropriate locations
    updates_made = 0
    
    # Image 1: Real-world scenario (after line 54)
    if 'real-world-scenario' in image_urls:
        pattern = r'(- \*\*API Versioning\*\*: Detect common API endpoint patterns despite typos\s*\n\s*\n)(!\[Real-World Application\])'
        replacement = f'\\1![Real-World Application]({image_urls["real-world-scenario"]})\n\n\\2'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            updates_made += 1
        else:
            # Try simpler pattern
            content = re.sub(
                r'!\[Real-World Application\]\(\.\.\/images\/TRI-002\/real-world-scenario\.png\)',
                f'![Real-World Application]({image_urls["real-world-scenario"]})',
                content
            )
    
    # Image 2: Trie variants (after algorithm explanation, around line 145)
    if 'trie-variants' in image_urls:
        content = re.sub(
            r'(Result: "inter" \(depth 5, all word IDs present\)\s*```\s*\n)',
            f'\\1\n![Trie Variants Visualization]({image_urls["trie-variants"]})\n',
            content
        )
        updates_made += 1
    
    # Image 3: Algorithm flow (before implementations, around line 193)
    if 'algorithm-flow' in image_urls:
        content = re.sub(
            r'(!\[Algorithm Visualization\]\(\.\.\/images\/TRI-002\/algorithm-visualization\.png\))',
            f'![Algorithm Flow]({image_urls["algorithm-flow"]})',
            content
        )
        updates_made += 1
    
    # Image 4: Test walkthrough (before common mistakes section, around line 520)
    if 'test-walkthrough' in image_urls:
        content = re.sub(
            r'(### Common Mistakes to Avoid)',
            f'![Test Case Walkthrough]({image_urls["test-walkthrough"]})\n\n\\1',
            content
        )
        updates_made += 1
    
    # Write updated content
    with open(editorial_path, 'w') as f:
        f.write(content)
    
    print(f"✓ Editorial updated ({updates_made} replacements made)")


def process_tri_002():
    """Generate all images for TRI-002, upload to Cloudinary, and update editorial."""
    problem_id = "TRI-002"
    output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    output_dir.mkdir(exist_ok=True)
    
    editorial_path = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-002-longest-common-prefix-one-deletion.md")
    
    # Try to use better model if available, fallback to flash
    model = "gemini-2.0-flash-exp-image-generation"  # Will check if better models available
    
    image_urls = {}
    
    for image_name, prompt in TRI_002_PROMPTS.items():
        # Generate image locally
        local_path = output_dir / f"{problem_id}-{image_name}.png"
        
        if not generate_image(GOOGLE_API_KEY, prompt, str(local_path), model):
            print(f"Skipping {image_name} due to generation error")
            continue
        
        # Check if file exists and has content
        if not local_path.exists() or local_path.stat().st_size == 0:
            print(f"✗ Generated file is empty or doesn't exist: {local_path}")
            continue
            
        # Small delay to avoid rate limiting
        time.sleep(2)
        
        # Upload to Cloudinary in Tries/TRI-002 folder
        cloudinary_folder = f"Tries/{problem_id}"
        url = upload_to_cloudinary(str(local_path), cloudinary_folder)
        
        if url:
            image_urls[image_name] = url
    
    # Update editorial with URLs
    if image_urls:
        update_editorial_markdown(editorial_path, image_urls)
        print(f"\n✓ Successfully processed {len(image_urls)} images for {problem_id}")
    else:
        print(f"\n✗ No images were successfully uploaded to Cloudinary for {problem_id}")
        print(f"Generated images saved in: {output_dir}")
    
    return len(image_urls)


def main():
    print("=" * 60)
    print("TRI-002 Editorial Image Generation")
    print("=" * 60)
    print()
    
    success_count = process_tri_002()
    
    print()
    print("=" * 60)
    print(f"Complete: {success_count}/4 images generated and uploaded")
    print("=" * 60)


if __name__ == "__main__":
    main()
