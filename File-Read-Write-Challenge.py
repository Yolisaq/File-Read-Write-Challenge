# File Handling and Exception Handling Template

def read_and_modify_file(input_file, output_file):
    """
    Reads content from input_file, modifies it, and writes to output_file.
    Example modification: convert text to uppercase.
    """
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_file}' cannot be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask user for input file
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the new file to write modified content: ")
    
    read_and_modify_file(input_file, output_file)

if __name__ == "__main__":
    main()
