from typing import List

def even_list(int_list: List[int]) -> List[int]:
    return [num for num in int_list if num % 2 == 0]


# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list.
    Args:
        even_int_list: A list of even integers.
    Returns:
        The sum of the squares of all even numbers in the list.
    """
    pass

# Main function
def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()
