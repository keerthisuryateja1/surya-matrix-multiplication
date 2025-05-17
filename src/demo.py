from standard_multiply import standard_multiply
from strassen_multiply import strassen_multiply
from surya_multiply import surya_multiply

def main():
    A_full = [[3, 5], [5, 3]]
    B_full = [[2, 4], [4, 2]]
    A_surya = [3, 5]
    B_surya = [2, 4]

    print("Standard Multiplication Result:")
    print(standard_multiply(A_full, B_full))

    print("\nStrassen's Multiplication Result:")
    print(strassen_multiply(A_full, B_full))

    print("\nSurya's Multiplication Result:")
    print(surya_multiply(A_surya, B_surya))

    A_general = [[1, 2], [3, 4]]
    B_general = [[5, 6], [7, 8]]

    print("\nStandard Multiplication (General Matrices):")
    print(standard_multiply(A_general, B_general))

    print("\nStrassen's Multiplication (General Matrices):")
    print(strassen_multiply(A_general, B_general))

if __name__ == "__main__":
    main()
