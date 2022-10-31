# run this program from the command prompt in windows.
# Change the directory to the folder where the python file is saved
# after changing directory, type python followed by name of file(name of file.py is first argument).
# Then write 3 more variables for first(apple) second(orange) and third(pineapple) since the program requires 4 arguments to run.
# In this case G:\My Drive\Jenga school\Python\Assignments\Lpthw>python exercise13.py apple orange pineapple

from sys import argv
# read the comments above for how to run this
script, first, second, third = argv

print("The script is called: ",script)
print("Your first variable is: ",first)
print("Your second variable is: ",second)
print("Your third variable is: ",third)
