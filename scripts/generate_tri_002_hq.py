#!/usr/bin/env python3
"""
TRI-002 Image Generation - HIGH QUALITY VERSION
Uses best available model with emphasis on clear, readable text.
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

# Enhanced prompts with emphasis on CLEAR, READABLE TEXT
TRI_002_PROMPTS = {
    "real-world-scenario": """Create a clear, professional hand-drawn diagram showing a Git version control scenario.

LAYOUT (3 sections horizontally):
Left: Developer workspace showing branch "feature/xuser-auth" with the extra 'x' circled in RED
Center: Developer workspace showing branch "feature/user-autz" with typo 'z' circled in RED  
Right: Developer workspace showing branch "feature/user-aauth" with duplicate 'a' circled in RED

Bottom: Large arrow pointing down to merged result showing "feature/user-a" in GREEN with clear label "Common prefix after 1 deletion"

STYLE:
- Hand-drawn excalidraw aesthetic but VERY CLEAR AND READABLE
- Large, legible text with good contrast
- Black text on white/light background
- Simple clean lines, minimal clutter
- Add small Git branch fork icons
- Label each section clearly: "Dev 1", "Dev 2", "Dev 3"

CRITICAL: All text must be LARGE and CLEARLY READABLE. This is a tutorial diagram.""",
    
    "trie-variants": """Create a clear technical diagram showing variant generation and trie structure.

TOP SECTION - "Variant Generation Example":
Show word "abc" with ALL its variants listed clearly:
• Original: abc
• Delete pos 0: bc
• Delete pos 1: ac  
• Delete pos 2: ab

BOTTOM SECTION - "Trie with Word ID Tracking":
Draw a clean tree structure:
- Circles for nodes
- Edges labeled with characters (a, b, c)
- At each node, show word IDs in curly braces: {0,1,2}
- Highlight the deepest node with all IDs with a STAR ★

Add clear legend box:
○ = Trie Node
{0,1,2} = Word IDs that pass through
★ = Longest common point

STYLE:
- Graph paper / grid background for clarity
- Large, bold text labels
- Clear node connections
- Professional technical diagram style
- ALL TEXT MUST BE LARGE AND READABLE

CRITICAL: This is an educational diagram. Text clarity is ESSENTIAL.""",
    
    "algorithm-flow": """Create a clear 3-column flowchart showing the algorithm phases.

COLUMN 1 - "Phase 1: Generate Variants" (BLUE header):
↓ Box: "For each word W:"
↓ Box: "Insert W → trie (mark with word_id)"
↓ Box: "For each position i:"
↓ Box: "Delete W[i] → variant V"
↓ Box: "Insert V → trie (mark with word_id)"

COLUMN 2 - "Phase 2: Find LCP" (GREEN header):
↓ Box: "DFS from trie root"
↓ Box: "Track prefix P"
↓ Box: "At each node N:"
↓ Box: "Check: All word_ids present?"
↓ Box: "If YES & len(P) > max:"
↓ Box: "Update: max_prefix = P"

COLUMN 3 - "Phase 3: Result" (ORANGE header):
↓ Box: "Return max_prefix"

STYLE:
- Whiteboard marker aesthetic
- LARGE, BOLD, CLEAR text in boxes
- Colored box backgrounds (light blue, light green, light orange)
- Thick black borders and arrows
- Clean, professional layout
- High contrast for readability

Example annotation below: "e.g., Node with IDs {0,1,2} = all 3 words"

CRITICAL: All text must be LARGE (18pt+) and CRYSTAL CLEAR. This is a teaching diagram.""",
    
    "test-walkthrough": """Create a detailed, clear step-by-step walkthrough diagram.

TOP - Input Section (dashed box):
Input words: ["abc", "axbc", "abxc"]
Goal: Find longest common prefix with ≤1 deletion per word

STEP 1 - "Variant Generation":
Word 0 "abc"  → variants: abc, bc, ac, ab
Word 1 "axbc" → variants: axbc, xbc, abc, axc, abc  
Word 2 "abxc" → variants: abxc, bxc, axc, abc, abc

STEP 2 - "Trie Structure":
Draw clean tree:
Root
  ↓
  a {0,1,2}
  ↓
  b {0,1,2} ★ ← ALL 3 WORDS REACH HERE
  ↓
  c {0,1}

STEP 3 - "Result":
Longest common prefix = "ab"

Show transformations clearly:
• "abc"  → "ab" (no deletion needed)
• "axbc" → "ab" (delete 'x' at pos 1)
• "abxc" → "ab" (delete 'x' at pos 2)

STYLE:
- Clean hand-drawn style
- Step numbers in LARGE circles
- Green checkmarks ✓ for correct matches
- Tree with thick lines and clear labels
- High contrast, easy to read
- Educational poster quality

CRITICAL: This is a tutorial walkthrough. Every piece of text must be LARGE, BOLD, and PERFECTLY READABLE. No tiny text!"""
}


def generate_image(api_key, prompt, output_path, model="imagen-3-fast-generate-001"):
    """Generate high-quality image using specified model."""
    client = genai.Client(api_key=api_key)
    
    print(f"\nGenerating with {model}...")
    print(f"Output: {output_path}")
    
    # Try multiple models in order of preference
    models_to_try = [
        "imagen-3-fast-generate-001",  # Try imagen-3 first (if available)
        "gemini-2.5-flash-image",      # Newer image generation model
        "gemini-2.0-flash-exp-image-generation",  # Fallback
    ]
    
    for model_name in models_to_try:
        try:
            print(f"  Trying model: {model_name}")
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
                        print(f"  ✓ Success! Image saved ({len(img_data):,} bytes)")
                        return True
            
            print(f"  ✗ No image in response from {model_name}")
            
        except Exception as e:
            print(f"  ✗ {model_name} failed: {e}")
            continue
    
    print(f"  ✗ All models failed for this image")
    return False


def upload_to_cloudinary(image_path, folder):
    """Upload an image to Cloudinary and return the URL."""
    print(f"  Uploading to Cloudinary: {folder}/")
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


def update_editorial_markdown(editorial_path, image_urls):
    """Update editorial with image URLs."""
    print(f"\nUpdating editorial: {editorial_path.name}")
    
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    # Update images
    if 'real-world-scenario' in image_urls:
        content = re.sub(
            r'!\[Real-World Application\]\([^)]+\)',
            f'![Real-World Application]({image_urls["real-world-scenario"]})',
            content
        )
    
    if 'trie-variants' in image_urls:
        # Insert after the trie example code block
        pattern = r'(Result: "inter" \(depth 5, all word IDs present\)\s*```\s*\n)'
        replacement = f'\\1\n![Trie Variants and Word Tracking]({image_urls["trie-variants"]})\n'
        content = re.sub(pattern, replacement, content)
    
    if 'algorithm-flow' in image_urls:
        content = re.sub(
            r'!\[Algorithm Visualization\]\([^)]+\)',
            f'![Algorithm Flow Diagram]({image_urls["algorithm-flow"]})',
            content
        )
    
    if 'test-walkthrough' in image_urls:
        pattern = r'(### Common Mistakes to Avoid)'
        replacement = f'\n![Test Case Walkthrough]({image_urls["test-walkthrough"]})\n\n\\1'
        content = re.sub(pattern, replacement, content)
    
    with open(editorial_path, 'w') as f:
        f.write(content)
    
    print(f"  ✓ Editorial updated successfully")


def main():
    print("=" * 70)
    print("TRI-002 HIGH QUALITY IMAGE GENERATION")
    print("=" * 70)
    
    problem_id = "TRI-002"
    output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    output_dir.mkdir(exist_ok=True)
    
    editorial_path = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-002-longest-common-prefix-one-deletion.md")
    
    image_urls = {}
    total = len(TRI_002_PROMPTS)
    
    for i, (image_name, prompt) in enumerate(TRI_002_PROMPTS.items(), 1):
        print(f"\n[{i}/{total}] Processing: {image_name}")
        print("-" * 70)
        
        local_path = output_dir / f"{problem_id}-{image_name}-v2.png"
        
        if generate_image(GOOGLE_API_KEY, prompt, str(local_path)):
            if local_path.exists() and local_path.stat().st_size > 0:
                time.sleep(3)  # Rate limiting
                
                url = upload_to_cloudinary(str(local_path), f"Tries/{problem_id}")
                if url:
                    image_urls[image_name] = url
        
        print("-" * 70)
    
    # Update editorial
    if image_urls:
        update_editorial_markdown(editorial_path, image_urls)
        print(f"\n{'='*70}")
        print(f"SUCCESS: {len(image_urls)}/{total} images generated and embedded")
        print(f"{'='*70}")
    else:
        print(f"\n{'='*70}")
        print(f"ERROR: No images were successfully generated")
        print(f"{'='*70}")
    
    return len(image_urls)


if __name__ == "__main__":
    main()
