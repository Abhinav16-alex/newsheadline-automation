import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"Fetching news from: {URL}")

try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status() # Check for request errors

    # --- Step 2: Parse the HTML ---
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # --- DEBUGGING STEP: See what the scraper sees ---
    # print("First 500 characters of HTML received:")
    # print(soup.prettify()[:500])
    # print("-" * 20)

    # --- Step 3: Find and Extract Headlines ---
    # UPDATED: We are specifically looking for <h2> tags.
    # This is the line you would change if BBC updates its site again.
    headline_tags = soup.find_all('h2')

    headlines = []
    for tag in headline_tags:
        # Some tags might be empty, so we get the text and clean it.
        headline_text = tag.get_text(strip=True)
        # We only add non-empty headlines that are a reasonable length.
        if headline_text and len(headline_text) > 10:
            headlines.append(headline_text)

    # --- Step 4: Save Headlines to a .txt File ---
    if headlines:
        with open('headlines.txt', 'w', encoding='utf-8') as file:
            print(f" Found {len(headlines)} headlines. Saving to headlines.txt...")
            for headline in headlines:
                file.write(headline + '\n')
        print("Success! Headlines have been saved.")
    else:
        # This message will show if the 'find_all' command returned nothing.
        print("⚠ Could not find any headlines with the specified tag ('h2').")
        print("The website's structure has likely changed. Please inspect the page to find the correct tag/class.")

except requests.exceptions.RequestException as e:
    print(f" Error: Could not connect to the website. Details: {e}")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
