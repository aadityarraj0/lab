import csv

def read_csv_to_dict(filename):
    data = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for column in reader.fieldnames:
            data[column] = []

        for row in reader:
            for column in row:
                try:
                    data[column].append(float(row[column]))
                except ValueError:
                    data[column].append(row[column])

    return data


def get_max(data, column):
    return max(data[column])


def get_min(data, column):
    return min(data[column])


def get_average(data, column):
    return sum(data[column]) / len(data[column])


def main():
    filename = input("Enter CSV file name (example: data.csv): ")
    data = read_csv_to_dict(filename)

    print("\nAvailable columns:")
    for col in data:
        print("-", col)

    while True:
        print("\nChoose an operation:")
        print("1. Max")
        print("2. Min")
        print("3. Average")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "4":
            print("Program ended.")
            break

        column = input("Enter column name: ")

        if column not in data:
            print("Invalid column name.")
            continue

        try:
            if choice == "1":
                print("Maximum value:", get_max(data, column))
            elif choice == "2":
                print("Minimum value:", get_min(data, column))
            elif choice == "3":
                print("Average value:", get_average(data, column))
            else:
                print("Invalid choice.")
        except TypeError:
            print("This column does not contain numeric data.")


main()
