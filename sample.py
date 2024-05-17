import pandas as pd

# Assuming you downloaded the dataset to 'idioms.csv'
data = pd.read_csv('idioms.csv')

# Select relevant columns (optional)
idioms = data[['phrase', 'definition']]



