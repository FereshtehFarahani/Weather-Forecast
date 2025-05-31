from fetch_data import fetch_data

def main():
    while True:
        fetch_data()
        if input("Do you want to continue? (yes/no): ").lower() == 'yes':
            continue
        else:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
