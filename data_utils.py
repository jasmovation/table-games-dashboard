import pandas as pd

def load_and_transform_data(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Ensure 'Date' is datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Optional: add derived fields (e.g. Month, Week)
    df['Month'] = df['Date'].dt.strftime('%B')
    df['Week'] = df['Date'].dt.isocalendar().week

    # Optional: clean column names or fill NAs
    df.fillna('', inplace=True)

    return df
