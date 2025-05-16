# indexing.py

import pandas as pd
import pyterrier as pt
from cleaning import preprocess_text
import os

# Initialize paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index", "hotel_reviews_index")

# Start PyTerrier
pt.java.init()




def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path, encoding='utf-8')

    df = df.dropna()

    # Create new docno
    df['docno'] = df.index.astype(str)

    # Clean Positive and Negative Reviews
    df['Processed_Positive'] = df['Positive_Review'].apply(preprocess_text)
    df['Processed_Negative'] = df['Negative_Review'].apply(preprocess_text)

    df['text'] = df['Processed_Positive'] + " " + df['Processed_Negative']

    return df[['docno', 'text', 'Hotel_Address', 'Hotel_Name', 'Reviewer_Nationality',
               'Positive_Review', 'Negative_Review', 'lat', 'lng']]


def build_index(df):
    print("DataFrame Columns: ", df.columns)
    print("Sample Row: ", df.iloc[0].to_dict())
    print("Index Path: ", INDEX_PATH)
    try:
        os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

        indexer = pt.IterDictIndexer(
            index_path=INDEX_PATH,
            overwrite=True,
            meta={
                'docno': 20,
                'Hotel_Name': 100,
                'Positive_Review': 2000,
                'Negative_Review': 2000,
                'Reviewer_Nationality': 50,
                'Hotel_Address': 200,
                'lat': 20,
                'lng': 20
            }
        )

        docs = []
        for _, row in df.iterrows():
            doc = {
                'docno': row['docno'],
                'text': row['text'],  #main
                'Hotel_Name': row['Hotel_Name'],
                'Positive_Review': row['Positive_Review'],
                'Negative_Review': row['Negative_Review'],
                'Reviewer_Nationality': row['Reviewer_Nationality'],
                'Hotel_Address': row['Hotel_Address'],
                'lat': str(row['lat']),
                'lng': str(row['lng'])
            }
            docs.append(doc)

        # Index the documents
        index_ref = indexer.index(docs)
        print("Indexing completed successfully")
        return pt.IndexFactory.of(index_ref)
    except Exception as e:
        print(f"  failed: {e}")
        raise


def get_index():
    return pt.IndexFactory.of(INDEX_PATH)