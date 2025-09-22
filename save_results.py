# save_results.py
import os
import pandas as pd
from text_metrics import compute_all_metrics

def save_all_metrics(input_file="Input.xlsx", cleaned_folder="cleaned_articles"):
    # Load original URLs
    df_input = pd.read_excel(input_file)  # columns: URL_ID, URL

    results = []

    for file in os.listdir(cleaned_folder):
        if file.endswith(".txt"):
            path = os.path.join(cleaned_folder, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            metrics = compute_all_metrics(text)
            metrics["URL_ID"] = file.replace(".txt", "")
            results.append(metrics)

    df_metrics = pd.DataFrame(results)

    # Merge with URLs
    df_results = df_input.merge(df_metrics, on="URL_ID", how="left")

    # Reorder columns
    desired_columns = [
        "URL_ID",
        "URL",
        "POSITIVE SCORE",
        "NEGATIVE SCORE",
        "POLARITY SCORE",
        "SUBJECTIVITY SCORE",
        "AVG SENTENCE LENGTH",
        "PERCENTAGE OF COMPLEX WORDS",
        "FOG INDEX",
        "AVG NUMBER OF WORDS PER SENTENCE",
        "COMPLEX WORD COUNT",
        "WORD COUNT",
        "SYLLABLE PER WORD",
        "PERSONAL PRONOUNS",
        "AVG WORD LENGTH"
    ]

    # Map your keys to the desired column names
    key_map = {
        "Positive Score": "POSITIVE SCORE",
        "Negative Score": "NEGATIVE SCORE",
        "Polarity Score": "POLARITY SCORE",
        "Subjectivity Score": "SUBJECTIVITY SCORE",
        "Avg Sentence Length": "AVG SENTENCE LENGTH",
        "Percent Complex Words": "PERCENTAGE OF COMPLEX WORDS",
        "Fog Index": "FOG INDEX",
        "Avg Words per Sentence": "AVG NUMBER OF WORDS PER SENTENCE",
        "Complex Word Count": "COMPLEX WORD COUNT",
        "Word Count": "WORD COUNT",
        "Syllables per Word": "SYLLABLE PER WORD",
        "Personal Pronouns": "PERSONAL PRONOUNS",
        "Avg Word Length": "AVG WORD LENGTH"
    }

    df_results.rename(columns=key_map, inplace=True)
    df_results = df_results[desired_columns]

    # Save to Excel & CSV
    df_results.to_excel("Final_Results.xlsx", index=False)
    df_results.to_csv("Final_Results.csv", index=False)

    return df_results
