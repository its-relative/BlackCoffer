import re
from nltk.tokenize import word_tokenize
from resources import all_stopwords
import nltk

for resource in ['punkt', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)


def clean_text(text):
    """
    Tokenize, lowercase, remove stopwords, punctuations, and numbers
    """
    # Lowercase
    text = text.lower()

    # Remove numbers and special characters
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in all_stopwords]

    # Rejoin tokens
    cleaned_text = " ".join(tokens)
    return cleaned_text
