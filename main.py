from fetch_data import fetch_data
from process_data import process_data

def main():
    while True:
        fetch_data()
        if input("Do you want to continue? (yes/no): ").lower() == 'yes':
            continue
        else:
            print("Exiting the program.")
            break


if __name__ == "__main__":
    process_data('data/weather_log.csv')

