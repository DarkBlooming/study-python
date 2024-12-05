import utilities

def main():
    numbers = [45, 63, 32, 46, 27]

    average = utilities.calculate_average(numbers)
    print(f"Average number: {average}")

    max_number = utilities.find_max(numbers)
    print(f"Max number: {max_number}")

if __name__ == "__main__":
    main()