#  BBC News Headline Scraper

This Python script fetches the latest headlines from [BBC News](https://www.bbc.com/news) and saves them to a `.txt` file. It's designed to be beginner-friendly, modular, and easy to customize if the website structure changes.

---

##  Features

- Fetches live headlines from BBC News
- Filters out short or empty headlines
- Saves results to a timestamped `.txt` file
- Includes error handling for network issues
- Easily customizable for other news sites

---

## Getting Started

### Prerequisites

Make sure you have Python 3 installed and the following libraries:

```bash
pip install requests beautifulsoup4
```

### How to Run

```bash
python bbc_headline_scraper.py
```

After running, you'll see a file like `headlines_2025-09-15_18-58-00.txt` containing the latest headlines.

---

## How It Works

1. **Send HTTP Request**  
   Uses `requests` with a custom `User-Agent` to mimic a browser.

2. **Parse HTML**  
   Uses `BeautifulSoup` to parse the page content.

3. **Extract Headlines**  
   Finds all `<h2>` tags (or specific classes like `'gs-c-promo-heading__title'`) and filters meaningful headlines.

4. **Save to File**  
   Writes the headlines to a `.txt` file with UTF-8 encoding.

---

##  Customization Tips

- **Change Target Tags**  
  If BBC updates its layout, modify this line:
  ```python
  soup.find_all('h2', class_='gs-c-promo-heading__title')
  ```

- **Add URLs to Headlines**  
  You can also extract links using:
  ```python
  tag.get('href')
  ```

- **Retry on Failure**  
  Add retry logic using `requests.adapters` for better reliability.

---

##  Output Example


 Found 15 headlines. Saving to headlines_2025-09-15_18-58-00.txt...
Success! Headlines have been saved.

## ⚠ Troubleshooting

- If no headlines are found, the site structure may have changed.
- Check the HTML manually using:
  ```python
  print(soup.prettify()[:500])

##  License

This project is open-source and free to use for educational and personal purposes.

##  Author

Crafted with clarity and simplicity by Shanmukha
