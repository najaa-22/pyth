def read_number():
    while True:
        num = input("Enter a number (minimum 4 digits): ")
        if num.isdigit() and len(num) >= 4:
            return int(num)
            
        else:
        print("Invalid input. Please enter a number with at least 4 digits.")

def reverse_number(n):
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


number = read_number()
print("Original number:", number)
print("Reversed number:", reverse_number(number))
