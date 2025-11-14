def replace_occurrences(input_str):
    if not input_str:
        return ""

    first_char = input_str[0]
    modified_str = first_char + input_str[1:].replace(first_char, '$')
    return modified_str


user_input = input("Enter a string: ")
result = replace_occurrences(user_input)
print("Modified string:", result)
