# getinput.py

def get_user_input():
    user_inputs = []
    while True:
        user_input = input("")
        if user_input.strip() == "":
            break
        user_inputs.append(user_input)
    return "\n".join(user_inputs)
