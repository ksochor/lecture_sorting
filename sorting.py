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


def selection_sort(rada, direction):
    if direction == "vz":
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
    elif direction == "ss":
        size = len(rada)
        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                # select the minimum element in every iteration
                if rada[j] < rada[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (rada[ind], rada[min_index]) = (rada[min_index], rada[ind])
        return rada[::-1]
    else:
        zprava = "Invalid input"
        return zprava


def bubble_sort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return elements
    return elements


def insertion_sort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    my_data = read_data("numbers.csv")
    print(my_data["series_1"])
    cisla = selection_sort(my_data["series_1"], "vz")
    print(f"{cisla}: selection_sort")
    bubble = bubble_sort(my_data["series_1"].copy())
    print(f"{bubble}: bubble_sort")
    insertion = insertion_sort(my_data["series_1"].copy())
    print(f"{insertion}: insertion_sort")
    pass


if __name__ == '__main__':
    main()
