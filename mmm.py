"""Module for calculating the mean, median, and mode of a dataset"""


def calc_mean(numbers):
    """Calculates the mean of a set of numbers"""

    return sum(numbers) / len(numbers)


def calc_median(numbers):
    """Calculates the median of a set of numbers"""

    sorted_dataset = sorted(numbers)
    if len(sorted_dataset) % 2 == 0:
        #even
        upper_index = len(sorted_dataset) // 2
        lower_index = upper_index - 1
        upper_value = sorted_dataset[upper_index]
        lower_value = sorted_dataset[lower_index]
        median = (upper_value + lower_value) / 2

    else:
        #odd
        mid_index = len(sorted_dataset) // 2
        median = sorted_dataset[mid_index]

    return median


def calc_mode(numbers):
    """Calculates the mode of a set of numbers"""

    number_dict = {}
    for number in set(numbers):
        number_dict[number] = numbers.count(number)

    #what is the goal of the loop:
    #find the highest repeated value
    highest_value = -1
    for key, value in number_dict.items():
        if value > highest_value:
            highest_value = value

    #append modes with the key of highest value
    modes = []
    for key, value in number_dict.items():
        if value == highest_value:
            modes.append(key)

    return modes


def solve_problem(numbers):
    """Runs the functions that calculates the mean, median, and mode"""

    mean = calc_mean(numbers)
    median = calc_median(numbers)
    modes = calc_mode(numbers)

    return mean, median, modes


def main():
    """The main function containing the data and dataset"""

    datasets = (
        [5, 3, 1, 1, 2, 9, 6, 8, 4, 1, 3, 8, 7, 2, 3, 2],
        [5, 3, 1, 1, 2, 9, 6, 8, 4, 1, 3, 8, 7, 2, 3],
        [5, 3, 1, 1, 2, 9, 6, 8, 4, 1, 3, 8, 7]
    )

    for dataset in datasets:
        mean, median, modes = solve_problem(dataset)
        print(f"mean = {round(mean, 2)}, median = {round(median, 2)}, mode = {modes}")

if __name__ == "__main__":
    main()
