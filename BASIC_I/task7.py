#Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
#Sample filename : abc.java
#Output : java

filename = input("Enter the filename: ")
print(filename + " is the file you wanna check.")
file_extension = filename.split(".")
print("Imported file is " + repr(file_extension[-1]) + " file")