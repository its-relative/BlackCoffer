Text Analysis Pipeline
=====================

Overview
--------
This project automates the process of extracting, cleaning, analyzing, and saving metrics from online articles. The pipeline computes sentiment analysis, readability analysis, and other textual metrics for a collection of articles provided via an input Excel file.

Features
--------
1. Article Extraction
   - Extracts articles from URLs listed in Input.xlsx.
   - Saves raw text files in extracted_articles/.

2. Text Cleaning
   - Cleans raw articles: removes unnecessary characters, extra whitespace, etc.
   - Saves cleaned text files in cleaned_articles/.

3. Text Metrics
   - Computes:
     - Sentiment Metrics: Positive, Negative, Polarity, Subjectivity.
     - Readability Metrics: Average sentence length, percentage of complex words, Fog index.
     - Other Metrics: Word count, complex words, syllables per word, personal pronouns, average word length.

4. Results Compilation
   - Merges computed metrics with URLs.
   - Saves results in both Excel (Final_Results.xlsx) and CSV (Final_Results.csv).

Folder Structure
----------------
cleaned_articles/       # Cleaned article text files
extracted_articles/     # Raw extracted article text files
Input.xlsx              # Input file with URL_ID and URL columns
text_cleaning.py        # Text cleaning functions
text_metrics.py         # Functions to compute text metrics
save_results.py         # Save metrics to Excel/CSV
data_extraction.py      # Functions to extract articles from URLs
main.py                 # Main execution script
Final_Results.xlsx      # Output metrics (generated)
Final_Results.csv       # Output metrics (generated)
resources.py            # Positive/negative word lists

Usage
-----
1. Install required packages:
   pip install pandas nltk textblob tqdm openpyxl

2. Place your input Excel file as Input.xlsx in the repo root.

3. Run the pipeline:
   python main.py

4. Outputs will be saved as:
   - Final_Results.xlsx
   - Final_Results.csv

Notes
-----
- Ensure NLTK resources 'punkt' and 'punkt_tab' are available. The code will download them automatically if missing.
- Cleaned and extracted articles are stored separately to avoid redundant processing.
