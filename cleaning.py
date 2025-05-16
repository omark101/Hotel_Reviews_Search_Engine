# cleaning.py

import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Initialize NLP tools
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_text(text, apply_stemming=True, apply_lemmatization=True):
    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize
    words = nltk.word_tokenize(text)

    # Remove stopwords
    words = [w for w in words if w not in stop_words]

    # Stemming or Lemmatization
    if apply_stemming:
        words = [stemmer.stem(w) for w in words]
    if apply_lemmatization:
        words = [lemmatizer.lemmatize(w) for w in words]

    # Rejoin
    return " ".join(words)
