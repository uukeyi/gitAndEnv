def isValid(string):
     stack = []
     valid_combinations = ['()', '[]', '{}']
     for char in string:
        if(char == "(" or char == '[' or char == '{'):
            stack.append(char)
        else:
            if(len(stack) != 0 and stack[len(stack) - 1] + char in valid_combinations):
                stack.append(char)
                del stack[-2:]
            else:
                return False
     return len(stack) == 0






print(isValid('(]'))




    #   (]){}
