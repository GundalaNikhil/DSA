import cloudinary
import cloudinary.uploader
import sys
import os

def upload_image(image_path, cloud_name, api_key, api_secret, folder=None):
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    try:
        options = {}
        if folder:
            options['folder'] = folder
            
        response = cloudinary.uploader.upload(image_path, **options)
        print(f"URL: {response['secure_url']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 upload_cloudinary.py <image_path> <cloud_name> <api_key> <api_secret> [folder]")
        sys.exit(1)

    image_path = sys.argv[1]
    cloud_name = sys.argv[2]
    api_key = sys.argv[3]
    api_secret = sys.argv[4]
    folder = sys.argv[5] if len(sys.argv) > 5 else None

    upload_image(image_path, cloud_name, api_key, api_secret, folder)


#dbname: dy4dvna3t
#api_key: 422129878775651
#api_secret: sBGz50Rxzzwk9pFAMFxyjvQN5uk

#google ai studio 
# API_KEY: AIzaSyArgfdzbWUOpaoYqg9_DnAcNeUt7j6Zg9k