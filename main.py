import pandas as pd
from data_extraction import save_articles, extract_article
from text_cleaning import clean_text
import os

# Load input Excel file
df = pd.read_excel("Input.xlsx")  # assumes columns URL_ID, URL

# Step 3: Extract articles **only if missing**
OUTPUT_FOLDER = "extracted_articles"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Get already extracted files (without .txt extension)
existing_files = {f.replace(".txt", "") for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".txt")}

# Filter dataframe to only URLs that are missing
df_missing = df[~df["URL_ID"].isin(existing_files)].reset_index(drop=True)

# Save missing articles
save_articles(df_missing)

# Step 5: Load all saved articles and clean them
cleaned_texts = {}
for file in os.listdir(OUTPUT_FOLDER):
    if file.endswith(".txt"):
        path = os.path.join(OUTPUT_FOLDER, file)
        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()
        cleaned_texts[file] = clean_text(raw_text)

# Optional: print first few cleaned texts
for k, v in list(cleaned_texts.items())[:3]:
    print(f"--- {k} ---")
    print(v[:300])  # first 300 characters
