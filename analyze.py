import google.generativeai as genai
import base64
from tts import text_to_speech  # Import the TTS function
from private import API_KEY

# Configure API key
genai.configure(api_key=API_KEY)

TOKEN_LIMIT = 1000  # Reasonable limit for a 480p image description

def count_tokens(prompt) -> int:
    """Estimates the token count for the given prompt."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    try:
        token_usage = model.count_tokens(prompt)
        return token_usage.total_tokens
    except Exception as e:
        print("Error estimating token usage:", e)
        return 0  # Default to 0 if estimation fails

def analyze_image(image_path: str) -> str:
    """Analyzes an image and returns a description while tracking token usage."""
    print("Analyzing image...")
    try:
        with open(image_path, "rb") as image_file:
            img_data = base64.b64encode(image_file.read()).decode("utf-8")

        prompt = [
            {"mime_type": "image/jpeg", "data": img_data},
            {"text": "Describe what is in the image."}
        ]

        # Estimate token usage before sending request
        tokens_used = count_tokens(prompt)
        print(f"Estimated token usage: {tokens_used}")

        if tokens_used > TOKEN_LIMIT:
            return f"Token usage exceeds limit ({tokens_used}/{TOKEN_LIMIT}). Request aborted."

        model = genai.GenerativeModel("gemini-2.0-flash")
        result = model.generate_content(prompt)

        return result.text.strip() if hasattr(result, "text") else "No valid response."

    except Exception as e:
        print("Error generating content:", e)
        return "Error analyzing image."

if __name__ == "__main__":
    image_path = "/home/pi3b/Cornerstone/test_photo.jpg"
    description = analyze_image(image_path)
    print("Image Description:", description)

    # Pass the description to TTS
    text_to_speech(description)
