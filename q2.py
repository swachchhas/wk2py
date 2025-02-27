
full_name = input("Enter your full name: ")

name_parts = full_name.split()

# Get first letter of first and last name
first_initial = name_parts[0][0]
last_initial = name_parts[-1][0]

# Display initials in uppercase
print(f"Your initials are: {first_initial.upper()}.{last_initial.upper()}")
