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
        new_char = random.choice(['x']) if prev_char == '.' else random.choice(['.', 'x'])  # prevent '..'
        name_list[index] = new_char
        prev_char = new_char
    
    modified_name = ''.join(name_list)
    return modified_name

name = input("Enter a name: ")

# prevent same names
modified_names = set()

while len(modified_names) < 10:
    modified_name = replace_random_chars(name)
    modified_names.add(modified_name)

for modified_name in modified_names:
    print("Modified:", modified_name)
