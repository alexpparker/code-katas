from data_structures.stack import Stack

def assessor(input_str):
    stack = Stack()
    for i in input_str:
        if i == "(":
            stack.push(i)
        elif i == ")":
            try:
                stack.pop()
            except:
                return -1
    if len(stack) == 0:
        return 0
    elif len(stack) > 0:
        return 1

if __name__ == "__main__":
    user_input = input("Enter your parenthetics: ")
    print(assessor(user_input))
