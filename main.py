# main.py

from indexing import load_and_preprocess_data, build_index, get_index

# Dataset path
DATA_PATH = "./data/Hotel_Reviews.csv"

# True = Build index, False = Load existing index
BUILD_INDEX = False  #False forever

def initialize_index():
    if BUILD_INDEX:
        df = load_and_preprocess_data(DATA_PATH)
        # return build_index(df)  # Build index
    else:
        return get_index()  # Load index
