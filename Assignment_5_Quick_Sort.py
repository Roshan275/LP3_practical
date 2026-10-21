"""Assignment 5: deterministic and randomized quicksort."""

# PRACTICAL TEST INPUT
# Run: python3 Assignment_5_Quick_Sort.py
# At the prompt, type: 8 3 5 1 9 2
# Both algorithms should print the sorted list: [1, 2, 3, 5, 8, 9].

import random


def quicksort_deterministic(values):
    """Sort in place, always selecting the last element as pivot."""
    def sort(low, high):
        if low >= high:
            return

        pivot = values[high]
        smaller_end = low - 1
        for current in range(low, high):
            if values[current] <= pivot:
                smaller_end += 1
                values[smaller_end], values[current] = values[current], values[smaller_end]

        pivot_position = smaller_end + 1
        values[pivot_position], values[high] = values[high], values[pivot_position]
        sort(low, pivot_position - 1)
        sort(pivot_position + 1, high)

    sort(0, len(values) - 1)
    return values


def quicksort_randomized(values):
    """Sort in place, choosing a random pivot for each partition."""
    def sort(low, high):
        if low >= high:
            return

        random_pivot = random.randint(low, high)
        values[random_pivot], values[high] = values[high], values[random_pivot]
        pivot = values[high]

        smaller_end = low - 1
        for current in range(low, high):
            if values[current] <= pivot:
                smaller_end += 1
                values[smaller_end], values[current] = values[current], values[smaller_end]

        pivot_position = smaller_end + 1
        values[pivot_position], values[high] = values[high], values[pivot_position]
        sort(low, pivot_position - 1)
        sort(pivot_position + 1, high)

    sort(0, len(values) - 1)
    return values


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Deterministic quicksort:", quicksort_deterministic(numbers.copy()))
    print("Randomized quicksort:   ", quicksort_randomized(numbers.copy()))
    print("Both average O(n log n), worst-case O(n^2); quicksort is not stable.")
    print("Average recursion space is O(log n); worst-case recursion space is O(n).")
