# run this program from the windows command prompt
# change the directory to where the python file is located and saved.
# This program requires two arguments to run the first time hence;
# Type in python then name of file.py(will be taken by script) followed by a name(will be user_name).
# For this one it will look like G:\My Drive\Jenga school\Python\Assignments\Lpthw>python exercise14.py Monica
# Follow the prompts as they come up.


from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}? ")
likes = input(prompt)

print(f"Where do you live {user_name}? ")
lives = input(prompt)

print("What kind of computer do you have? ")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")
