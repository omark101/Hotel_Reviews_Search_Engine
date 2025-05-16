from sentence_transformers import SentenceTransformer, util
from collections import Counter
import nltk
import numpy as np
import string


from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

print("Loading BERT model...")
bert = SentenceTransformer('all-MiniLM-L6-v2')

VOCAB_EMBEDDINGS = {}
cache = {}


def build_dynamic_vocab(df, top_n=100):
    text = " ".join(df['text'])
    words = nltk.word_tokenize(text.lower())
    words = [w for w in words if w not in stop_words and w.isalpha()]
    common = [word for word, _ in Counter(words).most_common(top_n)]

    print(f" Building vocab of top {top_n} words")
    embeddings = bert.encode(common)
    for word, emb in zip(common, embeddings):
        VOCAB_EMBEDDINGS[word] = emb


def expand_query(query, top_k=3):
    if query in cache:
        return cache[query]

    try:
        query_vec = bert.encode(query)
        similarities = [
            (w, float(util.cos_sim(query_vec, vec)))
            for w, vec in VOCAB_EMBEDDINGS.items()
        ]
        top_related = sorted(similarities, key=lambda x: -x[1])[:top_k]
        expansion = query + " " + " ".join([w for w, _ in top_related])
        print(f"🔍 Expanded Query: {expansion}")
        cache[query] = expansion
        return expansion
    except Exception as e:
        print(f" BERT Expansion failed: {e}")
        return query
