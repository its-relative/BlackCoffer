# save_results.py
import pandas as pd
from text_metrics import compute_all_metrics
import os

def save_all_metrics(output_folder="extracted_articles", cleaned_folder="cleaned_articles"):
    results = []

    for file in os.listdir(cleaned_folder):
        if file.endswith(".txt"):
            path = os.path.join(cleaned_folder, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            metrics = compute_all_metrics(text)
            metrics["URL_ID"] = file.replace(".txt", "")
            results.append(metrics)

    df_results = pd.DataFrame(results)
    df_results.to_excel("Final_Results.xlsx", index=False)
    df_results.to_csv("Final_Results.csv", index=False)
    return df_results
