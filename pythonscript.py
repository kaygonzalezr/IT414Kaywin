def add_numbers(num1, num2):
    result = num1 + num2
    return result

def main():
    # Prompt the user to enter two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Call the fuction and store the result
    sum_result = add_numbers(number1, number2)

    # Display the result
    print("The sum is:",sum_result)

# Call the main function
if __name__ == "__main__":
    main()

def test_add_numbers():
    # Test case 1
    assert add_numbers(2, 3) == 5

    # Test case 2
    assert add_numbers(-10,5) == -5

    #Test case 3
    assert add_numbers(0, 0) == 0

    print("All the cases passed!")

# Call the unit test function
test_add_numbers()