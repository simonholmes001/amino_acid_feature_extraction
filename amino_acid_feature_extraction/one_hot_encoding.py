import pandas as pd
import numpy as np

INPUT_PATH = "./output" # Do I have to change to "./output" if called from feature_extraction.sh -> YES
OUTPUT_PATH = "./output" # Run as "../output" when running as an individual script, not as part of feature_extraction.sh
INPUT_CSV = "standardised_features.csv"
OUTPUT_CSV = "one_hot_encoded_features.csv"
OUTPUT_NUMPY = "one_hot_encoded"

class OneHotEncoding:

    def __init__(self, input_path, input_csv):
        self.input_path = input_path
        self.input_csv = input_csv

        df_standardised_features = pd.read_csv(self.input_path + '/' + self.input_csv)

        # One hot encode CID column
        df = pd.get_dummies(df_standardised_features['CID'])

        df_join = pd.concat([df, df_standardised_features], axis=1, join='inner') # Join the databases
        df_join.drop('CID', axis=1, inplace=True)

        df_join.to_csv(OUTPUT_PATH + '/' + OUTPUT_CSV, encoding='utf-8', index=False) # Save joined data base to a csv file
        one_hot_encoded = df_join.to_numpy() # Convert pandas to numpy array
        np.save(OUTPUT_PATH + '/' + OUTPUT_NUMPY, one_hot_encoded) # Save numpy array to disk

def main():
    OneHotEncoding(INPUT_PATH, INPUT_CSV)

if __name__ == '__main__':
    main()
