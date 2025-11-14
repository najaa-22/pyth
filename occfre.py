def occurrence():
    s = input("Enter a string: ")
    char = input("Enter the character to find occurrence for: ")
    count = s.count(char)
    print(f"Occurrence of '{char}' in '{s}': {count}")

def frequency():
    s = input("Enter a string: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    print("Frequency of each character:")
    for char, count in freq.items():
        print(f"'{char}': {count}")

def factor():
    num = int(input("Enter a number to find its factors: "))
    factors = [i for i in range(1, num+1) if num % i == 0]
    print(f"Factors of {num}: {factors}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Occurrence")
        print("2. Frequency")
        print("3. Factor")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            occurrence()
        elif choice == '2':
            frequency()
        elif choice == '3':
            factor()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
