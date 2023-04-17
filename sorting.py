import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        # vykonání operací se souborem v této části
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(rada):
    size = len(rada)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if rada[j] < rada[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (rada[ind], rada[min_index]) = (rada[min_index], rada[ind])
    return rada

def main():
    my_data = read_data("numbers.csv")
    print(my_data["series_1"])
    cisla = selection_sort(my_data["series_1"])
    print(cisla)
    pass


if __name__ == '__main__':
    main()
