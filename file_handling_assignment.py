# Step 1: File Creation and Writing
# Creates a new text file named "my_file.txt" and writes some lines to it
with open("my_file.txt", 'w') as file:
    file.write("This is the first line of text.\n")
    file.write("Here is the number 42.\n")
    file.write("The final line for now!\n")

# Step 2: File Reading and Display
# Reads the content of "my_file.txt" and displays it on the console
print("Content after first write:")
with open("my_file.txt", 'r') as file:
    content = file.read()
    print(content)

# Step 3: File Appending
# Opens "my_file.txt" in append mode and adds more lines
with open("my_file.txt", 'a') as file:
    file.write("Appending more content now.\n")
    file.write("Second appended line, number 58.\n")
    file.write("This is the final appended line!\n")

# Step 4: Read and Display the updated content
print("Content after appending:")
with open("my_file.txt", 'r') as file:
    updated_content = file.read()
    print(updated_content)
