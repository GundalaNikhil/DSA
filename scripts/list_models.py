import sys
from google import genai

def list_models(api_key):
    client = genai.Client(api_key=api_key)
    try:
        for model in client.models.list():
            print(f"Model ID: {model.name}")
            # print(f"  Supported Actions: {model.supported_actions}")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 list_models.py <api_key>")
        sys.exit(1)
    list_models(sys.argv[1])
