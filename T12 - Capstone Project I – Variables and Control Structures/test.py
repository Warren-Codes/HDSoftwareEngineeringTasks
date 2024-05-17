example_list = ["Dave", "Rob", "Stephen"]
example_boolean = True
example_string = "hello world"
print(type(example_list))
print(type(example_boolean))
print(type(example_string))


# even a function is an instance of the function class!
def this_is_a_function(a, b):
    return a * b


print(type(this_is_a_function))
