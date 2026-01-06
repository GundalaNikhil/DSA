
import os
import requests
from google import genai
from google.genai import types

# Configuration
GOOGLE_API_KEY = "AIzaSyArgfdzbWUOpaoYqg9_DnAcNeUt7j6Zg9k"
client = genai.Client(api_key=GOOGLE_API_KEY)

def analyze_image_style(image_url):
    print(f"Downloading reference image from {image_url}...")
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        
        image_data = response.content
        
        prompt = (
            "Analyze this technical illustration for a coding problem. "
            "Describe its visual style, level of detail, color palette, and how it represents data structures or algorithms. "
            "What makes it 'dead accurate'? "
            "Provide a prompt that would generate an image in this exact style."
        )

        print("Analyzing with Gemini 2.0 Flash...")
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=[prompt, types.Part.from_bytes(data=image_data, mime_type="image/png")]
        )
        
        print("\n--- Analysis Result ---")
        print(response.text)
        return response.text

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = "https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_001.jpg" # Correct URL from file
    analyze_image_style(url)
