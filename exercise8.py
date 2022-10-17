formatter = "{} {} {} {}"  # will take 4 arguments not more not less for each print statement

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) #{} will be printed 16 times since calling formatter one time is calling {} 4 times
print(formatter.format(
    "Try your",
    "own text here",
    "maybe a poem",
    "Or a song about fear"
))
