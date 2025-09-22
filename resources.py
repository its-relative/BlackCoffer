# resources.py

import os

# ------------------------------
# Helper Functions
# ------------------------------

def load_stopwords(stopword_files):
    """
    Reads multiple stopword files and merges them into one set.
    Only the word before '|' (if present) is used, converted to lowercase.
    """
    all_stopwords = set()
    for file in stopword_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip().split("|")[0].lower()
                    if word:
                        all_stopwords.add(word)
        except UnicodeDecodeError:
            with open(file, 'r', encoding='latin-1') as f:
                for line in f:
                    word = line.strip().split("|")[0].lower()
                    if word:
                        all_stopwords.add(word)
    return all_stopwords


def load_sentiment_words(file_path):
    """
    Loads positive or negative word list into a set.
    Each word is expected to be on a separate line.
    """
    words = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.add(word)
    return words


# ------------------------------
# Load All Resources
# ------------------------------

stopwords_folder = "StopWords"

stopword_files = [
    os.path.join(stopwords_folder, "StopWords_Auditor.txt"),
    os.path.join(stopwords_folder, "StopWords_Currencies.txt"),
    os.path.join(stopwords_folder, "StopWords_DatesandNumbers.txt"),
    os.path.join(stopwords_folder, "StopWords_Generic.txt"),
    os.path.join(stopwords_folder, "StopWords_GenericLong.txt"),
    os.path.join(stopwords_folder, "StopWords_Geographic.txt"),
    os.path.join(stopwords_folder, "StopWords_Names.txt"),
]

all_stopwords = load_stopwords(stopword_files)

master_dict_folder = "MasterDictionary"
positive_words = load_sentiment_words(os.path.join(master_dict_folder, "positive-words.txt"))
negative_words = load_sentiment_words(os.path.join(master_dict_folder, "negative-words.txt"))

# ------------------------------
# Debug: Counts
# ------------------------------
print(f"Total stopwords loaded: {len(all_stopwords)}")
print(f"Total positive words: {len(positive_words)}")
print(f"Total negative words: {len(negative_words)}")
