# data_extraction.py

import os
import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Folder where extracted articles will be saved
OUTPUT_FOLDER = "extracted_articles"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def extract_article(url):
    """
    Extracts the title and main content text from a Blackcoffer article.
    Removes "Contact Details" section if present.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None, None

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the article title
        title_tag = soup.find("h1", class_="entry-title")
        title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

        # Extract article content
        content_div = soup.find("div", class_="td-post-content")
        if not content_div:
            return title, ""

        # Remove "Contact Details" section if it exists
        contact_heading = content_div.find("h1", string=re.compile("Contact Details", re.I))
        if contact_heading:
            for elem in contact_heading.find_all_next():
                elem.decompose()
            contact_heading.decompose()

        # Clean text
        text = content_div.get_text(separator=" ", strip=True)
        return title, text

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None


def save_articles(df):
    """
    Loops through the DataFrame of URLs, scrapes each article, and saves it as a text file.
    Each file is named by its URL_ID.
    """
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        url_id = row["URL_ID"]
        url = row["URL"]

        title, text = extract_article(url)
        if text is None:
            continue

        # Combine title + text
        full_text = f"{title}\n\n{text}"

        # Save file
        file_path = os.path.join(OUTPUT_FOLDER, f"{url_id}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_text)
