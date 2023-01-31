from Stack_Implementation import *
def infixtopostfix(infxexpr):
    prec={"^":4,"*":3,"/":3,"+":2,"-":2,"(":1}
    opstack=stack()
    postfixlist=[]
    tokenlist=infxexpr.split()

    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        
        elif token =="(":
            opstack.push(token)
        
        elif token==")":
            toptoken=opstack.pop()
            while toptoken!="(":
                postfixlist.append(toptoken)
                toptoken=opstack.pop()
        
        else:
            while (not opstack.isempty()) and (prec[opstack.peek()]>=prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isempty():
        postfixlist.append(opstack.pop())
    
    return " ".join(postfixlist)

print(infixtopostfix("A * B + C * D"))