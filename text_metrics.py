# ==============================
# text_metrics.py
# ==============================
# Computes:
# 1. Sentiment Analysis
# 2. Readability Analysis
# 3. Other Metrics (word/syllable counts, pronouns, etc.)
# ==============================

import re
from textblob import TextBlob
from resources import positive_words, negative_words
import nltk

for resource in ['punkt', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

# ------------------------------
# 1. Sentiment Analysis
# ------------------------------
def sentiment_analysis(text):
    words = text.split()
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    polarity = (pos_count - neg_count) / (pos_count + neg_count + 1e-6)
    subjectivity = TextBlob(text).sentiment.subjectivity
    return {
        "Positive Score": pos_count,
        "Negative Score": neg_count,
        "Polarity Score": polarity,
        "Subjectivity Score": subjectivity
    }

# ------------------------------
# 2. Readability Analysis
# ------------------------------
def readability_analysis(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    words = text.split()
    num_sentences = len(sentences) or 1  # avoid division by zero
    num_words = len(words)
    
    # Average sentence length
    avg_sentence_len = num_words / num_sentences
    
    # Percentage of complex words (3+ syllables)
    complex_words = [w for w in words if count_syllables(w) >= 3]
    percent_complex = len(complex_words) / (num_words + 1e-6) * 100
    
    # Fog index
    fog_index = 0.4 * (avg_sentence_len + percent_complex)
    
    return {
        "Avg Sentence Length": avg_sentence_len,
        "Percent Complex Words": percent_complex,
        "Fog Index": fog_index
    }

# ------------------------------
# 3. Other Metrics
# ------------------------------
def other_metrics(text):
    words = text.split()
    num_sentences = len(nltk.tokenize.sent_tokenize(text)) or 1
    num_words = len(words)
    syllable_counts = [count_syllables(w) for w in words]
    avg_syllables_per_word = sum(syllable_counts) / (num_words + 1e-6)
    
    # Personal pronouns
    personal_pronouns = re.findall(r'\b(I|we|my|ours|us)\b', text, flags=re.I)
    
    return {
        "Avg Words per Sentence": num_words / num_sentences,
        "Complex Word Count": len([w for w in words if count_syllables(w) >= 3]),
        "Word Count": num_words,
        "Syllables per Word": avg_syllables_per_word,
        "Personal Pronouns": len(personal_pronouns),
        "Avg Word Length": sum(len(w) for w in words) / (num_words + 1e-6)
    }

# ------------------------------
# Helper: Count Syllables
# ------------------------------
def count_syllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev_char_was_vowel = False
    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if word.endswith("e"):
        count = max(1, count-1)
    return max(1, count)

# ------------------------------
# 4. Compute All Metrics
# ------------------------------
def compute_all_metrics(text):
    metrics = {}
    metrics.update(sentiment_analysis(text))
    metrics.update(readability_analysis(text))
    metrics.update(other_metrics(text))
    return metrics
