def transform_data(df):
    try:
        # Remove null values
        df = df.dropna()

        # Standardize column names
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        print("Data transformed successfully")
        return df
    except Exception as e:
        print(f"Error in transformation: {e}")
        return None