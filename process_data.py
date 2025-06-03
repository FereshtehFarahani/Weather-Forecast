import pandas as pd 
def process_data(file_path):

    # Step 1: Load data and convert timestamp
    df = pd.read_csv(file_path)
    df['timestamp'] = df['timestamp'].str.strip()
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d_%H-%M-%S", errors='coerce')
    df['date'] = df['timestamp'].dt.date

    # Step 2: Clean data
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)  # or fillna if preferred

    # Step 3: aggregate data
    df = df.groupby(['date', 'city']).agg({
        'temperature': 'mean',
        'humidity': 'mean',
        'weather_description': lambda x: ', '.join(x.unique())
    }).reset_index()

    # Round numeric columns
    df['temperature'] = df['temperature'].round(2)
    df['humidity'] = df['humidity'].round(2)

    # Step 4: Save cleaned data
    df.to_csv("cleaned_data.csv", index=False)
