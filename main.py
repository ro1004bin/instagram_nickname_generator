import random

def replace_random_chars(name, num_changes=3):
    if not name:
        return name
    
    length = len(name)
    if length <= 1:
        return name
    
    indices = random.sample(range(1, length), min(num_changes, length - 1))
    
    name_list = list(name)
    prev_char = ''
    
    for index in indices:
        before_char = name_list[index - 1] if index > 0 else ''
        after_char = name_list[index + 1] if index < length - 1 else ''
        
        if prev_char == '.' or before_char == '.' or after_char == '.':
            new_char = 'x'
        else:
            new_char = random.choice(['.', 'x'])
        
        name_list[index] = new_char
        prev_char = new_char
    
    return ''.join(name_list)

name = input("Enter a name: ")

while True:
    try:
        number = int(input("Enter the amount you would like to generate\n(10 or more is recommended): "))
        if number <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for _ in range(number):
    print("Modified:", replace_random_chars(name))
