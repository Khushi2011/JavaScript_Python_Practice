# The advantages of using if __name__ == “__main__” statement:
# Using the main in our file, we can restrict some data from exporting to other files when imported.
# We can restrict the unnecessary data, thus making the output cleaner and more readable.
# We can choose what others may import or what they may not while using our module.
#
# The value of the __name__ attribute is set to __main__ when the module is run as the main program.
# Otherwise, the value of __name__ is set to the name of the module.
# The if __name__ == “__main__” block prevents the certain code from being run when the module is imported.

from nameIsEqualToMain import add
ans=add(7,5)
print(ans)