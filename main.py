"""
Project: Text Analysis Assignment
Objective: Extract text from URLs, clean it, and compute sentiment + readability metrics.
"""

# ==============================
# 1. Import Required Libraries
# ==============================
# (List of imports we will need later, e.g., requests, bs4, nltk, pandas, etc.)
"""
Step 1: Import Required Libraries
"""

# For data handling
import pandas as pd

# For web scraping
import requests
from bs4 import BeautifulSoup

# For text processing
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# For working with Excel
import openpyxl

# For handling file paths
import os


# ==============================
# 2. Load Input Data
# ==============================
# - Read Input.xlsx
# - Extract URL_ID and URL columns
# - Prepare dataframe for processing


# ==============================
# 3. Data Extraction
# ==============================
# - Loop through URLs
# - Scrape title + article text only
# - Save each article as text file (named by URL_ID)


# ==============================
# 4. Load Stopwords and Dictionaries
# ==============================
# - Read stopword files (Dates, Currencies, Auditor, Generic, GenericLong, Geographic, Names)
# - Merge into one master stopword set
# - Load Positive and Negative word lists


# ==============================
# 5. Text Cleaning
# ==============================
# - Tokenization
# - Lowercasing
# - Remove stopwords
# - Remove punctuations/numbers


# ==============================
# 6. Sentiment Analysis
# ==============================
# - Positive Score
# - Negative Score
# - Polarity Score
# - Subjectivity Score


# ==============================
# 7. Readability Analysis
# ==============================
# - Average Sentence Length
# - Percentage of Complex Words
# - Fog Index


# ==============================
# 8. Other Metrics
# ==============================
# - Average Number of Words Per Sentence
# - Complex Word Count
# - Word Count
# - Syllable Count Per Word
# - Personal Pronouns
# - Average Word Length


# ==============================
# 9. Save Results
# ==============================
# - Compile results into dataframe
# - Match Output Data Structure.xlsx format
# - Export final results to Excel/CSV


# ==============================
# 10. Main Execution Flow
# ==============================
# - Call functions step by step
# - Ensure correct order of operations
# - Save outputs
