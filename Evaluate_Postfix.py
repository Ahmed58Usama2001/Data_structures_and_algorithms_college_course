from Stack_Implementation import *
def domath(operator,op1,op2):
    if operator =="+":
        return op1+op2

    elif operator =="-":
        return op1-op2

    elif operator =="*":
        return op1*op2

    elif operator =="/":
        return op1/op2


def postfixeval(postfixexpr):
    tokenlist=postfixexpr.split()
    opstack=stack()
    for token in tokenlist:
        if token in "0123456789":
            opstack.push(int(token))
        else:
            operand2=opstack.pop()
            operand1=opstack.pop()
            result=domath(token,operand1,operand2)
            opstack.push(result)

    return opstack.pop()

print(postfixeval("7 8 + 3 2 + /"))