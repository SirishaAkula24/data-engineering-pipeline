from extract import extract_data
from transform import transform_data

def run_pipeline():
    df = extract_data("data/data.csv")

    if df is not None:
        df_clean = transform_data(df)
        print(df_clean.head())

if __name__ == "__main__":
    run_pipeline()