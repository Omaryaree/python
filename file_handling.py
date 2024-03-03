#f1= open("my_file.txt", "a")
#f1.write("\nI live in Kenya")
# print(f1.read())
#f1.write("My name is Omar\n")
#f1.write("My no is 345670248")

try:
    # Open the file in append mode ('a')
    with open("my_file2.txt", "r") as file:
        # Append additional lines of text to the file
        file.write("\nLine appended 1.\n")
        file.write("Line appended 2.\n")
        file.write("Line appended 3.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred: {e}")
finally:
    print("File appending completed.")