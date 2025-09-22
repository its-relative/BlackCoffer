import os
import pandas as pd
from tqdm import tqdm
from data_extraction import save_articles
from text_cleaning import clean_text
from text_metrics import compute_all_metrics
from save_results import save_all_metrics



# -----------------------------
# Paths
# -----------------------------
INPUT_FILE = "Input.xlsx"
OUTPUT_FOLDER = "extracted_articles"
CLEANED_FOLDER = "cleaned_articles"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(CLEANED_FOLDER, exist_ok=True)

# -----------------------------
# Load input Excel
# -----------------------------
df = pd.read_excel(INPUT_FILE)  # assumes columns URL_ID, URL

# -----------------------------
# Extract missing articles
# -----------------------------
# Already extracted files (without .txt)
existing_files = {f.replace(".txt", "") for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".txt")}

# Filter dataframe to only missing URLs
df_missing = df[~df["URL_ID"].isin(existing_files)].reset_index(drop=True)

if not df_missing.empty:
    print(f"Extracting {len(df_missing)} missing articles...")
    save_articles(df_missing)
else:
    print("All articles already extracted.")

# -----------------------------
# Load already cleaned files
# -----------------------------
cleaned_texts = {}
for file in os.listdir(CLEANED_FOLDER):
    if file.endswith(".txt"):
        path = os.path.join(CLEANED_FOLDER, file)
        with open(path, "r", encoding="utf-8") as f:
            cleaned_texts[file] = f.read()

# -----------------------------
# Clean new articles
# -----------------------------
# Already cleaned file IDs (without .txt)
cleaned_files = {f.replace(".txt", "") for f in os.listdir(CLEANED_FOLDER) if f.endswith(".txt")}

# Only process articles that exist but aren't cleaned yet
files_to_process = [
    f for f in os.listdir(OUTPUT_FOLDER)
    if f.endswith(".txt") and f.replace(".txt", "") not in cleaned_files
]

if files_to_process:
    print(f"Cleaning {len(files_to_process)} new articles...")
    for file in tqdm(files_to_process, desc="Cleaning articles"):
        path = os.path.join(OUTPUT_FOLDER, file)
        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_text(raw_text)
        cleaned_texts[file] = cleaned

        # Save cleaned version
        with open(os.path.join(CLEANED_FOLDER, file), "w", encoding="utf-8") as f:
            f.write(cleaned)
else:
    print("No new articles to clean.")

# -----------------------------
# Optional: Print a few examples
# -----------------------------
print("\nFirst few cleaned texts:")
for k, v in list(cleaned_texts.items())[:3]:
    print(f"--- {k} ---")
    print(v[:300])  # first 300 characters

# results = {}
# for file, text in cleaned_texts.items():
#     results[file] = compute_all_metrics(text)

# # Convert to DataFrame if needed
# import pandas as pd
# df_metrics = pd.DataFrame.from_dict(results, orient='index')
# df_metrics.to_csv("article_metrics.csv", index=True)

df_results = save_all_metrics()
print("Results saved successfully!")
