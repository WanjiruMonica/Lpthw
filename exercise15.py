# run this program from the windows command prompt
# create a text file and save it in the same folder as this python file; here I used exercise15_sample.txt.
# make sure to change the directory to where the folder with the files is located.
# you'll need two arguments to run this file the first time;
# That is exercise15.py(this is the script) and exercise15_sample.txt(this is the filename)
# Therefore in this case the command will look like G:\My Drive\Jenga school\Python\Assignments\Lpthw>python exercise15.py exercise15_sample.txt
# Don't forget to type python before the key words.

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
