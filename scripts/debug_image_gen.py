#!/usr/bin/env python3
"""
Debug version - check what Google AI Studio API is actually returning
"""

import sys
import os
import base64
from pathlib import Path
from google import genai
from google.genai import types

GOOGLE_API_KEY = "AIzaSyArgfdzbWUOpaoYqg9_DnAcNeUt7j6Zg9k"

def test_image_generation():
    client = genai.Client(api_key=GOOGLE_API_KEY)
    
    prompt = "Simple hand-drawn sketch of a tree with 3 nodes labeled A, B, C"
    
    print("Sending request to Google AI Studio...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )
        
        print(f"\nResponse received!")
        print(f"Number of candidates: {len(response.candidates)}")
        
        if response.candidates:
            candidate = response.candidates[0]
            print(f"Number of parts: {len(candidate.content.parts)}")
            
            for i, part in enumerate(candidate.content.parts):
                print(f"\nPart {i}:")
                if hasattr(part, 'text') and part.text:
                    print(f"  - Has text: {part.text[:100]}...")
                if hasattr(part, 'inline_data') and part.inline_data:
                    print(f"  - Has inline_data")
                    print(f"  - MIME type: {part.inline_data.mime_type}")
                    print(f"  - Data length: {len(part.inline_data.data)} chars")
                    
                    # Try to decode and save
                    try:
                        img_data = base64.b64decode(part.inline_data.data)
                        print(f"  - Decoded length: {len(img_data)} bytes")
                        print(f"  - First 20 bytes (hex): {img_data[:20].hex()}")
                        
                        # Save to file
                        output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
                        output_dir.mkdir(exist_ok=True)
                        
                        # Determine extension based on MIME type
                        ext = "jpg" if "jpeg" in part.inline_data.mime_type.lower() else "png"
                        output_path = output_dir / f"debug_test.{ext}"
                        
                        with open(output_path, "wb") as f:
                            f.write(img_data)
                        
                        print(f"  - Saved to: {output_path}")
                        
                        # Verify file
                        import subprocess
                        result = subprocess.run(["file", str(output_path)], capture_output=True, text=True)
                        print(f"  - File type: {result.stdout.strip()}")
                        
                    except Exception as e:
                        print(f"  - Error decoding: {e}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_image_generation()
