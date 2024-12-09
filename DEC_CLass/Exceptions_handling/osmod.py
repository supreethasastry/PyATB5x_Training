import os

print(os.getcwd())
# Returns the current working directory

# List files in the current directory
files = os.listdir('/Users/sastr/PycharmProjects/PyATB5x_Training')
print(f"Files in current directory: {files}")

# Create a new directory
# os.mkdir('Test2')

# Check if a file exists
file_exist = os.path.exists("TestData.txt")
print(file_exist)


print(os.name) # posix == mac, nt - windows