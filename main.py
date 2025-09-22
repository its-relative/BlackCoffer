# main.py

import pandas as pd
from data_extraction import save_articles

# Load input Excel file
df = pd.read_excel("Input.xlsx")  # expects columns: URL_ID, URL

# Optional: Remove duplicate URLs, keep first occurrence
df = df.drop_duplicates(subset='URL', keep='first').reset_index(drop=True)

# Scrape and save all articles
save_articles(df)

print("All articles have been extracted and saved in the 'extracted_articles' folder.")
