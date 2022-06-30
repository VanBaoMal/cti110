# Converts feet to steps
def feet_to_steps(ft_walked):
    steps = int(ft_walked / 2.5)
    return steps
    
# Starts program, gets user input and calls function and prints result
if __name__ == '__main__':
    user_input = float(input())
    steps_output = feet_to_steps(user_input)
    print(steps_output)