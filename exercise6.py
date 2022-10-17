types_of_people = 10 # this is 2 types of people but in binary
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't" #The double quotation makes it a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'") # The single quotation marks with {y} will remain even when the code runs

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) # after the statement, it will print the answer false

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)# The plus will make w and e be printed as one statement . You can also use end=''
