import pandas as pd
import glob
import os

def load_data():
    # Looks into your data folder for the cleaned files
    path = 'data/' 
    all_files = glob.glob(os.path.join(path, "*_clean.csv"))
    df_list = []
    for filename in all_files:
        df = pd.read_csv(filename)
        country_name = os.path.basename(filename).split('_')[0].capitalize()
        df['Country'] = country_name
        df_list.append(df)
    full_df = pd.concat(df_list, ignore_index=True)
    full_df['Date'] = pd.to_datetime(full_df['Date'])
    return full_df