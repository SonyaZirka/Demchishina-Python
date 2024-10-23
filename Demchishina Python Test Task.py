import re

def check_number(number):
    if number > 7:
        print("Hello")

def check_name(name):
    if name.capitalize() == "John":
        print(f"Hello, John")
    else:
        print("There is no such name")

def multiples_of_three(arr):
    multiples = [num for num in arr if num % 3 == 0]
    if multiples:
        print("Multiples of 3 in the array:", multiples)
    else:
        print("No multiples of 3 in the array.")

def check_brackets(sequence):
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(matching_brackets.values())

    for char in sequence:
        if char in opening_brackets:
            stack.append(char)
        elif char in matching_brackets:
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

def process_input(user_input):

    if re.match(r'^(-?\d+\s+)+-?\d+$', user_input):
        numbers_array = list(map(int, user_input.split()))
        multiples_of_three(numbers_array)

    elif re.match(r'^-?\d+$', user_input):
        check_number(int(user_input))

    elif re.match(r'^[()\[\]{}]+$', user_input):
        is_correct = check_brackets(user_input)
        if is_correct:
            print("The bracket sequence is correct.")
        else:
            print("The bracket sequence is incorrect.")

    else:
        check_name(user_input)

if __name__ == "__main__":
    while True:
        user_input = input("Enter something (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        process_input(user_input)