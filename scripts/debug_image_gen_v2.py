#!/usr/bin/env python3
"""
Debug version 2 - save the BASE64 data directly to check it
"""

import sys
import os
import base64
from pathlib import Path
from google import genai
from google.genai import types

GOOGLE_API_KEY = "AIzaSyArgfdzbWUOpaoYqg9_DnAcNeUt7j6Zg9k"

def test_image_generation_v2():
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
        
        if response.candidates:
            candidate = response.candidates[0]
            
            for i, part in enumerate(candidate.content.parts):
                if hasattr(part, 'inline_data') and part.inline_data:
                    print(f"\n--- Part {i} (inline_data) ---")
                    print(f"MIME type: {part.inline_data.mime_type}")
                    
                    # Get the base64 string
                    b64_data = part.inline_data.data
                    print(f"Base64 string length: {len(b64_data)} chars")
                    print(f"First 100 chars: {b64_data[:100]}")
                    print(f"Last 100 chars: {b64_data[-100:]}")
                    
                    # Save base64 data to file
                    output_dir = Path("/Users/nikhilgundala/.gemini/antigravity/brain/3076b095-e1ee-465d-afc7-a0d466ad5511/tri_images")
                    output_dir.mkdir(exist_ok=True)
                    
                    with open(output_dir / "debug_base64.txt", "w") as f:
                        f.write(b64_data)
                    print(f"Saved base64 to: {output_dir / 'debug_base64.txt'}")
                    
                    # Now decode properly
                    try:
                        img_data = base64.b64decode(b64_data)
                        print(f"\nDecoded binary length: {len(img_data)} bytes")
                        print(f"First 20 bytes (hex): {img_data[:20].hex()}")
                        
                        # Detect format from magic bytes
                        if img_data[:4] == b'\\x89PNG':
                            ext = "png"
                        elif img_data[:2] == b'\\xff\\xd8':
                            ext = "jpg"
                        elif img_data[:4] == b'RIFF':
                            ext = "webp"
                        else:
                            ext = "bin"
                            print(f"WARNING: Unknown format, magic bytes: {img_data[:4].hex()}")
                        
                        output_path = output_dir / f"debug_test_v2.{ext}"
                        with open(output_path, "wb") as f:
                            f.write(img_data)
                        
                        print(f"Saved to: {output_path}")
                        
                        # Verify file
                        import subprocess
                        result = subprocess.run(["file", str(output_path)], capture_output=True, text=True)
                        print(f"File type: {result.stdout.strip()}")
                        
                    except Exception as e:
                        print(f"Error decoding: {e}")
                        import traceback
                        traceback.print_exc()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_image_generation_v2()
