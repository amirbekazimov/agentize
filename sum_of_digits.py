# Script to calculate the sum of numbers

if __name__ == "__main__":
    print("Enter numbers separated by commas (e.g., 1,2,3):\n")
    
    try:
        user_input = input("Enter numbers: ").strip()
        
        # Split by comma and convert to integers
        numbers = [int(x.strip()) for x in user_input.split(',')]
        
        # Calculate sum of all numbers
        result = sum(numbers)
        
        # Print the result
        print(f"\nNumbers: {numbers}")
        print(f"Result: {result}")
            
    except ValueError:
        print("Invalid input! Please enter valid integers separated by commas.\n")