import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler

INPUT_PATH = "./output" # Do I have to change to "./output" if called from feature_extraction.sh -> YES
OUTPUT_PATH = "./output" # Run as "../output" when running as an individual script, not as part of feature_extraction.sh
INPUT_CSV = "features.csv"
OUTPUT_CSV = "standardised_features.csv"

class StandardiseFeatures:

    def __init__(self, input_path, input_csv):
        self.input_path = input_path
        self.input_csv = input_csv


        df_non_standardised_features = pd.read_csv(self.input_path + '/' + self.input_csv)

        # Save the variable you don't want to scale
        name_var = df_non_standardised_features['CID']

        scaler = StandardScaler()
        scaled_values = scaler.fit_transform(df_non_standardised_features.drop('CID', axis = 1))

        df_standardised_features = pd.DataFrame(scaled_values, index = df_non_standardised_features.index, columns = df_non_standardised_features.drop('CID', axis = 1).columns)
        df_standardised_features['CID'] = name_var

        colnames = df_standardised_features.columns.tolist() # Print our column names
        colnames = colnames[-1:] + colnames[:-1] # Reorder column names to put the last column first
        df_standardised_features = df_standardised_features[colnames] # Reassign column names

        # print(df_non_standardised_features.head())
        # print(df_standardised_features.head())
        # print(df_non_standardised_features.shape)
        # print(df_standardised_features.shape)

        df_standardised_features.to_csv(OUTPUT_PATH + '/' + OUTPUT_CSV, encoding='utf-8', index=False) # Save joined data base to a csv file

def main():
    StandardiseFeatures(INPUT_PATH, INPUT_CSV)

if __name__ == '__main__':
    main()
