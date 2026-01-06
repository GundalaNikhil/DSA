#!/usr/bin/env python3
"""
Generate explanatory images for Tries editorials using Google AI Studio,
upload to Cloudinary, and update markdown files with the URLs.

FIXED VERSION: Handles binary image data correctly (no base64 decode needed)
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

# API Credentials (from existing scripts)
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

# Image prompts for TRI-001
TRI_001_PROMPTS = {
    "real-world-scenario": """Simple hand-drawn sketch style diagram showing an e-commerce search autocomplete scenario. Draw a simple search bar at the top with "he" typed in it. Below it, show 3 suggestion boxes appearing as a dropdown: "he" (with a small "recent" tag), "hello" (with "popular" tag), and "helium" (with "trending" tag). Use excalidraw aesthetic - rough hand-drawn lines, simple shapes, minimal colors (black lines, light blue accents). Add small icons: a clock for recency, a star for popularity. Keep it clean, whiteboard-style, like a product design sketch.""",
    
    "algorithm-visualization": """Technical hand-drawn sketch of a Trie data structure for autocomplete. Draw a tree structure with nodes represented as simple circles. Root node at top, with 'h' as child, then 'e' below that. From 'e', show branches to 'l' (two branches - one leading to "hello" and one to "helium"). Mark complete words with small boxes containing metadata: "freq=5, t=0" for hello, "freq=3, t=5" for helium, "freq=4, t=9" for he. Use simple black lines, hand-drawn style, annotate with arrows and labels. Add a legend box showing "○ = node, □ = word end + metadata ". Keep it minimal, sketch-like, educational diagram style.""",
    
    "decay-calculation": """Whiteboard-style flowchart showing decay score calculation process. Draw 3 columns representing 3 words: "he", "hello", "helium". For each column, show step-by-step calculation boxes connected by arrows: 
1. Top box: word with its frequency and timestamp
2. Middle box: decay formula "freq × e^(-(10-t)/10)" with numbers filled in
3. Bottom box: final score (3.62 for "he", 1.84 for "hello", 1.82 for "helium")
At the bottom, show a ranking arrow pointing to "he" (1st), "hello" (2nd), "helium" (3rd). Use marker-on-whiteboard aesthetic - bold simple lines, blue and black colors, clean boxes, hand-drawn arrows. Add currentTime=10, D=10 as parameters at top.""",
    
    "test-walkthrough": """Simple hand-drawn test case walkthrough diagram showing the autocomplete algorithm execution. At top, show input parameters in a dashed box: "prefix='he', currentTime=10, D=10, k=2". Below, draw the process in 4 steps as simple sketched boxes:
Step 1: "Navigate to 'he' node" (small trie snippet with h→e highlighted)
Step 2: "Collect matches" (show ["he", "hello", "helium"] in a list)
Step 3: "Calculate scores" (show 3 simple bars of different heights labeled with scores: 3.62, 1.84, 1.82)
Step 4: "Return top 2" (highlight "he" and "hello" with checkmarks)
Connect steps with hand-drawn arrows. Use minimalist sketch style, black lines with light color accents (green for checkmarks, blue for highlights). Blueprint/technical sketch aesthetic."""
}


def generate_image(api_key, prompt, output_path):
    """Generate an image using Google AI Studio API."""
    client = genai.Client(api_key=api_key)
    
    print(f"Generating image: {output_path}")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )
        
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                # FIXED: inline_data.data is already binary bytes, not base64!
                img_data = part.inline_data.data
                
                with open(output_path, "wb") as f:
                    f.write(img_data)
                print(f"✓ Image saved to {output_path} ({len(img_data)} bytes)")
                return True
        
        print(f"✗ No image found in response for {output_path}")
        return False
        
    except Exception as e:
        print(f"✗ Error generating image: {e}")
        return False


def upload_to_cloudinary(image_path, folder):
    """Upload an image to Cloudinary and return the URL."""
    print(f"Uploading to Cloudinary: {folder}/")
    try:
        # Upload with explicit format
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
        import traceback
        traceback.print_exc()
        return None


def update_editorial_markdown(editorial_path, image_urls):
    """Update editorial markdown file with Cloudinary image URLs."""
    print(f"Updating editorial: {editorial_path}")
    
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    # Replace placeholder image paths with Cloudinary URLs
    # Pattern: ![caption](../images/TRI-001/filename.png)
    
    if 'real-world-scenario' in image_urls:
        content = re.sub(
            r'!\[Real-World Application\]\(\.\.\/images\/TRI-001\/real-world-scenario\.png\)',
            f'![Real-World Application]({image_urls["real-world-scenario"]})',
            content
        )
    
    if 'algorithm-visualization' in image_urls:
        content = re.sub(
            r'!\[Algorithm Visualization\]\(\.\.\/images\/TRI-001\/algorithm-visualization\.png\)',
            f'![Algorithm Visualization]({image_urls["algorithm-visualization"]})',
            content
        )
    
    # Write updated content
    with open(editorial_path, 'w') as f:
        f.write(content)
    
    print(f"✓ Editorial updated with {len(image_urls)} image URLs")


def process_tri_001():
    """Generate all images for TRI-001, upload to Cloudinary, and update editorial."""
    problem_id = "TRI-001"
    # Save to artifacts directory for persistence
    output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
    output_dir.mkdir(exist_ok=True)
    
    editorial_path = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Tries/editorials/TRI-001-autocomplete-top-k-fresh.md")
    
    image_urls = {}
    
    for image_name, prompt in TRI_001_PROMPTS.items():
        # Generate image locally
        local_path = output_dir / f"{problem_id}-{image_name}.png"
        
        if not generate_image(GOOGLE_API_KEY, prompt, str(local_path)):
            print(f"Skipping {image_name} due to generation error")
            continue
        
        # Check if file exists and has content
        if not local_path.exists() or local_path.stat().st_size == 0:
            print(f"✗ Generated file is empty or doesn't exist: {local_path}")
            continue
            
        # Small delay to avoid rate limiting
        time.sleep(2)
        
        # Upload to Cloudinary in Tries/TRI-001 folder
        cloudinary_folder = f"Tries/{problem_id}"
        url = upload_to_cloudinary(str(local_path), cloudinary_folder)
        
        if url:
            image_urls[image_name] = url
        # Don't delete files - keep them for inspection
    
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
    print("Editorial Image Generation Pipeline v3 (FIXED)")
    print("=" * 60)
    print()
    
    success_count = process_tri_001()
    
    print()
    print("=" * 60)
    print(f"Pipeline complete: {success_count} images generated and uploaded")
    print("=" * 60)


if __name__ == "__main__":
    main()
