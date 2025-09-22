from tqdm import tqdm
import os
from text_cleaning import clean_text

OUTPUT_FOLDER = "extracted_articles"
CLEANED_FOLDER = "cleaned_articles"
os.makedirs(CLEANED_FOLDER, exist_ok=True)

# Already cleaned files
cleaned_files = {f.replace(".txt", "") for f in os.listdir(CLEANED_FOLDER) if f.endswith(".txt")}

cleaned_texts = {}

# Only process files that exist but aren't cleaned yet
files_to_process = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".txt") and f.replace(".txt","") not in cleaned_files]

for file in tqdm(files_to_process, desc="Cleaning articles"):
    path = os.path.join(OUTPUT_FOLDER, file)
    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_text(raw_text)
    cleaned_texts[file] = cleaned

    # Save cleaned version
    with open(os.path.join(CLEANED_FOLDER, file), "w", encoding="utf-8") as f:
        f.write(cleaned)

# Optional: print first few cleaned texts
for k, v in list(cleaned_texts.items())[:3]:
    print(f"--- {k} ---")
    print(v[:300])  # first 300 characters
