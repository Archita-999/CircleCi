# Function to convert a string to uppercase
def to_upper(name):
    return name.upper()
# Function to print a greeting message
def say_hello(name):
    # Using f-string to include the name in the output
    print(f'Hello, {name}')
# Main block - runs only when the script is executed directly
if __name__ == '__main__':
    # Assign a string to the variable 'name'
    name = 'TrainWithArchita'
      # Call the say_hello function with 'name'
    say_hello(name)
     # Call the to_upper function to convert the string to uppercase
    up = to_upper(name)
    # Print the uppercase version of the string
    print(up)