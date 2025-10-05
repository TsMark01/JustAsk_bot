import requests
import json

# API configuration
BASE_URL = "https://api.deepseek.com"
API_KEY = ""
MODEL = "deepseek-chat"


def call_deepseek_api(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(
            f"{BASE_URL}/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None


def main():
    prompt = "Hello! Can you tell me about the benefits of using FastAPI for building APIs?"
    response = call_deepseek_api(prompt)

    if response and 'choices' in response:
        print("Response from DeepSeek API:")
        print(response['choices'][0]['message']['content'])
    else:
        print("Failed to get a valid response from the API.")


if __name__ == "__main__":
    main()
