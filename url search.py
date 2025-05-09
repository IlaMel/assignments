import requests
from bs4 import BeautifulSoup
import re

DANGEROUS_WORDS = {"bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"}

def count_dangerous_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return sum(word in DANGEROUS_WORDS for word in words)

def main():
    url = input("Give me a valid URL to download?").strip()
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        print(f"Error opening url: {url}")
        return

    content_type = response.headers.get("Content-Type", "")
    is_html = "text/html" in content_type.lower()
    is_utf8 = "charset=utf-8" in content_type.lower() or response.encoding and response.encoding.lower() == "utf-8"

    if is_html and is_utf8:
      
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            texts = soup.stripped_strings
            full_text = " ".join(texts)
            count = count_dangerous_words(full_text)
            print(f"Number of dangerous words: {count}")
        except Exception:
            print("Error parsing HTML.")
            return
    else:
        print("Doesn't appear to be an HTML file with utf-8 encoding.")

    save_path = input("Give me a valid path to save the contents?").strip()
    try:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Saving succeeded to: {save_path}")
    except Exception:
        print("Saving failed.")

if __name__ == "__main__":
    main()