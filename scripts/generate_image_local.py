import sys
import os
import base64
from google import genai
from google.genai import types

def generate_image_local(api_key, prompt, output_path):
    client = genai.Client(api_key=api_key)
    
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
                img_data = base64.b64decode(part.inline_data.data)
                with open(output_path, "wb") as f:
                    f.write(img_data)
                print(f"Image saved to {output_path}")
                return
        print("No image found in response.")
        
    except Exception as e:
        print(f"Error generating image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image_local.py <prompt> <output_path> [api_key]")
        sys.exit(1)
        
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    api_key = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("GOOGLE_API_KEY")
    
    if not api_key:
        print("Error: API Key not provided. Set GOOGLE_API_KEY env var or pass as argument.")
        sys.exit(1)
        
    generate_image_local(api_key, prompt, output_path)
