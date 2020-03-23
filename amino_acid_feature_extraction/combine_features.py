import pandas as pd

OUTPUT_PATH = "./output"
INPUT_TEXT = "data.txt"
INPUT_CSV = "test_data.csv"
OUTPUT_CSV = "features.csv"

df_text = pd.read_table(OUTPUT_PATH + '/' + INPUT_TEXT, delim_whitespace=True, names=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'))
df_text_transpose = df_text.T # data.txt has the 20 amino acids as columns but need the data to have the amino acids as rows, need to transform a 500 x 20 matrix to a 20 x 500 matrix
df_csv = pd.read_csv(OUTPUT_PATH + '/' + INPUT_CSV)

df_text_transpose.index = df_csv.index # Homogenize the index values
df_text_transpose[["CID_2"]] = df_csv[["CID"]] # Assign the columns

colnames = df_text_transpose.columns.tolist() # Print our column names
colnames = colnames[-1:] + colnames[:-1] # Reorder column names to put the last column first
df_text_transpose = df_text_transpose[colnames] # Reassign column names

df_join = pd.concat([df_csv, df_text_transpose], axis=1, join='inner') # Join the databases
df_join = df_join.drop("CID_2", axis=1)

df_join.to_csv(OUTPUT_PATH + '/' + OUTPUT_CSV, encoding='utf-8', index=False) # Save joined data base to a csv file

# print("The shape of df_csv is: {}".format(df_csv.shape))
# print("The shape of df_text is: {}".format(df_text.shape))
# print("The shape of df_text_transpose is: {}".format(df_text_transpose.shape))
# print("The shape of df_join is: {}".format(df_join.shape))
# print(26 + 565)
# print(df_join.head())

