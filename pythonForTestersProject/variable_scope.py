def example_function():
    local_var = "I'm local var"
    print(f"Inside example_function: {local_var}")

example_function()

global_var = "I'm global var"
def example_function_2():
    global global_var
    global_var = "I'm modified global var"
    print(f"Inside example_function_2: {global_var}")

example_function_2()
print(f"Outside example_function_2: {global_var}")